import click
import os
import shutil
import subprocess
from typing import Tuple, Dict, Union

DB_DRIVE_PATH: str = "./db_drive"
TC_DRIVE_PATH: str = "./tc_drive"
STORAGE_DRIVE_PATH: Tuple[str, ...] = (
    "./storage0",
    "./storage1",
)

# Group 1: On Grab Event
@click.group()
@click.option(
    "--radarr_download_client",
    envvar="radarr_download_client",
    default=None,
    help="Download client (empty if unknown)",
)
@click.option(
    "--radarr_download_id",
    envvar="radarr_download_id",
    default=None,
    help="Hash of the torrent/NZB file",
)
@click.option(
    "--radarr_movie_id",
    envvar="radarr_movie_id",
    default=None,
    help="Internal ID of the movie",
)
@click.option(
    "--radarr_movie_imdbid",
    envvar="radarr_movie_imdbid",
    default=None,
    help="IMDb ID for the movie (empty if unknown)",
)
@click.option(
    "--radarr_movie_in_cinemas_date",
    envvar="radarr_movie_in_cinemas_date",
    default=None,
    help="Cinema release date (empty if unknown)",
)
@click.option(
    "--radarr_movie_physical_release_date",
    envvar="radarr_movie_physical_release_date",
    default=None,
    help="Physical release date (empty if unknown)",
)
@click.option(
    "--radarr_movie_title",
    envvar="radarr_movie_title",
    default=None,
    help="Title of the movie",
)
@click.option(
    "--radarr_movie_tmdbid",
    envvar="radarr_movie_tmdbid",
    default=None,
    help="TMDb ID for the movie",
)
@click.option(
    "--radarr_movie_year",
    envvar="radarr_movie_year",
    default=None,
    help="Release year of the movie",
)
@click.option(
    "--radarr_release_indexer",
    envvar="radarr_release_indexer",
    default=None,
    help="Indexer from which the release was grabbed",
)
@click.option(
    "--radarr_release_quality",
    envvar="radarr_release_quality",
    default=None,
    help="Quality name of the release, as detected by Radarr",
)
@click.option(
    "--radarr_release_qualityversion",
    envvar="radarr_release_qualityversion",
    default=None,
    help="Quality version of the release",
)
@click.option(
    "--radarr_release_releasegroup",
    envvar="radarr_release_releasegroup",
    default=None,
    help="Release group (empty if unknown)",
)
@click.option(
    "--radarr_release_size",
    envvar="radarr_release_size",
    default=None,
    help="Size of the release",
)
@click.option(
    "--radarr_release_title",
    envvar="radarr_release_title",
    default=None,
    help="Torrent/NZB title",
)
@click.pass_context
def grab(ctx):
    ctx.ensure_object(dict)
    # do stuff


# Group 2: On Import/On Upgrade Event
@click.group()
@click.option(
    "--radarr_isupgrade",
    envvar="radarr_isupgrade",
    default=None,
    help="True if an existing file is upgraded, False otherwise",
)
@click.option(
    "--radarr_movie_path",
    envvar="radarr_movie_path",
    default=None,
    help="Full path to the movie",
)
@click.option(
    "--radarr_moviefile_id",
    envvar="radarr_moviefile_id",
    default=None,
    help="Internal ID of the movie file",
)
@click.option(
    "--radarr_moviefile_relativepath",
    envvar="radarr_moviefile_relativepath",
    default=None,
    help="Path to the movie file, relative to the movie path",
)
@click.option(
    "--radarr_moviefile_path",
    envvar="radarr_moviefile_path",
    default=None,
    help="Full path to the movie file",
)
@click.option(
    "--radarr_moviefile_quality",
    envvar="radarr_moviefile_quality",
    default=None,
    help="Quality name of the movie file",
)
@click.option(
    "--radarr_moviefile_qualityversion",
    envvar="radarr_moviefile_qualityversion",
    default=None,
    help="Quality version of the movie file",
)
@click.option(
    "--radarr_moviefile_releasegroup",
    envvar="radarr_moviefile_releasegroup",
    default=None,
    help="Release group of the movie file",
)
@click.option(
    "--radarr_moviefile_scenename",
    envvar="radarr_moviefile_scenename",
    default=None,
    help="Original release name",
)
@click.option(
    "--radarr_moviefile_sourcepath",
    envvar="radarr_moviefile_sourcepath",
    default=None,
    help="Full path to the imported movie file",
)
@click.option(
    "--radarr_moviefile_sourcefolder",
    envvar="radarr_moviefile_sourcefolder",
    default=None,
    help="Full path to the folder the movie file was imported from",
)
@click.option(
    "--radarr_deletedrelativepaths",
    envvar="radarr_deletedrelativepaths",
    default=None,
    help="|-delimited list of files that were deleted to import this file",
)
@click.option(
    "--radarr_deletedpaths",
    envvar="radarr_deletedpaths",
    default=None,
    help="|-delimited list of full paths to files that were deleted",
)
@click.pass_context
def download(ctx):
    ctx.ensure_object(dict)
    # do stuff


