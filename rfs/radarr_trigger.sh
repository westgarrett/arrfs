#!/bin/bash
ROOT_DIR="$(dirname ${0})"
VENV_DIR="${ROOT_DIR}/venv"
PYTHON_ENTRY="${ROOT_DIR}/main.py"
LOG_FILE="${ROOT_DIR}/logs/$(basename "${0}" .sh).log"
set -x
echo "$(whoami)"
ls -la "${ROOT_DIR}"

function log() {
    if [ ! -d  "${ROOT_DIR}/logs" ]
    then
        mkdir -p "${ROOT_DIR}/logs"
    fi
    log_date="$(date '+%Y-%m-%d %H:%M:%S')"
    echo  >> "${LOG_FILE}"
    for arg in "${@}"
    do 
        echo "[${log_date}] : [$(basename ${0} .sh)] : ${arg}" >> "${LOG_FILE}"
    done
}

# if [ ! -d "${VENV_DIR}" ]
# then
#     log "create a virtual environment and install requirements.txt"
#     mkdir -p ${VENV_DIR}
#     "$(which python3) -m venv ${VENV_DIR}"
#     source "${VENV_DIR}/bin/activate"
#     "$(which python3) -m pip install -r ${ROOT_DIR}/requirements.txt"
# else
#     source "${VENV_DIR}/bin/activate"
# fi

args="${@}"
if [ -z "${radarr_eventtype}" ]
then
    log "No radarr event type provided. Using \"Test\" as the default"
fi

log "Radarr \"${radarr_eventtype}\" triggered"
log "Running Python script with arguments: --callarr radarr ${args}"

"$(which python3)" "${PYTHON_ENTRY}" "--callarr" "radarr" ${args}
exit 0
