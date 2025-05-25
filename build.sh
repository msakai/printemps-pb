set -eu

# apt-get update
# apt-get install -y cmake gcc g++ make

mkdir -p bin

(cd src/printemps && make -f makefile/Makefile.extra && cp build/extra/Release/pb_competition_2025_solver ../../bin)

(
  cd src/runsolver/src \
  && make \
  && cp runsolver ../../../bin/
)
