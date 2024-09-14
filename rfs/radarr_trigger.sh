#!/bin/bash
ROOT_DIR="$(dirname ${0})"
VENV_DIR="${ROOT_DIR}/venv"
PYTHON_ENTRY="${ROOT_DIR}/main.py"
LOG_FILE="${ROOT_DIR}/logs/$(basename "${0}" .sh).log"
# set -x
echo "$(whoami)"
ls -la "${ROOT_DIR}"

function log() {
    log_date="$(date '+%Y-%m-%d %H:%M:%S')"
    log_str="[${log_date}] : [$(basename ${0} .sh)]"
    if [ "${1}" == "true" ]
    then
        shift
        for arg in "${@}"
        do 
            echo "${log_str} : ${arg}"
        done
    else
        shift
        if [ ! -d  "${ROOT_DIR}/logs" ]
        then
            mkdir -p "${ROOT_DIR}/logs"
        fi
        for arg in "${@}"
        do 
            echo "${log_str} : ${arg}" >> "${LOG_FILE}"
        done
    fi
}

function get_venv() {
    remote="${1}"
    if [ if ! "${remote}" == "true" || ! -d "${VENV_DIR}" ]
    then
        log "create a virtual environment and install requirements.txt"
        mkdir -p ${VENV_DIR}
        "$(which python3) -m venv ${VENV_DIR}"
        source "${VENV_DIR}/bin/activate"
        "$(which python3) -m pip install -r ${ROOT_DIR}/requirements.txt"
    else
        log "venv already exists"
        source "${VENV_DIR}/bin/activate"
    fi
}

remote=false
if [ "$(whoami)" == "abc" ]
then
    remote="true"
fi

get_venv "${remote}"

args="${@}"
if [ -z "${radarr_eventtype}" ]
then
    radarr_eventtype="Test"
    log "${remote}" "No radarr event type provided. Using \"Test\" as the default"
fi

log "${remote}" "Radarr \"${radarr_eventtype}\" triggered"
log "${remote}" "Running Python script with arguments: --callarr radarr ${args}"

"$(which python3)" "${PYTHON_ENTRY}" "--callarr" "radarr" ${args}
exit 0
