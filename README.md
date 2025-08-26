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

## Submission for [Pseudo Boolean Competition 2025 (PB25)](https://www.cril.univ-artois.fr/PB25/)

* [Solver archive](https://github.com/msakai/printemps-pb/releases/download/PB25-submission-20250528/printemps-pb.tar.gz) ([Github Release](https://github.com/msakai/printemps-pb/releases/tag/PB25-submission-20250528))
* [Solver description](description/description.pdf)

### Some results

#### Complete solver point of view (Number of solved instances, tie broken by CPU time)

> [!NOTE]
> Since PRINTEMPS is an INCOMPLETE solver, it cannot SOLVE instances from a complete solver point of view, except for instances where the answers are SAT.

PRINTEMPS:

|category|all instances|# solved|rank|
|-|-:|-:|-:|
|DEC-LIN|502|104|35th among 36 solvers|
|DEC-LIN (SAT answers)|165|104|28th among 36 solvers|
|DEC-NLC|10|8|5th among 12 solvers|
|DEC-NLC (SAT answers)|8|8|4th among 12 solvers|
|OPT-LIN|555|0|45th among 46 solvers|
|OPT-NLC|57|0|12th among 12 solvers|
|PARTIAL-LIN|208|0|9th among 9 solvers|
|SOFT-LIN|60|0|9th among 9 solvers|

PRINTEMPS (20 cores):

|category|all instances|# solved|rank|
|-|-:|-:|-:|
|DEC-LIN|502|104|36th among 36 solvers|
|DEC-LIN (SAT answers)|165|104|31st among 36 solvers|
|DEC-NLC|10|8|7th among 12 solvers|
|DEC-NLC (SAT answers)|8|8|6th among 12 solvers|
|OPT-LIN|555|0|46th among 46 solvers|
|OPT-NLC|57|0|12th among 12 solvers|

Source:
- [PBS/PBO: CPU Ranking of solvers on all selected instances (including those not supported by some solvers)](https://www.cril.univ-artois.fr/PB25/results/results.php?idev=115)
- [WBO: Ranking of solvers](https://www.cril.univ-artois.fr/PB25/results/results.php?idev=118)


#### Number of times the solver is able to give the best known answer from an incomplete solver point of view (i.e. without considering optimality proof)

> [!NOTE]
> These results are computed from the table on “Results for each bench by categories” pages.

PRINTEMPS:

|category|all instances|# best known|rank|
|-|-:|-:|-:|
|[DEC-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=112)|502|104|35th-36th (tie) among 36 solvers|
|[DEC-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=116)|10|8|4th-11th (tie) among 12 solvers|
|[OPT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=113)|555|231|37th among 46 solvers|
|[OPT-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|57|23|8th-9th (tie) among 13 solvers|
|[PARTIAL-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=118&idcat=119)|208|135|7th among 9 solvers|
|[SOFT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|60|47|8th among 9 solvers|

PRINTEMPS (20 cores):

|category|all instances|# best known|rank|
|-|-:|-:|-:|
|[DEC-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=112)|502|104|35th-36th (tie) among 36 solvers|
|[DEC-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=116)|10|8|4th-11th (tie) among 12 solvers|
|[OPT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=113)|555|245|36th among 46 solvers|
|[OPT-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|57|23|8th-9th (tie) among 13 solvers|

#### Number of times the solver is the best solver from an incomplete solver point of view

> [!NOTE]
> These results are computed from the table on “Results for each bench by categories” pages.

PRINTEMPS:

|category|all instances|# best solver|rank|
|-|-:|-:|-:|
|[DEC-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=112)|502|9|9th among 36 solvers|
|[DEC-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=116)|10|1|3rd-4th (tie) among 12 solvers|
|[OPT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=113)|555|42|6th among 46 solvers|
|[OPT-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|57|6|4th-5th (tie) among 13 solvers|
|[PARTIAL-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=118&idcat=119)|208|57|2nd among 9 solvers|
|[SOFT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|60|24|1st among 9 solvers|

PRINTEMPS (20 cores):

|category|all instances|# best solver|rank|
|-|-:|-:|-:|
|[DEC-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=112)|502|13|4th among 36 solvers|
|[DEC-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=116)|10|1|3rd-4th (tie) among 12 solvers|
|[OPT-LIN](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=113)|555|65|3rd among 46 solvers|
|[OPT-NLC](https://www.cril.univ-artois.fr/PB25/results/globalbybench.php?idev=115&idcat=117)|57|10|2nd-3rd (tie) among 13 solvers|
