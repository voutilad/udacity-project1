#!/usr/bin/python
import media, omdb
import fresh_tomatoes
import urllib, json

"""
Builds the "entertainment center" representing the Fresh Tomatoes website.
"""

movies = []
favorites = [
             ('mad max: fury road', 'https://www.youtube.com/watch?v=hEJnMQG9ev8'),
             ('the final sacrifice', None),
             ('surf nazis must die', 'https://www.youtube.com/watch?v=Q8LV1S2q2GA'),
             ('bananaland', 'https://www.youtube.com/watch?v=8tch4JJKcMA')
            ]

print 'Assembling movie data...'

for favorite in favorites:
    print ' Fetching metadata for ' + favorite[0] + '...'

    title = favorite[0]
    trailer = favorite[1]

    imdb_movie = omdb.search(title)
    if imdb_movie['Poster'] == 'N/A':
        imdb_movie['Poster'] = None

    if imdb_movie is not None:
        movies.append(media.Movie(
                                    title=imdb_movie['Title'],
                                    trailer_youtube_url=trailer,
                                    poster_image_url=imdb_movie['Poster']))


print 'Movies list built:\n' + str(movies)

print 'Generating movies page and launching browser...'
fresh_tomatoes.open_movies_page(movies)
