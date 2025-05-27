set -eu

# apt-get update
# apt-get install -y cmake gcc g++ libnuma-dev make

mkdir -p bin

make -C src/printemps -f makefile/Makefile.extra STATIC=ON MARCH=broadwell MTUNE=cascadelake
cp src/printemps/build/extra/Release/pb_competition_2025_solver bin/

make -C src/runsolver/src STATIC=-static
cp src/runsolver/src/runsolver bin/
