#!/usr/bin/env python

import imdb
import re, os, sys

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
        dir = dir.replace(" ", "\\ ").replace("\n", "")

    if re.search('(\.mkv)|(\.avi)', dir):
        print  "[!] It looks like you aren't inputting a mp4 or m4v. In order to avoid corruption to the file, tags can't be written to the submitted file type."
        print "[!] Would you like metamaker to convert the file and write the tags? (y/n)"
        prompt = raw_input("> ").lower()
        if prompt == "y":
            dir = convert(dir)
        else:
            print "Okay, exiting..."
            sys.exit()

    mov = api.search_movie(id)[0]
    api.update(mov)

    print "Downloading cover to ~/temp..."
    cov_url = str(mov['cover'])
    dl_path = os.path.expanduser("~/temp/" + id + ".jpg")
    os.system("wget -O " + dl_path + " " + cov_url)

    cov_path = os.path.expanduser("~/temp/" + id + ".jpg")

    write_data(cov_path, mov, dir)

    print "Writing complete"

def batch(b_file, interactive):
    if interactive:
        print "Please enter path to the batch file"
        b_file = raw_input("> ")
    b_file = os.path.abspath(b_file)
    bf = open(b_file)
    for l in bf.readlines():
        l = l.split(':')
        main(l[0], l[1])
    bf.close()

def write_data(cov_path, mov, dir):
    print "Writing data to file..."
    mp4box = "MP4Box -itags cover=\"" + cov_path + "\":tool=\"metamaker\":genre=\"" + mov['genre'][0] + "\":writer=\"" + mov['writer'][0]['name'] + "\":name=\"" + mov['title'] + "\":created=\"" + str(mov['year']) + "\":encoder=\"MP4Box\" " + dir + ""
    os.system(mp4box)

def convert(dir):
    n_dir = re.sub('(\.mkv)|(\.avi)', '.mp4', dir).replace("\n", "")
    print "Starting ffmpeg. How long this will take, and the quality of the conversion is dependant upon your system."
    os.system("ffmpeg -i " + dir + " -vcodec copy -acodec copy " + n_dir)
    print "[+] Conversion complete, returning to write tags"
    return n_dir

def print_usage():
    print "metamaker: A tagging tool created by Samuel Steele (c) 2015."
    print "usage:"
    print "\t metamaker <imdb-id> <path-to-file>"
    print "options:"
    print "\t [--batch | -b] <path-to-batch-file> : Enable batch processing. (See http://github.com/cryptoc1/metamakerblob/master/BATCH.md)"
    print "\t [--help | -h] : Print this usage info."
    print ""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print_usage()
            sys.exit()
        if sys.argv[1] == "--batch" or sys.argv[1] == "-b":
            if len(sys.argv) > 2:
                batch(sys.argv[2], False)
            else:
                batch(None, True)
        else:
            main(sys.argv[1], sys.argv[2])
    else:
        main(None, None)
