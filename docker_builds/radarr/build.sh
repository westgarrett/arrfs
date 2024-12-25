#!/bin/bash

script_path="$(dirname ${0})"

# Define the default paths
git_repo="https://github.com/linuxserver/docker-radarr.git"
config_path="${script_path}/config"
downloads_path="/tmp"
custom_path="/tmp"
storage_paths=( "${script_path}/storage0" "${script_path}/storage1" )  # Add more storage paths as needed

# Define options
while getopts ":r:c:d:s:m:" opt; do
  case "${opt}" in
    r) git_repo="${OPTARG}";;
    c) config_path="${OPTARG}";;
    d) downloads_path="${OPTARG}";;
    s) custom_path="${OPTARG}";;
    m) storage_paths+=("${OPTARG}");;
    \?) echo "Invalid option: -${OPTARG}"; exit 1;;
  esac
done

docker_dir="${script_path}/docker-radarr"

if [ ! -d "${docker_dir}" ]
then
    git clone "${git_repo}" "${docker_dir}"
fi

if [ ! -d "${config_path}" ]
then
  echo "${config_path} doesn't exist, creating..."
  mkdir -p "${config_path}"
fi 

for path in "${storage_paths[@]}"
do 
  if [ ! -d "${path}" ]
  then
    echo "${path} doesn't exist, creating..."
    mkdir -p "${path}"
  fi
done

if [ -f "${script_path}/Dockerfile" ]
then
  cp "${script_path}/Dockerfile" "${docker_dir}"
else
  echo "Dockerfile not found in script directory, generating"
  bash "${script_path}/gen_dockerfile.sh"
fi

wd="$(pwd)"
cd "${docker_dir}"

tag=$(date +'%d.%m.%Y_%H.%M.%s')

sudo docker build --no-cache --pull -t lscr.io/linuxserver/radarr:"${tag}" .
rm -rf "${docker_dir}"
cd "${wd}"

cat << EOF > ${script_path}/docker-compose.yml
---
services:
  radarr:
    image: lscr.io/linuxserver/radarr:${tag}
    container_name: radarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ${config_path}:/config
      - ${downloads_path}:/downloads
      - ${custom_path}:/custom
      - ${storage_paths[0]}:/movies0
      - ${storage_paths[1]}:/movies1  # Add more storage paths as needed
    ports:
      - 7878:7878
    restart: unless-stopped
EOF