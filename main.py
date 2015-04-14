#!/usr/bin/env python

import imdb

api = imdb.IMDb()

mov = api.search_movie('tt0470752')[0]
api.update(mov)

# Prints info about Ex Machina
print mov['runtime'][0], mov['rating'], mov['director'][0]
