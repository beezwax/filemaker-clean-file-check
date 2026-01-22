# filemaker-clean-file-check
Check if a FileMaker .fmp12 file was closed cleanly by the server or client

---

### Usage

`python3 filemaker-clean-file-check.py /some/path/to/a.fmp12`

---

### What is this?

This tool checks for a byte flag found in .fmp12 files that indicates whether the FileMaker file at the given path was cleanly closed.

It does not in any way alter the data on the file, although meta data (that is not part of the file's data) about when the file was last accessed will be changed as a result.

### When To Use It?

If one or more of the considerations below is true then this tool may be helpful:

* working with very large files
* restoring from backups (especially if they are remote, tape based, etc.) that may require a lengthy delay to restore from
* in unusual circumnstances were you may be uncertainty about the current state of the files
* you don't want to possibly tie up the file with a lengthy consistency or recovery check
* FMS is hung, and you'd like to know if the database file was closed*

*On FileMaker Server, it is possible for a hosted file to of effectively been closed. For instance, if the database file was Paused in the admin console before the issue occured.

### What does it mean if it was cleanly closed?

* the file should be a complete and fully intact copy of the database file*
* the data in file includes all data changes up to the time the file was last closed

*This assumes there weren't any prior problems with the file.

### What if it wasn't cleanly closed?

For smaller files, and assuming recent backups of the needed vintage are available, the easiest, quickest, and safest path is to restore from the last good backup.

But to drill down on this, here are the possible scenarios:

* the file _may_ still be OK
* a fair chance of minor damage, which FMS or FMP can repair easily
* a significant chance some data or schema changes (using "schema" in broad sense) were lost
* a somewhat unlikely chance that the file is badly damaged

In this case there is nothing close to certainty about the state of the file. At the least, some data may of been added, updated, or deleted that is not part of the file you are evaluating.

FileMaker Server's Persistent Cache settings can greatly reduce the likelyhood of losing any data, and can restore the file's data to something either at, or very close to, the time of the incident. It does this by utilizing data that was written out to cache files, similar to a transaction log, to restore any recent changes. The main catch, at least for very large files: the only way to utilize this is to allow FMS to re-open the file, perform a lengthy consistency check, and then attempt to re-consolidate the files.

If using FMP, or FMS is not using Persistent Cache, or the cache is unusable for some reason, you have an increased likelyhood of ending up with a more seriously damaged file. In regards to lost data however there is one thing to check for in the Event.log. If you see a message like the one below the Persistent Cache could be missing a significant number of changes:

`The transaction originating from user[user-name-here] session[session-name] machine[your.host.name] to file[your-filename.fmp12] was not committed before the server terminated abnormally.`

---

### Related

If you found this useful, you might also be interested in the fmslog utility at https://github.com/beezwax/fmslog
