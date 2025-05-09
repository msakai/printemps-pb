set -eu

# apt-get update
# apt-get install -y curl g++ gcc libc6-dev libffi-dev libgmp-dev libncurses-dev make xz-utils zlib1g-dev git gnupg netbase cmake
# curl -sSL https://get.haskellstack.org/ | sh

# stack_docker_args=(--docker --docker-image "quay.io/benz0li/ghc-musl:9.6.6" --docker-run-args "--platform linux/amd64")
stack_docker_args=(--docker --docker-image "quay.io/benz0li/ghc-musl:9.6.6")

(
  cd src/toysolver \
  && stack build --flag toysolver:optparse-applicative-018 --flag toysolver:LinuxStatic --flag toysolver:ForceChar8 --flag toysolver:-BuildForeignLibraries "${stack_docker_args[@]}" \
  && cp "$(stack path --local-install-root "${stack_docker_args[@]}")/bin/toyconvert" ../../bin
)

(cd src/printemps && make -f makefile/Makefile.application STATIC=ON && cp build/application/Release/mps_solver ../../bin)
