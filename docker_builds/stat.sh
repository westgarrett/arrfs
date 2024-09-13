#!/bin/bash
script_path="$(dirname $(readlink -f ${0}))"

while getopts ":s:d:" opt; do
  case "${opt}" in
    s) service="${OPTARG}";;
    d) direction="${OPTARG}";;
    \?) echo "Invalid option: -${OPTARG}"; exit 1;;
  esac
done

if  [ -z "${service}" ] || [ -z "${direction}" ]
then
    echo "Usage: $0 -s ${service:-'<service>'} -d ${direction:-'<up|down>'}"
    exit 1
fi

if [ ! -d "${script_path}/${service}" ]
then
    echo "Error: service '${service}' not found in ${script_path}"
    exit 1
fi

if  [ "${direction}" != "up" ] && [ "${direction}" != "down" ]
then
    echo "Error: '${direction}' is neither up nor down"
    exit 1
fi

if [ ! -f "${script_path}/${service}/docker-compose.yml" ]
then
    echo "Error: docker-compose.yml file not found in ${script_path}"
    echo "Run ${script_path}/${service}/build.sh first!"
    exit 1
fi

sudo docker-compose -f "${script_path}/${service}/docker-compose.yml" up -d
sudo docker ps

exit 0