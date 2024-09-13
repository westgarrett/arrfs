#!/bin/bash
script_path="$(dirname $(readlink -f ${0}))"
repo="https://github.com/westgarrett/rfs.git"
branch="$(git rev-parse --abbrev-ref HEAD)"
destination="/app/rfs"
if [ -f "${script_path}/Dockerfile" ]
then
    echo "previous Dockerfile found, removing it"
    rm "${script_path}/Dockerfile"
fi

cp "${script_path}/Dockerfile.template" "${script_path}/Dockerfile"

sed -i 's|GIT_BRANCH|"-b '${branch}' --single-branch"|g' "${script_path}/Dockerfile"
sed -i 's|GIT_REPO|'${repo}'|g' "${script_path}/Dockerfile"
sed -i 's|GIT_DESTINATION|'${destination}'|g' "${script_path}/Dockerfile"