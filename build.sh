set -eu

# apt-get update
# apt-get install -y curl g++ gcc libc6-dev libffi-dev libgmp-dev libncurses-dev make xz-utils zlib1g-dev git gnupg netbase cmake
# curl -sSL https://get.haskellstack.org/ | sh

(
  cd src/toysolver \
  && stack build --flag toysolver:optparse-applicative-018 --flag toysolver:ForceChar8 --flag toysolver:-BuildForeignLibraries \
  && cp "$(stack path --local-install-root)/bin/toyconvert" ../../bin
)

(cd src/printemps && make -f makefile/Makefile.application && cp build/application/Release/mps_solver ../../bin)

(
  cd src/runsolver/src \
  && make \
  && cp runsolver ../../../bin/
)
