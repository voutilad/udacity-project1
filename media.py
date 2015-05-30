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
    title = None
    trailer_youtube_url = None
    poster_image_url = None
    cast = []
    genre = 'Undefined'
    release_date = None
    mpaa_rating = None
    running_time = -1


    def __init__(self, title, poster_image_url=None, trailer_youtube_url=None):
        self.title = title

        if poster_image_url is None:
            self.poster_image_url = ''
        else:
            self.poster_image_url = poster_image_url

        if trailer_youtube_url is None:
            self.trailer_youtube_url = ''
        else:
            self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        return str([self.title, self.poster_image_url, self.trailer_youtube_url])

    def running_time(self, running_time=None):
        """"
        """"
        if running_time is None:
            if self.running_time is None:
                return -1
            else:
                return self.running_time
        else:
            if type(running_time) is int and running_time > -1:
                self.running_time = running_time
                return self.running_time
            else:
                raise Exception('Invalid running_time format. Expecting a positive integer.')

    def rating(self, mpaa_rating=None):
        """
        Sets and returns the MPAA movie rating.
        Attributes:
            mpaa_rating (str): Optional new value for MPAA rating
        Returns:
            mpaa_rating (str): current mpaa_rating value
        """
        if mpaa_rating is None:
            if self.mpaa_rating is None:
                return 'Unrated'
            else:
                return self.mpaa_rating
        else:
            if type(mpaa_rating) is str:
                self.mpaa_rating = mpaa_rating
                return self.mpaa_rating
            else:
                raise Exception('Invalid rating value')
