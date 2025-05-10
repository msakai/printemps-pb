# PRINTEMPS-pb

Wrapper of [PRINTEMPS](https://snowberryfield.github.io/printemps/) intended for submitting to [PB25 competition](https://www.cril.univ-artois.fr/PB25/).

## Solver information

### Suggested command line

```
python3 DIR/bin/main.py --time-limit TIMELIMIT --reserve-output-time 5 --tmpdir TMPDIR --seed RANDOMSEED BENCHNAME
```

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

## Requirements

* Python 3

## Build from source

* Install necessary packages
  * Ubuntu: `curl`, `g++`, `gcc`, `libc6-dev`, `libffi-dev`, `libgmp-dev`, `libncurses-dev`, `make`, `xz-utils`, `zlib1g-dev`, `git`, `gnupg`, `netbase`, `cmake`
* Install the [Haskell Tool Stack](https://docs.haskellstack.org/en/stable/)
  * `curl -sSL https://get.haskellstack.org/ | sh`
* Run `build.sh` or `build_static.sh`
