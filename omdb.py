"""
A simple implementation of the OMDb API <http://www.omdbapi.com>.

"""
import urllib, urllib2
import json

__OMDB_URL = 'http://www.omdbapi.com/?y=&plot=short&r=json&'


def __build_url(movie_title):
    """
    Builds the OMDb API url <http://www.omdbapi.com> that looks up a title and returns JSON.
    Args:
        movie_title: string of a movie title to search for

    Returns:
        a url as a string representing a GETable OMDb title lookup
    """
    return __OMDB_URL + urllib.urlencode({'t': movie_title})


def search(movie_title):
    """
    Fetches a title from OMDb using their public API.

    Args:
        movie_url: string url representing a particular movie search

    Returns:
        a python dict object with the OMDb metadata or None if an error occurs

    """
    try:
        url = __build_url(movie_title)
        res = urllib.urlopen(url)

        if res.getcode() == 200:
            raw = res.read()
            return json.loads(raw)
        else:
            return None

    except urllib2.URLError:
        return None
