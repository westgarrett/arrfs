#!/bin/bash
ROOT_DIR="/custom"
VENV_DIR="/config/venv"
LOG_FILE="${ROOT_DIR}/logs/$(basename "${0}" .sh).log"
PYTHON_ENTRY="${ROOT_DIR}/main.py"
set -x

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$(basename ${0} .sh)]" "${1}" >> "${LOG_FILE}"
}

if [ ! -d "${VENV_DIR}" ]
then
    log "create a virtual environment and install requirements.txt"
    mkdir -p ${VENV_DIR}
    "$(which python3) -m venv ${VENV_DIR}"
    source "${VENV_DIR}/bin/activate"
    "$(which python3) -m pip install -r ${ROOT_DIR}/requirements.txt"
else
    source "${VENV_DIR}/bin/activate"
fi

args="${@}"
if [ -z "${radarr_eventtype}" ]
then
    log "No radarr event type provided. Using \"Test\" as the default"
fi

log "Radarr \"${radarr_eventtype}\" triggered"
log "Running Python script with arguments: --callarr radarr ${args}"

"$(which python3) ${PYTHON_ENTRY}" "--callarr" "radarr" ${args}
exit 0
