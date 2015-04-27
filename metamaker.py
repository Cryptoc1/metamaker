#!/usr/bin/env python

import imdb
import os, sys, subprocess as sp

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
    wget = ['wget',
            '-O', '~/temp/' + id + '.jpg',
            cov_url]
    sp.Popen(wget, stdout = sp.PIPE).wait()
    # os.system("wget -O ~/temp/" + id + ".jpg " + cov_url)
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
    mp4box = ['MP4Box',
            '-itags', 'cover="' + cov_path + '":tool="metamaker":genre="' + mov['genre'][0] + '":writer="' + mov['writer'][0]['name'] + '":name="' + mov['title'] + '":created="' + str(mov['year']) + '":encoder="MP4Box" ' + dir + '']
    sp.Popen(mp4box,  stdout = sp.PIPE).wait()
    # os.system("MP4Box -itags cover=\"" + cov_path + "\":tool=\"metamaker\":genre=\"" + mov['genre'][0] + "\":writer=\"" + mov['writer'][0]['name'] + "\":name=\"" + mov['title'] + "\":created=\"" + str(mov['year']) + "\":encoder=\"MP4Box\" " + dir + "")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "--batch":
            if len(sys.argv) > 2:
                batch(sys.argv[2], False)
            else:
                batch(None, True)
        else:
            main(sys.argv[1], sys.argv[2])
    else:
        main(None, None)
