# USB organizer tool

Got a USB (or any other folder on your PC) that's a mess?
Let this USB organizer tool relieve you of your headache!

Just point the script at any directory and it will list the files and propose
a better directory structure. Just pass the `--apply` flag and it'll do the
work!

## Features
- categorizes files by extension
- dry-run mode by default
- `--apply` flag moves files
- creates category files automatically
- never deletes files

# Usage:

`python organizer.py /path/to/USB/stick [--apply]`

## Note:
This script runs in dry-run mode by default and will not modify files.