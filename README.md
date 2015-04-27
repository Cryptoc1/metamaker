# MetaMaker
MetaMaker is a simple pyhton utility I created to write metadata to movie file. By default, MetaMaker writes all metadata that MP4Box supports that can be retreived from IMDb.

## How To Use
Begin by running install.sh

	$ ./install.sh

To skip checking if brew is installed:

	$ ./install.sh --without-brew-check

Using MetaMaker is quite simple really:

	$ metamaker <imdb-id> <path-to-file>

Or, you can use the interactive console by running:

	$ metamaker

A feature that I'm quite proud of in MetaMaker, is batch processing:

	$ metamaker --batch <batch-file>

More information about how to use batch processing can be found in *BATCH.md*

Note about platform support: MetaMaker was built with OS X in mind, and has only been tested on my Mac. Further platform testing isn't planned for future development.

## Video formats supported
- [x] mp4
- [x] m4v
- [x] avi<sup>\*</sup>
- [x] mkv<sup>\*</sup>

<sup>\*</sup> Writing tags to avi and mkv files only works after they've been converted to mp4 (using ffmpeg).

## Things to Watch-out For
* If any directories that you enter include unicode characters, the program will crash.

## Dependencies
* MP4Box
* ffmpeg

MP4Box can be installed with brew:

	$ brew install mp4box

ffmpeg can also be installed using brew:

	$ brew install ffmpeg

Note that *install.sh* installs dependencies for you (unless you supply *--without-brew-check*).

#### Plain and Simple
