set -eu

# apt-get update
# apt-get install -y cmake gcc g++ make

(cd src/printemps && make -f makefile/Makefile.extra STATIC=ON && cp build/extra/Release/pb_competition_2025_solver ../../bin)

(
  cd src/runsolver/src \
  && docker run -v $(pwd):/work -w /work --rm --user=root alpinelinux/build-base sh -c "apk add numactl-dev && make STATIC=-static" \
  && cp runsolver ../../../bin/
)
