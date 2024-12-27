radarr event triggers custom script
operation is already in-progress, so the only handling I can do is determining where the file will be going
    * make the import location that's given to radarr on the /operations disk or tmpfs
        * it will only move into that directory once the import is ready or manually approved
        * get the file path from the environment variable and watch for the file to be present on the temp disk
        * that operation is only a mv, just moving file pointers around


radarr import path is set to /operations/casio/radarr (or something more descriptive)
radarr downloads "some movie 2024" on /operations/downloads
once completed, radarr either prompts for manual imports or automatically processes and imports to /operations/casio/radarr
a daemon will be watching /operations/casio/radarr for these directories
    * this is where we could do any sort of post-processing and media analysis as well
when a directory is populated in /operations/casio/radarr, a script (maybe existing idk) would classify the media and system condition
    * disk capacity, free space, usage and calculation of most space efficient/speed/etc (actually would be auto-populated in a config file)
    * there's a question of if spreading like series episodes across multiple disks with the same folder name is doable or not, need to test
    * otherwise, media directory size would be evaluated and then be sent to a determined disk
    * a symlink would be simultaneously created with the same directory name and inserted into /arrfs/movies
        * will need to test hard links and balance the pros/cons
        * I have a feeling that hard links will cause more issues when deleting/updating files
        * the *arrs all warn that using symlinks isn't recommended and I've always been curious why
    * I also want to find out if a jellyfin library scan on the symlink db would lower the disk read time. doubtful but test I guess