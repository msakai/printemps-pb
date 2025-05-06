import argparse
import json
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument('--time-limit', type=int, default=30)
parser.add_argument('--tmpdir')
parser.add_argument('--seed', type=int)
parser.add_argument('benchname')
args = parser.parse_args()

cwd = Path.cwd()
bin_dir = Path(__file__).parent.resolve()
benchname = cwd / args.benchname
tmpdir = cwd / args.tmpdir

incumbent_path = tmpdir / "incumbent.json"
incumbent_path.unlink(missing_ok=True)

# Read metadata
is_opt = False
with open(args.benchname) as f:
    line = f.readline()
    assert line.startswith('* ')
    tmp = line[1:].strip().split()
    assert len(tmp) % 2 == 0

    hint = {}
    for i in range(len(tmp) // 2):
        hint[tmp[i*2]] = tmp[i*2+1]

    num_variables = int(hint["#variable="])
    int_size = int(hint["intsize="])

    while line := f.readline():
        if line.startswith('*'):
            continue
        is_opt = line.startswith('min:') or line.startswith('soft:')
        break

if int_size >= 53:
    print("s UNSUPPORTED")
    exit()

mps_filename = tmpdir / (Path(args.benchname).stem + ".mps")

subprocess.run(
    [bin_dir / "toyconvert", args.benchname, "-o", str(mps_filename), "--linearize"],
    check=True,
    input="",
    encoding="us-ascii",
)

mps_solver_args = [
    str(bin_dir / "mps_solver"),
    str(mps_filename),
    "--include-mps-loading-time",  # Include MPS file loading time in the calculation time.
    "-k", "1000000000",  # ITERATION_MAX
    "-v", "Outer",  # VERBOSE
]

if args.seed is not None:
    options = {
        "general": {
            "seed": args.seed,
        }
    }
    with open(tmpdir / "options.json", "w") as f:
        json.dump(options, f)
    mps_solver_args.append(str(tmpdir / "options.json"))

start_time_2 = time.time()
mps_solver_args.extend(["-t", str(int(args.time_limit - (start_time_2 - start_time)))])  # TIME_MAX

popen = subprocess.Popen(
    mps_solver_args,
    stdin=subprocess.DEVNULL,
    stdout=subprocess.PIPE,
    stderr=None,
    encoding="us-ascii",
    cwd=tmpdir,
)

def handle_sigterm(signum, frame):
    # Send SIGTERM to the child process
    popen.terminate()

signal.signal(signal.SIGTERM, handle_sigterm)

# Ctrl-C sends SIGINT to both the parent and child processes.
# The parent process (this process) ignores it and waits for the child process to terminate.
signal.signal(signal.SIGINT, signal.SIG_IGN)

o_value = None
incumbent_objective_pat = re.compile(r'^INFO\s+:\s+-- Incumbent objective: ([^ ]+)')
incumbent_violation_pat = re.compile(r'^INFO\s+:\s+-- Incumbent violation: ([^ ]+)')

while line := popen.stdout.readline():
    if line.startswith("# Incumbent Summary"):
        line = popen.stdout.readline()
        if "Status: Feasible incumbent objective was updated." in line or "Status: Global incumbent objective was updated." in line:
            line = popen.stdout.readline()  # elapsed time
            line = popen.stdout.readline()  # Incumbent objective
            m = re.match(incumbent_objective_pat, line.strip())
            val = int(float(m.group(1)))
            line = popen.stdout.readline()  # Incumbent violation
            m = re.match(incumbent_violation_pat, line.strip())
            violation = int(float(m.group(1)))
            if is_opt and violation == 0 and (o_value is None or val < o_value):
                print(f"o {val}", flush=True)
                o_value = val
        else:
            continue

popen.wait()

# with open(tmpdir / "status.json", "r") as f:
#     status = json.load(f)

if not incumbent_path.exists():
    print("s UNKNOWN")
    exit()
    
with open(incumbent_path, "r") as f:
    incumbent = json.load(f)

if not incumbent["is_found_feasible_solution"]:
    print("s UNKNOWN")
    exit()

if is_opt:
    val = int(incumbent["objective"])
    if o_value is None or val < o_value:
        print(f"o {val}")

print("s SATISFIABLE")

var_pat = re.compile(r'^x(\d+)$')
sol = {}
for var, val in incumbent["variables"].items():
    if m := re.fullmatch(var_pat, var):
        sol[int(m.group(1))] = val

for base in range(1, num_variables + 1, 10):
    sys.stdout.write("v")
    for i in range(base, min(base+10, num_variables + 1)):
        if sol.get(i, 0) > 0.5:
            sys.stdout.write(f" x{i}")
        else:
            sys.stdout.write(f" -x{i}")
    sys.stdout.write("\n")
sys.stdout.flush()
