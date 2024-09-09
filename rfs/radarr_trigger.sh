#!/bin/bash
ROOT_DIR="~/rfs"
LOG_FILE="${ROOT_DIR}/rfs/logs/$(basename "${0}" .sh).log"
PYTHON_ENTRY="${ROOT_DIR}/rfs/main.py"
radarr_eventtype="Test"
set -e

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')" >> "${LOG_FILE}"
}

# Define an array of valid event types
valid_event_types=("Grab" "Download" "Rename" "HealthIssue" "ApplicationUpdate" "Test")

# Check if event type is valid
if [[ ! " ${valid_event_types[@]} " =~ " ${1} " ]]; then
    log "Unknown event type: ${1}"
    exit 1
fi

# Check if Python script exists and is executable
if [ ! -x "${PYTHON_ENTRY}" ]; then
    log "Error: Python script '${PYTHON_ENTRY}' is not executable"
    exit 1
fi

log "${radarr_eventtype} triggered"
log "Running Python script with arguments: ${@}"

python3 "${PYTHON_ENTRY}" "radarr" "${@}"
exit 0
