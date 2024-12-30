import os
import time
from arrfs.main import read_config, DEFAULT_CONFIG_PATH

def casio():
    config_namespace = read_config(DEFAULT_CONFIG_PATH)
    radarr_import_path = config_namespace.radarr.import_path
    radarr_downloads_path = config_namespace.radarr.downloads_path
    sonarr_import_path = config_namespace.sonarr.import_path
    sonarr_downloads_path = config_namespace.sonarr.downloads_path

    while True:
        any_radarr_imports = os.listdir(radarr_import_path)
        any_sonarr_imports = os.listdir(sonarr_import_path)
        if any_radarr_imports:
            for directory in any_radarr_imports:
                directory_size = os.stat(directory).st_size
        elif any_sonarr_imports:
            for directory in any_sonarr_imports:
                directory_size = os.stat(directory).st_size
            
        # hard sleep for disk watching?
        time.sleep(5)


if __name__ == "__main__":
    casio()