# filemaker-clean-file-check
Check if a FileMaker .fmp12 file was closed cleanly by the server or client

---

### What Is This?

This tool checks if the FileMaker database file at the given path was cleanly closed.

### When To Use It?

If working with larger files, restoring from backups (especially if they are remote, tape based, etc.) may require a fair amount of time. Or, due to unusual circumnstances, there may uncertainty about the current state of the files, but you don't want to tie up the files with a lengthy consistency or recovery check. This tool may help you to determine that the files were safely & correctly closed.

### More Background

Typically you'd be interested in this if your server or client had became unstable, had a power outage, disk became too full, etc.
In these cases there may be uncertainty as to whether the previously files were open (hosted), and safe to use.

For smaller files, and assuming recent backups are avilable, the easiest, quickest, and safest path is to restore from the last good backup.

But other less common situations may occur where there is reason to think the current files were not damaged, 
Generally, if a file is open and in use, there will be unsaved data (record commits, etc.) that is still in memory or has not been written out to the .fmp12 file yet.

Other actions, such as pausing the database file, or a scheduled backup having recently completed, may force any unsaved data to be consolidated into the main file.
