import sys
import click
import os
import shutil
import subprocess
from typing import Tuple, Dict, Union

from main import create_symlink, compare_drive_capacity, get_path_info

# Group 1: On Grab Event
@click.command()
@click.argument(
    "radarr_download_client",
    envvar="radarr_download_client",
    required=False,
    default=None,
)
@click.argument(
    "radarr_download_id",
    envvar="radarr_download_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_id",
    envvar="radarr_movie_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_imdbid",
    envvar="radarr_movie_imdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_in_cinemas_date",
    envvar="radarr_movie_in_cinemas_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_physical_release_date",
    envvar="radarr_movie_physical_release_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_title",
    envvar="radarr_movie_title",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_tmdbid",
    envvar="radarr_movie_tmdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_year",
    envvar="radarr_movie_year",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_indexer",
    envvar="radarr_release_indexer",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_quality",
    envvar="radarr_release_quality",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_qualityversion",
    envvar="radarr_release_qualityversion",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_releasegroup",
    envvar="radarr_release_releasegroup",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_size",
    envvar="radarr_release_size",
    required=False,
    default=None,
)
@click.argument(
    "radarr_release_title",
    envvar="radarr_release_title",
    required=False,
    default=None,
)
def grab(
    radarr_download_client,
    radarr_download_id,
    radarr_movie_id,
    radarr_movie_imdbid,
    radarr_movie_in_cinemas_date,
    radarr_movie_physical_release_date,
    radarr_movie_title,
    radarr_movie_tmdbid,
    radarr_movie_year,
    radarr_release_indexer,
    radarr_release_quality,
    radarr_release_qualityversion,
    radarr_release_releasegroup,
    radarr_release_size,
    radarr_release_title,
):
    print("grab command")
    print(
        radarr_download_client,
        radarr_download_id,
        radarr_movie_id,
        radarr_movie_imdbid,
        radarr_movie_in_cinemas_date,
        radarr_movie_physical_release_date,
        radarr_movie_title,
        radarr_movie_tmdbid,
        radarr_movie_year,
        radarr_release_indexer,
        radarr_release_quality,
        radarr_release_qualityversion,
        radarr_release_releasegroup,
        radarr_release_size,
        radarr_release_title,
    )


# Group 2: On Import/On Upgrade Event
@click.command()
@click.argument(
    "radarr_download_id",
    envvar="radarr_download_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_download_client",
    envvar="radarr_download_client",
    required=False,
    default=None,
)
@click.argument(
    "radarr_isupgrade",
    envvar="radarr_isupgrade",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_id",
    envvar="radarr_movie_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_imdbid",
    envvar="radarr_movie_imdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_in_cinemas_date",
    envvar="radarr_movie_in_cinemas_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_path",
    envvar="radarr_movie_path",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_physical_release_date",
    envvar="radarr_movie_physical_release_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_title",
    envvar="radarr_movie_title",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_tmdbid",
    envvar="radarr_movie_tmdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_year",
    envvar="radarr_movie_year",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_id",
    envvar="radarr_moviefile_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_relativepath",
    envvar="radarr_moviefile_relativepath",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_path",
    envvar="radarr_moviefile_path",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_quality",
    envvar="radarr_moviefile_quality",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_qualityversion",
    envvar="radarr_moviefile_qualityversion",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_releasegroup",
    envvar="radarr_moviefile_releasegroup",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_scenename",
    envvar="radarr_moviefile_scenename",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_sourcepath",
    envvar="radarr_moviefile_sourcepath",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_sourcefolder",
    envvar="radarr_moviefile_sourcefolder",
    required=False,
    default=None,
)
@click.argument(
    "radarr_deletedrelativepath",
    envvar="radarr_deletedrelativepath",
    required=False,
    default=None,
)
@click.argument(
    "radarr_deletedpaths",
    envvar="radarr_deletedpaths",
    required=False,
    default=None,
)
def download(
    radarr_download_id,
    radarr_download_client,
    radarr_isupgrade,
    radarr_movie_id,
    radarr_movie_imdbid,
    radarr_movie_in_cinemas_date,
    radarr_movie_path,
    radarr_movie_physical_release_date,
    radarr_movie_title,
    radarr_movie_tmdbid,
    radarr_movie_year,
    radarr_moviefile_id,
    radarr_moviefile_relativepath,
    radarr_moviefile_path,
    radarr_moviefile_quality,
    radarr_moviefile_qualityversion,
    radarr_moviefile_releasegroup,
    radarr_moviefile_scenename,
    radarr_moviefile_sourcepath,
    radarr_moviefile_sourcefolder,
    radarr_deletedrelativepath,
    radarr_deletedpaths,
):
    click.echo("download event")
    print(
        radarr_download_id,
        radarr_download_client,
        radarr_isupgrade,
        radarr_movie_id,
        radarr_movie_imdbid,
        radarr_movie_in_cinemas_date,
        radarr_movie_path,
        radarr_movie_physical_release_date,
        radarr_movie_title,
        radarr_movie_tmdbid,
        radarr_movie_year,
        radarr_moviefile_id,
        radarr_moviefile_relativepath,
        radarr_moviefile_path,
        radarr_moviefile_quality,
        radarr_moviefile_qualityversion,
        radarr_moviefile_releasegroup,
        radarr_moviefile_scenename,
        radarr_moviefile_sourcepath,
        radarr_moviefile_sourcefolder,
        radarr_deletedrelativepath,
        radarr_deletedpaths,
    )


