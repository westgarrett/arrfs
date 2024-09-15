#!/bin/bash
ROOT_DIR="$(dirname ${0})"
VENV_DIR="${ROOT_DIR}/venv"
REMOTE=false
PYTHON_ENTRY="${ROOT_DIR}/main.py"
LOG_FILE="${ROOT_DIR}/logs/$(basename "${0}" .sh).log"
# set -x
ls -la "${ROOT_DIR}"

function log() {
    log_date="$(date '+%Y-%m-%d %H:%M:%S')"
    if "${REMOTE}"
    then
        log_str="[$(basename ${0} .sh).remote]"
        for arg in "${@}"
        do
            if  [ "${arg}" ]
            then
                echo "${log_str} : ${arg}"
            fi
        done
    else
        if [ ! -d  "${ROOT_DIR}/logs" ]
        then
            mkdir -p "${ROOT_DIR}/logs"
        fi
        log_str="[$(basename ${0} .sh).local]"
        for arg in "${@}"
        do
            if [ "${arg}" ]
            then
                echo "[${log_date}] : ${log_str} : ${arg}" >> "${LOG_FILE}"
            fi
        done
    fi
}

function get_venv() {
    if "${REMOTE}"
    then
        VENV_DIR="/app/venv"
    else
        if [ ! -d "${VENV_DIR}" ]
        then
            log "create a virtual environment and install requirements.txt"
            mkdir -p "${VENV_DIR}"
            "$(which python3) -m venv ${VENV_DIR}"
            "$(which python3) -m pip install -r ${ROOT_DIR}/requirements.txt"
        fi
    fi
    log "Activating the virtual environment in ${VENV_DIR}"
    source "${VENV_DIR}/bin/activate"
}

if [ "$(whoami)" == "abc" ]
then
    VENV_DIR="/app/venv"
    REMOTE=true
fi

get_venv

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
