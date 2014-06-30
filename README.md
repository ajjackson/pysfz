pysfz
=====

A python library for interfacing with the SFZ sampler instrument format.

## Requirements and installation ##

Python 2.7.x is required. (Conversion to Python 3 should be trivial if needed.)
Add the top-level directory (the folder containing this file) to the
PYTHONPATH, e.g. from a bash shell:

	export PYTHONPATH="~/src/pysfz:$PYTHONPATH"

## SFZ format ##

The .sfz format is a convenient text format for sample-based virtual instrument patches. 
The actual samples are provided as relative paths in the .sfz instrument file. 
This permits multiple instruments to be efficiently defined from existing samples without 
creating redundant copies.

The format was developed by Cakewalk. Unfortunately they have
rearranged their website and the formal specification no longer exists
at http://www.cakewalk.com/DevXchange/sfz.asp, although the wonderful
[archive.org](https://archive.org) project has maintained copies of
this page. 
An informal but extensive description is also available at
http://drealm.info/sfz/plj-sfz.xhtml.

## Development notes ##

This project is just beginning! The immediate goals are:

* A python interface for importing, modifying and exporting the major
  features of SFZ sampler instrument files.
* A routine for generating random, pseudo-random and other algorithmic
  sampler instruments from a directory structure containing audio
  files.

From a development standpoint, this will involve creating:

* An "Instrument" class which contains sample regions with supported metadata
* A "read" routine which generates an Instrument from a valid .sfz file
* A "write" function/method which generates a valid .sfz file
* A number of example scripts and functions which do fun things

### Platform issues ###

SFZ is held up as a simple format, and has been keenly adopted by the
LinuxSampler project.
However, it was developed by Cakewalk, a Windows-focused developer,
and all the examples they provide use windows-style paths (i.e. with
backslashes).

The sole developer of this project is targeting plugins running in
WINE on a linux system; the Windows plugins are likely to prefer
backslashes, but local scripts are dealing with a unix-like file-system.
Any other users of this package are likely to be using a single
environment such as OSX, Linux with Linuxsampler or a regular Windows
setup.

Some flags will therefore be provided to switch between the formats.
Forward-slashes are to be preferred internally, and these will be
converted to/from backslashes as needed.
In the long run, it should be possible to detect the system type and
apply this automatically.

## Boring stuff ##

### Licence and attribution ###

This project has solely been developed (so far) by Adam J. Jackson. Contributions are welcome.
This project is licensed under the GPLv3; a license file should be included in this folder.

### Disclaimer ###

This project is not related to Cakewalk in any way. 
To the best of my knowledge the SFZ format is royalty-free and there are no SFZ-related restrictions on the use of this project.
