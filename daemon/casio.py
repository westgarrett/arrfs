import os
import shutil
import time
from collections import namedtuple
from typing import List
from arrfs.main import read_config, DEFAULT_CONFIG_PATH


class StorageDecision:
    def __init__(self):
        pass



def create_symlink(db_path: str, true_path: str):
    """Create a symbolic link to the true path."""
    if os.path.exists(db_path):
        os.remove(db_path)
        os.symlink(true_path, db_path)
    else:
        os.symlink(true_path, db_path)
    return db_path


def get_path_info(path: str) -> namedtuple | None:
    """Read the total, used and free capacities of a path to an immutable class"""
    path = None
    if os.path.exists(path_info):
        path_info = shutil.disk_usage(path)
    else:
        print(f"drive at {path} does not exist")

    return path_info if path_info else None


def compare_storage_devices(devices: List[str], criteria: List[StorageDecision]=[]) -> str:
    """Compare the qualities of the configured drives"""
    """TODO figure out a way to customize file organization criteria, % used, speed, etc"""
    return devices[0] if devices else "-1"

def casio():
    config_namespace = read_config(DEFAULT_CONFIG_PATH)
    arrfs_db_path = config_namespace.arrfs.root_path
    radarr_import_path = config_namespace.radarr.import_path
    # radarr_downloads_path = config_namespace.radarr.downloads_path
    sonarr_import_path = config_namespace.sonarr.import_path
    # sonarr_downloads_path = config_namespace.sonarr.downloads_path
    storage_device_paths = config_namespace.storage
    

    while True:
        any_radarr_imports = os.listdir(radarr_import_path)
        any_sonarr_imports = os.listdir(sonarr_import_path)
        if any_radarr_imports or any_sonarr_imports:
            # get storage path info
            storage_path_info_list = [get_path_info(p) for p in storage_device_paths]
            target_storage_path = compare_storage_devices(storage_path_info_list)


        if any_radarr_imports:
            for directory in any_radarr_imports:
                directory_size = os.stat(directory).st_size
                shutil.move(src=radarr_import_path, dst=target_storage_path)

        if any_sonarr_imports:
            for directory in any_sonarr_imports:
                directory_size = os.stat(directory).st_size
            
        # hard sleep for disk watching?
        time.sleep(5)


if __name__ == "__main__":
    casio()