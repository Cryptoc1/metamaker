# Batch processing with MetaMaker
A useful feature I've integrated into MetaMaker is *batch processing*. To use batch processing, simply use the *--batch* argument.

	$ metamker --batch <batch-file>

Where *batch-file* is a plain-text file that uses a "imdb-id:path-to-file" format. Example (example.batch):

	tt1549572:Another Earth/Another Earth.mp4
	tt1758692:Like Crazy/Like Crazy.mp4
	tt0088847:The Breakfast Club/The Breakfast Club.mp4

If *batch-file* isn't supplied, you will be dropped into an interactive console. 

## How to Create Batch Files
The batch files are simply plain-text files with a bit of basic formatting. The most effiecient way I use to create batch files is utilizing unix commands.

Within my computer, I store my movies in a folder suitabley named *Movies*. To begin, I enter this directory and run the following command.

	$ ls */*.mp4 >> metamaker.batch

This will enter all the mp4s into seperate lines in plain-text. From there all I have to do is enter the IMDb id for the movie followed by a colon before the path to each movie. (See example.batch for more info)
