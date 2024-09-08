#!/bin/bash
LOG_FILE="logs/$(basename "${0}" .sh).log"
PYTHON_ENTRY="main.py"
radarr_eventtype="Test"

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')" >> "${LOG_FILE}"
}

case "${radarr_eventtype}" in
    Grab)
        break ;;
    Download)
        break ;;
    Rename)
        break ;;
    HealthIssue)
        break ;;
    ApplicationUpdate)
        break ;;
    Test)
        break ;;
    *)
        log "Unknown event type: ${radarr_eventtype}"
        exit 1 ;;
esac

log "${radarr_eventtype} triggered"
python3 "${PYTHON_ENTRY}" "${radarr_eventtype}"
exit 0
