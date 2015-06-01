# FSND Project 1 - Movie Trailer Website

**Website**: https://github.com/voutilad/udacity-project1/

**Author**: Dave Voutila - voutilad\[at\]gmail.com

This first project demonstrates some core concepts of utilizing Python classes, proper python styling per [Google's Python Style Guide](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html?showone=Naming#Comments), and some tinkering with [Bootstrap](http://getbootstrap.com).

## Requirements
* Python 2.x - tested with 2.7.6
* Live internet connectivity
* Modern web browser

## Usage
Simply run:
````
python entertainment_center.py
````

### Adding/Removing Movies
To add movies, modify the _entertainment_center.py_  file by adding or removing tuples from the _FAVORITES_ list like so:

`````python
FAVORITES = [
    ('mad max: fury road', 'https://www.youtube.com/watch?v=hEJnMQG9ev8'),
    ('the final sacrifice', None),
    ('surf nazis must die', 'https://www.youtube.com/watch?v=Q8LV1S2q2GA'),
    ('breaking away', 'https://www.youtube.com/watch?v=J1jzs6dk4bs'),
    ('tron', 'https://www.youtube.com/watch?v=L9szn1QQfas'),
    ('ski patrol', 'https://www.youtube.com/watch?v=OTyp09bkZbk')
]
`````

Each tuple follows the format:
`````
(title, youtube_url)
`````
At minimum, a title must be provided. For titles without known trailers, the _youtube_url_ value can be _None_.

The rest is taken care of by the OMDb client (_omdb.py_) for retrieving:
* movie poster url
* MPAA rating
* movie runtime
* year of release
* short plot summary
* IMDB rating

## Some References

- [The Open Movie Database](http://www.omdbapi.com) to fetch metadata (specifically movie posters).
- [Boostrap - Popovers](http://getbootstrap.com/javascript/#popovers)

## Copyright and Licenses

For _fresh_tomatoes.py_, it was provided by [Udacity](http://www.udacity.com) and is used with permission as part of the Full Stack Web Developer Nanodegree course.

For other Python code, see LICENSE file.

For _Fox_movietone_2.jpg_ (the placeholder poster graphic), it is provided in the public domain per https://commons.wikimedia.org/wiki/File:Fox_movietone_2.jpg
