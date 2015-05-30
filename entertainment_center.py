#!/usr/bin/python
import media
import fresh_tomatoes

print 'Assembling movie data...'
madmax = media.Movie('Mad Max: Fury Road', 'http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI', 'https://www.youtube.com/watch?v=hEJnMQG9ev8')
madmax.rating('R')
badger = media.Movie('ESPN 30 for 30: Slaying the Badger', 'http://ecx.images-amazon.com/images/I/71KjRpHIpbL._SX425_.jpg', 'https://www.youtube.com/watch?v=6H7w89aZHZo')

movies = [madmax, badger]

print 'Movies list built:\n' + str(movies)

print 'Generating movies page and launching browser...'
fresh_tomatoes.open_movies_page(movies)
