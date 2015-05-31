# -*- coding: utf-8 -*-
"""
This module defines the `Movie` class for use in Project 1.
"""

class Movie(object):
    """
    Represents a movie for display in the Fresh Tomatoes web application

    Attributes:
        title (str): Movie title
        poster_image_url (str): optional URL to hosted poster image
        trailer_youtube_url (str): optional URL to the youtube video of the trailer
    """

    def __init__(self, title, poster_image_url=None, trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url

        if trailer_youtube_url is None:
            self.trailer_youtube_url = 'https://www.youtube.com/watch?v=5uZr3JWYdy8'
        else:
            self.trailer_youtube_url = trailer_youtube_url


    def __str__(self):
        return str([self.title, self.poster_image_url, self.trailer_youtube_url])
