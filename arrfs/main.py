import click
import os
import shutil
import subprocess
import sys
import pathlib
import pprint
import tomli
from collections import namedtuple
from typing import Tuple, List, Dict, Union
import radarr.radarr_cli as radarr_cli
import sonarr.sonarr_cli as sonarr_cli

CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "config", "config.toml"
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
    "--arrfs_path",
    default=None,
    help=f"Database path",
)
@click.option(
    "--download_drive_path",
    default=None,
    help=f"Download drive path",
)
@click.option(
    "--storage_drive_path",
    default=None,
    multiple=True,
    help=f"Storage drive path(s) to bundle together",
)
@click.option("--config_path", default=None, help="Path to config.toml")
@click.pass_context
def eventtype(
    ctx,
    callarr,
    debug,
    arrfs_path: str,
    download_drive_path: str,
    storage_drive_path: List[str],
    config_path: str,
):
    """Event type passed from the trigger shell script"""
    config_namespace = read_config(
        config_path if config_path is not None else CONFIG_PATH
    )
    print(f"Loading {config_namespace.title}")

    # symlink db path
    arrfs_path = (
        arrfs_path if arrfs_path is not None else config_namespace.arrfs.root_path
    )
    assert arrfs_path is not None

    # *arr configs
    callarr_namespace = config_namespace.__getattribute__(callarr)
    download_drive_path = (
        download_drive_path
        if download_drive_path is not None
        else callarr_namespace.downloads_path
    )
    assert download_drive_path is not None

    storage_drive_path = [
        path
        for path in (
            storage_drive_path
            if storage_drive_path is not None
            else [v for _, v in config_namespace.storage]
        )
    ]
    assert storage_drive_path is not None

    if callarr == "radarr":
        radarr_cli.handle_event(arrfs_path, download_drive_path, storage_drive_path)
    elif callarr == "sonarr":
        sonarr_cli.handle_event(arrfs_path, download_drive_path, storage_drive_path)
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


def get_path_info(path: str) -> namedtuple | None:
    """Get the total, used and free capacities of a path"""
    path = None
    if os.path.exists(path_info):
        path_info = shutil.disk_usage(path)
    else:
        print(f"drive at {path} does not exist")

    return path_info if path_info else None


def compare_drive_capacity():
    """Compare the capacity of the configured drives."""
    pass


def read_config(config_path: str) -> namedtuple:
    """Read config values from config.toml"""
    with open(config_path, "rb") as config_file:
        config_dict = tomli.load(config_file)
    config_class = namedtuple("ArrfsConfig", config_dict.keys())
    config_obj = config_class(**config_dict)
    return config_obj


if __name__ == "__main__":
    config_namespace = read_config(CONFIG_PATH)
    eventtype()
