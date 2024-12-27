radarr event triggers custom script
operation is already in-progress, so the only handling I can do is determining where the file will be going
    * make the import location that's given to radarr on the /operations disk or tmpfs
        * it will only move into that directory once the import is ready or manually approved
        * get the file path from the environment variable and watch for the file to be present on the temp disk
        * that operation is only a mv, just moving file pointers around


radarr import path is set to /operations/rolex (or something more descriptive)
radarr downloads "some movie 2024" on /operations/downloads
once completed, radarr either prompts for manual imports or automatically imports to /operations/rolex
a daemon will be watching /operations/rolex for these directories
    * this is where we could do any sort of post-processing and media analysis as well