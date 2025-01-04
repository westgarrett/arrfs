radarr event triggers custom script
operation is already in-progress, so the only handling I can do is determining where the file will be going
    * make the import location that's given to radarr on the /operations disk or tmpfs
        * it will only move into that directory once the import is ready or manually approved
        * get the file path from the environment variable and watch for the file to be present on the temp disk
        * that operation is only a mv, just moving file pointers around

the entire trigger script framework may not be needed at all lol
I've already kind of scrapped it from the current execution by introducting an explicit config file
it's worth maintaining for some other use; notifications, analytics/dashboards


radarr import path is set to /operations/casio/radarr (or something more descriptive)
radarr downloads "some movie 2024" on /operations/downloads
once completed, radarr either prompts for manual imports or automatically processes and imports to /operations/casio/radarr
a daemon will be watching /operations/casio/radarr for these directories
    * this is where we could do any sort of post-processing and media analysis as well
when a directory is populated in /operations/casio/radarr, a script (maybe existing idk) would classify the media and system condition
    * disk capacity, free space, usage and calculation of most space efficient/speed/etc (would be auto-populated in a config file?)
    * there's a question of if spreading like series episodes across multiple disks with the same folder name is doable or not, need to test
        * os.walk over the directories and have the directory structure completely mirrored in symlinks
    * otherwise, media directory size would be evaluated and then be sent to a determined disk
    * a symlink would be simultaneously created with the same directory name and inserted into /arrfs/movies
        * will need to test hard links and balance the pros/cons
        * I have a feeling that hard links will cause more issues when deleting/updating files
        * the *arrs all warn that using symlinks isn't recommended and I've always been curious why
        * is there any reason that the symlink db generation can't be done after all of the media is spread across disks?
            * the only reason I can see this not working is if radarr needs the import_path == library_path
                * radarr wouldn't be able to maintain true function
            * each storage device listed in the config file would have a movies/shows/etc
            directory, and the media would be thrown into those files regardless
            * then the symlink db could be generated on-change in the daemon
            * that way if something is deleted from the disk the db can be rewritten instead of edited
    * I also want to find out if a jellyfin library scan on the symlink db would lower the disk read time. doubtful but test I guess
Race conditions
    * if there are multiple download clients, the disk utilization calculation would change dynamically
        * a singular download client wouldn't have this issue necessarily
        * if imported from the /operations/casio/* folders it could be a sequential operation, would just be slower
        * the disk usage information returned from the program would need to have any current write/delete operations accounted for
        * this means that the disk usage would have to be projected for each event
        * easy way: get each directory size in /operations/casio/movies and determine where it will go in a queue
            * this would allow for sequential writes
            * job A would be writing to disk 1 with size X
            * job B would be writing to disk 2 because the size of the file in job A transitioned the target disk after adding X to the map 