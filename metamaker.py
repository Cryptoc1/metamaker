#!/usr/bin/env python

import imdb
import os, sys

def main(id, dir):
    api = imdb.IMDb()

    if id == None:
        print "Enter the IMDb id"
        id = raw_input("> ")
    else:
        id = id
    if dir == None:
        print "Enter the filename (or path to)"
        dir = os.path.abspath(raw_input("> "))
    else:
        dir = os.path.abspath(dir)
        dir = dir.replace(" ", "\\ ")

    mov = api.search_movie(id)[0]
    api.update(mov)

    print "Downloading cover to ~/temp..."
    cov_url = mov['cover']
    os.system("wget -O ~/temp/" + id + ".jpg " + cov_url)
    cov_path = os.path.expanduser("~/temp/" + id + ".jpg")
   
    print "Writing data to file..."
    print dir
    os.system("MP4Box -itags cover=\"" + cov_path + "\":tool=\"metamaker\":genre=\"" + mov['genre'][0] + "\":writer=\"" + mov['writer'][0]['name'] + "\":name=\"" + mov['title'] + "\":created=\"" + str(mov['year']) + "\":encoder=\"MP4Box\" " + dir + "")

    print "Process complete, exiting."
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1], sys.argv[2])
    else:
        main(None, None)
