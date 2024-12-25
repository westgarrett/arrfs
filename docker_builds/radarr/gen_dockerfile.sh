#!/bin/bash
set -x
script_dir="$(dirname ${0})"
repo="https://github.com/westgarrett/arrfs.git"
branch="$(git rev-parse --abbrev-ref HEAD)"
# checkout=true
# branch_single=true
branch_args=${branch_single:-true} && branch_args="--single-branch" || branch_args=""
# no_checkout=${checkout:-true} && checkout_args="--no-checkout" || checkout_args=""
destination="/app/arrfs"
if [ -f "${script_dir}/Dockerfile" ]
then
    echo "previous Dockerfile found, removing it"
    rm "${script_dir}/Dockerfile"
fi

cp "${script_dir}/Dockerfile.template" "${script_dir}/Dockerfile"

sed -i 's|GIT_BRANCH|-b '${branch}'|g' "${script_dir}/Dockerfile"
sed -i 's|BRANCH_SINGLE|'${branch_args}'|g' "${script_dir}/Dockerfile"
# sed -i 's|GIT_CHECKOUT|'${checkout_args}'|g' "${script_dir}/Dockerfile"
sed -i 's|GIT_REPO|'${repo}'|g' "${script_dir}/Dockerfile"
sed -i 's|GIT_DESTINATION|'${destination}'|g' "${script_dir}/Dockerfile"