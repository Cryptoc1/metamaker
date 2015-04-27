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

Note about platform support: MetaMaker was built with OS X in mind, and has only been tested on my Mac. Further platform testing isn't planned for future development.

## Video formats supported
- [x] mp4
- [ ] m4v
- [ ] avi
- [ ] mkv
~~- [ ] wmv~~

wmv support won't be included because most movies aren't distributed using wmv.

## Things to Watch-out For
* If any directories that you enter include unicode characters, the program will crash.

## Dependencies
* MP4Box

MP4Box can be installed with brew

	$ brew install mp4box

Note that *install.sh* installs mp4box for you.

#### Plain and Simple
