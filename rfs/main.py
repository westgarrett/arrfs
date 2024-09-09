import click
import os
import shutil
import subprocess
import sys
from typing import List, Dict, Union
from rfs.radarr import radarr_cli

DB_DRIVE_PATH: str = "./db_drive"
TC_DRIVE_PATH: str = "./tc_drive"
STORAGE_DRIVE_PATH: List[str] = [
    "./storage0",
    "./storage1",
]


class ArrEvent:
    def __init__(
        self,
        callarr: str,
        debug: bool,
        db_drive_path: str = DB_DRIVE_PATH,
        tc_drive_path: str = TC_DRIVE_PATH,
        storage_drive_path: Union[List[str], str, None] = STORAGE_DRIVE_PATH,
    ):
        if os.path.exists(db_drive_path):
            self.db_drive_path = db_drive_path

        if os.path.exists(tc_drive_path):
            self.tc_drive_path = tc_drive_path

        self.storage_drive_path = []
        for path in storage_drive_path:
            if os.path.exists(path):
                self.storage_drive_path.append(path)

    def cli(self):
        if self.callarr == "radarr":
            radarr_cli()


# Event type passed from the trigger shell script
@click.group()
@click.option(
    "--callarr", default=None, help=f"The *arr invoking {os.path.basename(__file__)}"
)
@click.option("--debug/--no-debug", default=False)
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
def eventtype(ctx, callarr, debug, db_drive_path, tc_drive_path, storage_drive_path):
    if callarr is None:
        raise click.ClickException("Missing --callarr option")
    click.echo("here")
    print(**ctx.obj)
    ctx.obj = ArrEvent(
        callarr, debug, db_drive_path, tc_drive_path, storage_drive_path, **ctx.obj
    )


def create_symlink(db_path: str, true_path: str):
    pass


def get_drive_used_capacity(drive_uuid: str):
    pass


def compare_drive_capacity():
    pass


def main():
    # download disk -> generate symlink on jellyfin DBdrive / partition -> import to symlink path
    eventtype()


if __name__ == "__main__":
    eventtype(sys.argv)
