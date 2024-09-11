#!/bin/bash
LOG_FILE="logs/$(basename "${0}" .sh).log"
PYTHON_ENTRY="main.py"
set -e

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') [$(basename ${0} .sh)]" "${1}" >> "${LOG_FILE}"
}

if [ -z "${radarr_eventtype}" ]; then
    radarr_eventtype="Test"
fi

# Check if Python script exists and is executable
# if [ ! -x "${PYTHON_ENTRY}" ]; then
#     log "Error: Python script '${PYTHON_ENTRY}' is not executable"
#     exit 1
# fi

args="${@}"
if [ -z "${radarr_eventtype}" ] 
then
    log "No radarr event type provided. Using \"Test\" as the default"
fi

log "Radarr \"${radarr_eventtype}\" triggered"
log "Running Python script with arguments: --callarr radarr ${args}"

python3 "${PYTHON_ENTRY}" "--callarr" "radarr" ${args}
exit 0
