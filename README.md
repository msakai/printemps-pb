# PRINTEMPS-pb

Wrapper of [PRINTEMPS](https://snowberryfield.github.io/printemps/) intended for submitting to [PB25 competition](https://www.cril.univ-artois.fr/PB25/).

## Solver information

### Suggested command line

Using `runsolver`:

```
DIR/bin/runsolver -d 5 -C $((TIMELIMIT-5-1)) -W $((TIMELIMIT-5-1)) -v TMPDIR/out.v -w TMPDIR/out.w DIR/bin/pb_competition_2025_solver -k 10000000 -j NBCORE -r RANDOMSEED BENCHNAME
```

Without using `runsolver`:

```
DIR/bin/pb_competition_2025_solver -k 10000000 -t TIMELIMIT -j NBCORE -r RANDOMSEED BENCHNAME
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

## Build from source

* Install necessary packages
  * Ubuntu: `cmake`, `gcc`, `g++`, `make`
* Run `build.sh` or `build_static.sh`
