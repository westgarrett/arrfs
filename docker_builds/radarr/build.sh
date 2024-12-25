#!/bin/bash
set -x
script_path="$(dirname $(realpath ${0}))"

# Define the default paths
git_repo="https://github.com/linuxserver/docker-radarr.git"
config_path="${script_path}/config"
downloads_path="/tmp"
custom_path="/tmp"
docker_dir="/tmp/docker-radarr"
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

bash "${script_path}/gen_dockerfile.sh"
cp "${script_path}/Dockerfile" "${docker_dir}"

tag=$(date +'%d.%m.%Y_%H.%M.%s')

cd "${docker_dir}"
sudo docker build --no-cache --pull -t lscr.io/linuxserver/radarr:"${tag}" .
cd "${script_path}"
rm -rf "${docker_dir}"

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