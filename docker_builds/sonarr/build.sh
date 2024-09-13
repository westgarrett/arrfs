#!/bin/bash

script_path="$(dirname $(readlink -f ${0}))"

# Define the default paths
git_repo="https://github.com/linuxserver/docker-sonarr.git"
config_path="/home/${USER}/docker_stuff/sonarr/config"
downloads_path="/home/${USER}/rfs/rfs/tc_drive"
custom_path="/home/${USER}/rfs/rfs/"
storage_paths=("/home/${USER}/rfs/rfs/storage0" "/home/${USER}/rfs/rfs/storage1")  # Add more storage paths as needed

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

docker_dir="${script_path}/docker-sonarr"

if [ ! -d "${docker_dir}" ]; then
    git clone "${git_repo}" "${docker_dir}"
fi

if [ -f "${script_path}/Dockerfile" ]
then
  cp "${script_path}/Dockerfile" "${docker_dir}"
fi

wd="$(pwd)"
cd "${docker_dir}"

tag=$(date +'%d.%m.%Y_%N')
sudo docker build --no-cache --pull -t lscr.io/linuxserver/sonarr:"${tag}" .
rm -rf "${docker_dir}"
cd "${wd}"

cat << EOF > ${script_path}/docker-compose.yml
---
services:
  sonarr:
    image: lscr.io/linuxserver/sonarr:${tag}
    container_name: sonarr
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - ${config_path}:/config
      - ${downloads_path}:/downloads
      - ${custom_path}:/custom
      - ${storage_paths[0]}:/shows0
      - ${storage_paths[1]}:/shows1  # Add more storage paths as needed
    ports:
      - 7878:7878
    restart: unless-stopped
EOF