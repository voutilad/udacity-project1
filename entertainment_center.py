#!/usr/bin/python
import media
import fresh_tomatoes
import urllib, json

imdb_url = 'http://www.omdbapi.com/?y=&plot=short&r=json&'
trailer_addict_url = 'http://api.traileraddict.com/?imdb=1403865&count=4&width=680'
default_trailer = 'https://www.youtube.com/watch?v=5uZr3JWYdy8'


def build_url(movie_title):
    """
    Builds the OMDb API url <http://www.omdbapi.com> that looks up a title and returns JSON.
    Args:
        movie_title: string of a movie title to search for

    Returns:
        a url as a string representing a GETable OMDb title lookup
    """
    return imdb_url + urllib.urlencode({'t': movie_title})

def get_imdb_movie(movie_url):
    """
    Fetches a title from OMDb using their public API.

    Args:
        movie_url: string url representing a particular movie search

    Returns:
        a python dict object with the OMDb metadata

    """
    res = urllib.urlopen(movie_url)
    if res.getcode() == 200:
        raw = res.read()
        return json.loads(raw)
    else:
        print 'error getting url ' + url
        return None



favorites = [
            ('mad max: fury road', 'https://www.youtube.com/watch?v=hEJnMQG9ev8'),
            ('the final sacrifice', default_trailer),
            ('surf nazis must die', default_trailer)
        ]

print 'Assembling movie data...'
movies = []
for favorite in favorites:
    print '\tFetching metadata for ' + favorite[0] + '...'

    title = favorite[0]
    trailer = favorite[1]

    imdb_movie = get_imdb_movie(build_url(title))
    if imdb_movie is not None:
        movies.append(media.Movie(
                                    title=imdb_movie['Title'],
                                    trailer_youtube_url=trailer,
                                    poster_image_url=imdb_movie['Poster']))


print 'Movies list built:\n' + str(movies)

print 'Generating movies page and launching browser...'
fresh_tomatoes.open_movies_page(movies)
