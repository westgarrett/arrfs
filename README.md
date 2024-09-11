# Media Storage Distribution Project

## Overview
This project is designed to intelligently distribute media files across multiple drives or arrays of varying types and capacities. It functions as a pseudo-RAID system, using symlinks to evenly spread media content across storage locations. The project consists of a trigger shell script, a Python `main.py` entrypoint, and several subdirectories (e.g., `radarr/`, `sonarr/`) to process and manage media storage.

## Components

### 1. Shell Trigger Script
The trigger shell script initiates the process, calling the Python entrypoint (`main.py`). This script could be run periodically or based on file system events, depending on your setup.

### 2. `main.py` (Python Entrypoint)
The core logic of the project is implemented in the `main.py` script. This script handles the main workflow, including detecting new media files, determining how to distribute them, and creating the necessary symlinks to ensure even storage across multiple drives/arrays.

### 3. Subdirectories
- **`radarr/`**: Contains scripts and configurations specific to handling media processed by Radarr.
- **`sonarr/`**: Contains scripts and configurations specific to handling media processed by Sonarr.
- Additional subdirectories can be created for other media services, as needed.

## Features
- **Pseudo-RAID Distribution**: The system emulates RAID-like behavior by distributing media evenly across available storage, respecting drive capacities and types.
- **Symlink Management**: Media files are accessible via symlinks, ensuring logical consistency while physically distributing files across different drives.
- **Modular Support**: Easily expandable to support different media processing tools like Radarr, Sonarr, and more.

## Prerequisites
- Python 3.x
- Shell scripting environment
- [Optional] Radarr, Sonarr, or similar media management tools

## Usage

1. **Configure Storage Locations**: Update the configuration files in the appropriate subdirectories to specify the storage locations (drives/arrays) and capacities.
   
2. **Run the Shell Trigger Script**:
    ```bash
    ./trigger.sh
    ```

3. **Python Script Execution**:
   The shell script will automatically call `main.py`, which will then process and distribute the media files according to the configured rules.

## Roadmap
- Add support for more media services.
- Implement detailed logging for media processing.
- Expand symlink management to handle failures and retries.

## License
This project is open-source and licensed under the MIT License.
