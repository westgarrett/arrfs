#!/bin/bash
LOG_FILE="logs/$(basename "${0}" .sh).log"
PYTHON_ENTRY="main.py"
set -e

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$(basename ${0} .sh)]" "${1}" >> "${LOG_FILE}"
}

args="${@}"
if [ -z "${radarr_eventtype}" ]
then
    log "No radarr event type provided. Using \"Test\" as the default"
fi

log "Radarr \"${radarr_eventtype}\" triggered"
log "Running Python script with arguments: --callarr radarr ${args}"

python3 "${PYTHON_ENTRY}" "--callarr" "radarr" ${args}
exit 0
