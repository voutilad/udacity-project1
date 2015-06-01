#!/usr/bin/python
"""
Assembles and launches the Fresh Tomatoes website.

    Run:
        python entertainment_center.py
"""
import media, omdb
import fresh_tomatoes

MOVIES = []
FAVORITES = [
    ('mad max: fury road', 'https://www.youtube.com/watch?v=hEJnMQG9ev8'),
    ('the final sacrifice', None),
    ('surf nazis must die', 'https://www.youtube.com/watch?v=Q8LV1S2q2GA'),
    ('breaking away', 'https://www.youtube.com/watch?v=J1jzs6dk4bs'),
    ('tron', 'https://www.youtube.com/watch?v=L9szn1QQfas'),
    ('ski patrol', 'https://www.youtube.com/watch?v=OTyp09bkZbk')
]

print 'Assembling movie data...'

for favorite in FAVORITES:
    print ' Fetching metadata for ' + favorite[0] + '...'

    title = favorite[0]
    trailer = favorite[1]

    imdb_movie = omdb.search(title)
    if imdb_movie['Poster'] == 'N/A':
        imdb_movie['Poster'] = None

    if imdb_movie is not None:
        movie = media.Movie(
            title=imdb_movie['Title'],
            trailer_youtube_url=trailer,
            poster_image_url=imdb_movie['Poster'],
            rating=imdb_movie['Rated'],
            release_date=imdb_movie['Released'],
            plot_summary=imdb_movie['Plot'],
            running_time=imdb_movie['Runtime'],
            popularity=imdb_movie['imdbRating'])
        MOVIES.append(movie)


print 'Movies list built:\n' + str(MOVIES)

print 'Generating movies page and launching browser...'
fresh_tomatoes.open_movies_page(MOVIES)
