# @author Dave Voutila

class Movie:

    title = None
    trailer_youtube_url = None
    poster_image_url = None
    cast = []
    genre = 'Undefined'


    def __init__(self, title, poster_image_url=None, trailer_youtube_url=None):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        return str([self.title, self.poster_image_url, self.trailer_youtube_url])
