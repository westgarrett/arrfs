import os
import shutil
import subprocess
from typing import List, Dict

DB_DRIVE: str = "~/rfs/db_drive"
STORAGE_DRIVES: Dict[str, str] = {
    "uuid0": "~/rfs/storage0",
    "uuid1": "~/rfs/storage1",
}

def create_symlink(db_path: str, true_path: str):
    pass

def get_drive_used_capacity(drive_uuid: str):
    pass

def compare_drive_capacity()

def main():
    # download disk -> generate symlink on jellyfin DBdrive / partition -> import to symlink path






    pass


if __name__ == "__main__":
    main()
