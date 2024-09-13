#!/bin/bash

# Define the default values for the paths
config_path="/home/gw/docker_stuff/radarr/config"
downloads_path="/home/gw/rfs/rfs/tc_drive"
custom_path="/home/gw/rfs/rfs/"
storage_paths=("/home/gw/rfs/rfs/storage0" "/home/gw/rfs/rfs/storage1")  # Add more storage paths as needed

# Define the options and their corresponding variables
while getopts ":c:d:s:m:" opt; do
  case $opt in
    c) config_path="$OPTARG";;
    d) downloads_path="$OPTARG";;
    s) custom_path="$OPTARG";;
    m) storage_paths+=("$OPTARG");;  # Append to the storage_paths array
    \?) echo "Invalid option: -$OPTARG"; exit 1;;
  esac
done

# Rest of the script remains the same
docker_dir="$(pwd)/docker-radarr"

if [ ! -d "${docker_dir}" ]; then
    git clone https://github.com/linuxserver/docker-radarr.git
fi

cp "$(pwd)/Dockerfile" "${docker_dir}"
cd "${docker_dir}"

tag=$(date +'%d.%m.%Y_%N')
sudo docker build --no-cache --pull -t lscr.io/linuxserver/radarr:"${tag}" .
rm -rf "${docker_dir}"

echo """
---
services:
  radarr:
    image: radarr:${tag}
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
""" > docker-compose.yml