# Group 3: On Rename Event
@click.group()
@click.option(
    "--radarr_moviefile_ids",
    envvar="radarr_moviefile_ids",
    default=None,
    help=",-delimited list of file IDs",
)
@click.option(
    "--radarr_moviefile_relativepaths",
    envvar="radarr_moviefile_relativepaths",
    default=None,
    help="|-delimited list of relative paths",
)
@click.option(
    "--radarr_moviefile_paths",
    envvar="radarr_moviefile_paths",
    default=None,
    help="|-delimited list of full paths",
)
@click.option(
    "--radarr_moviefile_previousrelativepaths",
    envvar="radarr_moviefile_previousrelativepaths",
    default=None,
    help="|-delimited list of previous relative paths",
)
@click.option(
    "--radarr_moviefile_previouspaths",
    envvar="radarr_moviefile_previouspaths",
    default=None,
    help="|-delimited list of previous paths",
)
@click.pass_context
def rename(ctx):
    ctx.ensure_object(dict)
    # do stuff


# Group 4: On Health Check Event
@click.group()
@click.option(
    "--radarr_health_issue_level",
    envvar="radarr_health_issue_level",
    default=None,
    help="Type of health issue (Ok, Notice, Warning, or Error)",
)
@click.option(
    "--radarr_health_issue_message",
    envvar="radarr_health_issue_message",
    default=None,
    help="Message from the health issue",
)
@click.option(
    "--radarr_health_issue_type",
    envvar="radarr_health_issue_type",
    default=None,
    help="Area that triggered the health issue",
)
@click.option(
    "--radarr_health_issue_wiki",
    envvar="radarr_health_issue_wiki",
    default=None,
    help="Wiki URL for more details",
)
@click.pass_context
def health(ctx):
    ctx.ensure_object(dict)


# Group 5: On Application Update Event
@click.group()
@click.option(
    "--radarr_update_message",
    envvar="radarr_update_message",
    default=None,
    help="Message from Radarr update",
)
@click.option(
    "--radarr_update_newversion",
    envvar="radarr_update_newversion",
    default=None,
    help="New version Radarr updated to",
)
@click.option(
    "--radarr_update_previousversion",
    envvar="radarr_update_previousversion",
    default=None,
    help="Previous version Radarr updated from",
)
def update(ctx):
    ctx.ensure_object(dict)
    # do stuff


# Group 6: On Test Event
@click.pass_context
def test(ctx):
    ctx.ensure_object(dict)
    click.echo(f"Radarr \"{get_radarr_eventtype()}\" was successful")

def get_radarr_eventtype():
    return os.getenv("radarr_eventtype", "Test")

def handle_event(db_drive_path, tc_drive_path, storage_drive_path):
    radarr_eventtype = get_radarr_eventtype()
    event_types = ["Grab", "Rename", "Download", "HealthIssue", "ApplicationUpdate", "Test"]
    if radarr_eventtype is None:
        raise ValueError(f"radarr_eventtype == {radarr_eventtype}")
    for _type in event_types:
        if radarr_eventtype == _type:
            eval(f"{_type.lower()}()")


if __name__ == "__main__":
    # process the radarr_eventtype
    handle_event()
