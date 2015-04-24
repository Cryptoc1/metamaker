# MetaMaker
MetaMaker is a simple pyhton utility I created to write metadata to movie file (mp4, ~~m4v, mkv, avi, wmv~~).

## How To Use
Begin by running install.sh

	$ ./install.sh

Using MetaMaker is quite simple really:

	$ metamaker <imdb-id> <path-to-file>

Or, you can use the interactive console by running:

	$ metamaker

## Things to Watch-out For
* If any directories that you enter include unicode characters, the program will crash.

## Dependencies
* MP4Box

MP4Box can be installed with brew

	$ brew install mp4box

Note that *install.sh* installs mp4box for you.

#### Plain and Simple
