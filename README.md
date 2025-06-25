# PRINTEMPS for Pseudo Boolean Competition

[PRINTEMPS](https://snowberryfield.github.io/printemps/) solver for [PB25 competition](https://www.cril.univ-artois.fr/PB25/) submission.

## Solver information

[Solver description](description/description.pdf)

### Suggested command line

Using `runsolver`:

```
DIR/bin/runsolver -d 5 -C $((TIMELIMIT-5-1)) -W $((TIMELIMIT-5-1)) -v TMPDIR/out.v -w TMPDIR/out.w DIR/bin/pb_competition_2025_solver -k -1 -t -1.0 -j NBCORE -r RANDOMSEED BENCHNAME
```

Without using `runsolver`:

```
DIR/bin/pb_competition_2025_solver -k -1 -t $((TIMELIMIT-5)) -j NBCORE -r RANDOMSEED BENCHNAME
```

Since it may take some time to print solution after receiving the SIGTERM, some amount of time is subtracted from time limit to have enough time to print solution.

Also, since `pb_competition_2025_solver` only supports time limits in wall clock time but not support time limits in CPU time, it is wrapped by `runsolver` to support time limits in CPU time.

### Complete or not?

* ☐ Complete (your solver can answer UNSATISFIABLE)
* ☑ Incomplete (your solver can find solutions but cannot prove that there is no solution)

### Categories of benchmarks

* ☑ DEC-LIN (decision problem, linear constraints, no UNSAT certificate)
* ☐ DEC-LIN-CERT (decision problem, linear constraints, UNSAT certificate required)
* ☑ DEC-NLC (decision problem, non-linear constraints, no UNSAT certificate)
* ☑ OPT-LIN (optimization problem, linear constraints, no OPT/UNSAT certificate)
* ☐ OPT-LIN-CERT (optimization problem, linear constraints, OPT/UNSAT certificate required)
* ☑ OPT-NLC (optimization problem, non-linear constraints, no OPT/UNSAT certificate)
* ☑ PARTIAL-LIN (WBO, both soft and hard constraints, linear constraints)
* ☑ SOFT-LIN (WBO, only soft constraints, linear constraints)

## Binary executables

Statically linked executables are included in the submission archive.

Note that `pb_competition_2025_solver` was built using `-march broadwell`.
If the architecture of the evaluation environment is older than Broadwell, please build from source code using the following instructions.

## Build from source code

* Option 1.
    1. Install necessary packages (e.g. `cmake`, `gcc`, `g++`, `libnuma-dev`, `make` on Ubuntu Linux)
    2. Run `bash build.sh` or `bash build_static.sh`
* Option 2 (Statically linking `musl` instead of `glibc`).
    1. Install Docker
    2. Run `docker run -v $(pwd):/work -w /work --rm --user=root alpinelinux/build-base sh -c "apk add numactl-dev && sh build_static.sh"`
