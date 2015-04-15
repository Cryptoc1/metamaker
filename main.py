#!/usr/bin/env python

import imdb
import os, sys, time

api = imdb.IMDb()

print "Enter the IMDb id"
mov = api.search_movie(raw_input("> "))[0]
api.update(mov)

# Prints info about Ex Machina
print mov['plot']
