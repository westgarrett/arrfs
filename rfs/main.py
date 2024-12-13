import click
import os
import shutil
import subprocess
import sys
import pathlib
from typing import Tuple, List, Dict, Union
import radarr.radarr_cli as radarr_cli
import sonarr.sonarr_cli as sonarr_cli

DB_DRIVE_PATH: str = "./db_drive"
TC_DRIVE_PATH: str = "./tc_drive"
STORAGE_DRIVE_PATH: Tuple[str, ...] = (
    "./storage0",
    "./storage1",
)

# Event type passed from the trigger shell script
@click.command()
@click.option(
    "--callarr",
    default=None,
    help=f"The *arr invoking {os.path.basename(__file__)}",
    required=True,
)
@click.option("--debug/--no-debug", is_flag=True, default=False, help="Debug mode")
@click.option(
    "--db_drive_path",
    default=None,
    help=f"Database drive path, overrides {DB_DRIVE_PATH}",
)
@click.option(
    "--tc_drive_path",
    default=None,
    help=f"Torrent client drive path, overrides {TC_DRIVE_PATH}",
)
@click.option(
    "--storage_drive_path",
    default=None,
    multiple=True,
    help=f"Storage drives to bundle together, ex. {STORAGE_DRIVE_PATH}",
)
@click.pass_context
def eventtype(
    ctx,
    callarr,
    debug,
    db_drive_path: str,
    tc_drive_path: str,
    storage_drive_path: List[str],
):
    """Event type passed from the trigger shell script"""
    if callarr == "radarr":
        radarr_cli.handle_event(db_drive_path, tc_drive_path, storage_drive_path)
    elif callarr == "sonarr":
        sonarr_cli.handle_event(db_drive_path, tc_drive_path, storage_drive_path)
    else:
        raise ValueError(f"Unsupported callarr value: {callarr}")


def create_symlink(db_path: str, true_path: str):
    """Create a symbolic link to the true path."""
    if os.path.exists(db_path):
        os.remove(db_path)
        os.symlink(true_path, db_path)
    else:
        os.symlink(true_path, db_path)
    return db_path


# def get_drive_used_capacity(drive_uuid: str):
def get_directory_size(drive_path: str):
    """Get the used capacity of a drive."""
    # for now I'm going to use the size of the storage directory to simulate function
    root_dir = pathlib.Path(drive_path)
    for _file in root_dir.glob("**/*"):
        if _file.is_file():
            total_size += _file.stat().st_size


def compare_drive_capacity():
    """Compare the capacity of the drives."""
    pass


if __name__ == "__main__":
    eventtype()
