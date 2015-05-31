# -*- coding: utf-8 -*-
"""
This module defines the `Movie` class for use in Project 1.
"""

class Movie(object):
    """
    Attributes:
        title (str): Movie title
        poster_image_url (str): URL to hosted poster image
        trailer_youtube_url (str): URL to the youtube video of the trailer
    """

    def __init__(self, title, poster_image_url=None, trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


    def __str__(self):
        return str([self.title, self.poster_image_url, self.trailer_youtube_url])
