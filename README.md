# A file system for shallow pockets

## An \*arr-enabled media distribution project

## Overview
Intelligently distribute media files across multiple drives or arrays of varying types, capacities, and speeds. It functions as a distributed file system using symlinks to evenly store media content across multiple storage devices


## Features
- **Pseudo-RAID Distribution**: The system emulates RAID-like behavior by distributing media evenly across available storage, respecting drive capacities and types.
- **Symlink Management**: Media files are accessible via symlinks, ensuring logical consistency while physically distributing files across different drives.
- **Modular Support**: Easily expandable to support different media processing tools like Radarr, Sonarr, and more.


## Components

### 1. \*arr Trigger Script
A trigger shell script called on an \*arr event

### 2. Python Entrypoint
Handles the distribution of media based on storage device parameters

### 3. Docker build / deployment flow
Shell scripts to set up the Docker build environment and deploy custom images

## Prerequisites
- Python 3.x
- Docker

## Usage


## Roadmap
- Create arrfs configuration cli that allows storage assignment/management
- 
- Implement detailed logging for media processing.
- Expand symlink management to handle failures and retries.

## License
This project is open-source and licensed under the MIT License.
