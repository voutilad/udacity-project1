# -*- coding: utf-8 -*-
"""
This module defines the `Movie` class for use in Project 1.
"""

_DEFAULT_POSTER_URL = 'Fox_movietone_2.jpg'
_DEFAULT_TRAILER_URL = 'https://www.youtube.com/watch?v=5uZr3JWYdy8'



class Movie(object):
    """
    Represents a movie for display in the Fresh Tomatoes web application

    Attributes:
        title (str): Movie title
        poster_image_url (str): optional URL to hosted poster image
        trailer_youtube_url (str): optional URL to the youtube video of the trailer
    """

    #pylint: disable=too-many-instance-attributes

    def __init__(self, title, poster_image_url=None,
                 trailer_youtube_url=None, **kwargs):

        self.title = title
        self.poster_image_url = poster_image_url

        if poster_image_url is None:
            self.poster_image_url = _DEFAULT_POSTER_URL
        else:
            self.poster_image_url = poster_image_url

        if trailer_youtube_url is None:
            self.trailer_youtube_url = _DEFAULT_TRAILER_URL
        else:
            self.trailer_youtube_url = trailer_youtube_url

        #some extra attributes for prettifying the descriptions
        self.attributes = kwargs


    def describe(self):
        """
        Returns a summary of key movie attributes as a string.
        """
        description = ''

        if self.attributes.has_key('release_date'):
            description = description + ' (' + str(self.attributes['release_date']) + ')'
        if self.attributes.has_key('running_time'):
            description = description + ' [' + str(self.attributes['running_time']) + ']'
        if self.attributes.has_key('rating'):
            description = description + '\nRated: ' + str(self.attributes['rating'])
        if self.attributes.has_key('plot_summary'):
            description = description + '\n' + self.attributes['plot_summary']
        if self.attributes.has_key('popularity'):
            description = description + '\n[' + str(self.attributes['popularity']) + ']'

        return description


    def describe_html(self):
        """
        Returns an HTML formatted summary of key movie attributes as a string.
        """
        description = ''
        if self.attributes.has_key('rating'):
            description = description + '<b>Rated:</b> ' + str(self.attributes['rating']) + '<br>'

        if self.attributes.has_key('release_date'):
            description = description + '<b>Released:</b> '
            description = description + str(self.attributes['release_date']) + '<br>'

        if self.attributes.has_key('running_time'):
            description = description + '<b>Running Time</b>: '
            description = description + str(self.attributes['running_time']) + '<br>'

        if self.attributes.has_key('popularity'):
            description = description + '<b>IMDB Rating:</b> '
            description = description + str(self.attributes['popularity']) + ' out of 10<br>'

        if self.attributes.has_key('plot_summary'):
            description = description + '<i>' + self.attributes['plot_summary'] + "</i><br>"

        return description


    def __str__(self):
        return self.describe()
