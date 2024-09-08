#!/bin/bash
LOG_FILE="logs/$(basename "${0}" .sh).log"

function log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S')" >> "${LOG_FILE}"
}

case "${radarr_eventtype}" in
    Grab)
        log "Grab"
        echo ;;
    Download)
        log "Download"
        echo ;;
    Rename)
        log "Rename"
        echo ;;
    HealthIssue)
        log "HealthIssue"
        echo ;;
    ApplicationUpdate)
        log "ApplicationUpdate"
        echo ;;
    Test)
        log "Test"
        python3 test.py
        echo ;;
    
esac

log "${radarr_eventtype} triggered"

exit 0
