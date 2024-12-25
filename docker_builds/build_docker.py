import click
import datetime
import os
import shutil
import subprocess
from typing import List


@click.command()
@click.option(
    "--service", default=None, help="Specify the service to build", required=True
)
@click.option("--config_path", default=os.path.join(os.path.basename(__file__), "config", "config.toml"), help="Specify the config.toml path")
@click.option(
    "--docker_dir",
    default=None,
    help="Docker image download + build directory",
)
@click.option("--port", default="7878", help="Port service points to")
@click.option("--downloads_path", default=os.path.join(os.path.basename(__file__), "downloads"), help="Specify the downloads path")
@click.option(
    "--arrfs_path",
    default=None,
    help="Path to arrfs",
)
@click.pass_context
def build_docker_image(
    ctx,
    service: str,
    config_path: str,
    docker_dir: str,
    downloads_path: str,
    port: str,
    arrfs_path: List[str],
):
    print(ctx)
    os.path.join(os.path.basename(__file__), f"docker-{service}"),
    image_tag = f"{datetime.datetime.now():%d.%m.%y.%H.%m.%s}"
    if docker_dir is not None and not os.path.exists(docker_dir):
        os.makedirs(docker_dir)
    subprocess.run(
        f"sudo docker build --no-cache --pull -t lscr.io/linuxserver/{service}:{image_tag} {docker_dir}",
        shell=True,
    )
    shutil.rmtree(docker_dir)
    compose = f"""
services:
  {service}:
    image: lscr.io/linuxserver/{service}:{image_tag}
    container_name: {service}
    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Etc/UTC
    volumes:
      - {config_path}:/config
      - {downloads_path}:/downloads
      - {arrfs_path}:/{'movies' if service == 'radarr' else 'shows'}
    ports:
      - {port}:{port}
    restart: unless-stopped
"""
    with open(os.path.join(docker_dir, "docker-compose.yml")) as f:
        f.write(compose)


if __name__ == "__main__":
    build_docker_image()
