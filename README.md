# filemaker-clean-file-check
Check if a FileMaker .fmp12 file was closed cleanly by the server or client

---

### Usage

`python3 filemaker-clean-file-check.py /some/path/to/a.fmp12`

---

### What is this?

This tool checks for a byte flag found in .fmp12 files that indicates whether the FileMaker file at the given path was cleanly closed.

It does not in any way alter the data on the file, although some meta (that is not in the file) about when the file was last accessed may be changed as a result.

### When To Use It?

If working with larger files, restoring from backups (especially if they are remote, tape based, etc.) may require a fair amount of time. Or, due to unusual circumnstances, there may uncertainty about the current state of the files, but you don't want to possibly tie up the file with a lengthy consistency or recovery check. This tool can help you determine if the local files were safely & correctly closed.

### What does it mean if it was cleanly closed?

This means the file should be a complete and fully intact copy of the database file at the time it was last written to. This of course assumes there weren't any prior problems with the file.

### What if it wasn't cleanly closed?

This does not necessarily mean the previously hosted/open file is bad. But, at the very least, some data may of been added, updated, or deleted, that is not part of the file. FileMaker Server's Persistent Cache settings can greatly reduce the likelyhood of this problem, and can restore the file to its at, or very close to, the time of the incident. It can do this by utilizing data that was written out to cache files, similar to a transaction log, to restore any recent changes.

On FileMaker Server, this will mean that FMS will perform always perform a consistency check before opening the file.

If not using FMS, or FMS is not using Persistent Cache, or the cache is not usable for some reason, there is a significant chance of at least minor damage. 

### More Background

Typically you'd be interested in this if your server or client had became unstable, had a power outage, disk became too full, etc.
In these cases there may be uncertainty as to whether the previously files were open (hosted) at the time of the incident, and whether they are safe to use.

For smaller files, and assuming recent backups of the needed vintage are available, the easiest, quickest, and safest path is to restore from the last good backup.

But other less common situations may occur where there is reason to think the current files were not damaged by the event, or extra measures are needed. In these cases, it may be safe to
proceed with the previously opened/hosted files.
Generally, if a file is open and in use, there will be unsaved data (record commits, etc.) that is still in memory or has not been written out to the .fmp12 file yet.

Other actions, such as pausing the database file, or a scheduled backup having recently completed, may force any unsaved data to be consolidated into the main file.