# Group 3: On Rename Event
@click.command()
@click.argument(
    "radarr_movie_id",
    envvar="radarr_moviefile_id",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_title",
    envvar="radarr_movie_title",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_year",
    envvar="radarr_moviefile_year",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_path",
    envvar="radarr_movie_path",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_imdbid",
    envvar="radarr_movie_imdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_tmdbid",
    envvar="radarr_movie_tmdbid",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_in_cinemas_date",
    envvar="radarr_movie_in_cinemas_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_movie_physical_release_date",
    envvar="radarr_movie_physical_release_date",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_ids",
    envvar="radarr_moviefile_ids",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_relativepaths",
    envvar="radarr_moviefile_relativepaths",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_paths",
    envvar="radarr_moviefile_paths",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_previousrelativepaths",
    envvar="radarr_moviefile_previousrelativepaths",
    required=False,
    default=None,
)
@click.argument(
    "radarr_moviefile_previouspaths",
    envvar="radarr_moviefile_previouspaths",
    required=False,
    default=None,
)
def rename(
    radarr_movie_id,
    radarr_movie_title,
    radarr_movie_year,
    radarr_movie_path,
    radarr_movie_imdbid,
    radarr_movie_tmdbid,
    radarr_movie_in_cinemas_date,
    radarr_movie_physical_release_date,
    radarr_moviefile_ids,
    radarr_moviefile_relativepaths,
    radarr_moviefile_paths,
    radarr_moviefile_previousrelativepaths,
    radarr_moviefile_previouspaths,
):
    print("rename event")
    print(
        radarr_movie_id,
        radarr_movie_title,
        radarr_movie_year,
        radarr_movie_path,
        radarr_movie_imdbid,
        radarr_movie_tmdbid,
        radarr_movie_in_cinemas_date,
        radarr_movie_physical_release_date,
        radarr_moviefile_ids,
        radarr_moviefile_relativepaths,
        radarr_moviefile_relativepaths,
        radarr_moviefile_paths,
        radarr_moviefile_previousrelativepaths,
        radarr_moviefile_previouspaths,
    )


# Group 4: On Health Check Event
@click.command()
@click.argument(
    "radarr_health_issue_level",
    envvar="radarr_health_issue_level",
    required=False,
    default=None,
)
@click.argument(
    "radarr_health_issue_message",
    envvar="radarr_health_issue_message",
    required=False,
    default=None,
)
@click.argument(
    "radarr_health_issue_type",
    envvar="radarr_health_issue_type",
    required=False,
    default=None,
)
@click.argument(
    "radarr_health_issue_wiki",
    envvar="radarr_health_issue_wiki",
    required=False,
    default=None,
)
def healthissue(
    radarr_health_issue_level,
    radarr_health_issue_message,
    radarr_health_issue_type,
    radarr_health_issue_wiki,
):
    print(
        radarr_health_issue_level,
        radarr_health_issue_message,
        radarr_health_issue_type,
        radarr_health_issue_wiki,
    )
    click.echo("healthissue event")


# Group 5: On Application Update Event
@click.command()
@click.argument(
    "radarr_update_message",
    envvar="radarr_update_message",
    required=False,
    default=None,
)
@click.argument(
    "radarr_update_newversion",
    envvar="radarr_update_newversion",
    required=False,
    default=None,
)
@click.argument(
    "radarr_update_previousversion",
    envvar="radarr_update_previousversion",
    required=False,
    default=None,
)
def applicationupdate(
    radarr_update_message, radarr_update_newversion, radarr_update_previousversion
):
    if radarr_update_message is None:
        pass

    if radarr_update_newversion is None:
        pass

    if radarr_update_previousversion is None:
        pass

    print(
        radarr_update_message, radarr_update_newversion, radarr_update_previousversion
    )
    click.echo("applicationupdate event")
    # do stuff


# Group 6: On Test Event
def test():
    click.echo(f'Radarr "{get_radarr_eventtype()}" was successful')


def get_radarr_eventtype():
    return os.getenv("radarr_eventtype", default="Test")


def handle_event(db_drive_path: str, download_drive_path: str, storage_drive_path: str):
    sys.argv = [__repr__]
    radarr_eventtype = get_radarr_eventtype()
    event_types = [
        "Grab",
        "Rename",
        "Download",
        "HealthIssue",
        "ApplicationUpdate",
        "Test",
    ]
    if radarr_eventtype is None:
        raise ValueError(f"radarr_eventtype == {radarr_eventtype}")
    for _type in event_types:
        if radarr_eventtype == _type:
            getattr(sys.modules[__name__], _type.lower())()


__repr__: str = f"{__name__}.{get_radarr_eventtype().lower()}"

if __name__ == "__main__":
    # process the radarr_eventtype
    handle_event()
