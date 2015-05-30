#!/usr/bin/python
import media
import fresh_tomatoes

madmax = media.Movie('Mad Max: Fury Road', 'http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI', 'https://www.youtube.com/watch?v=hEJnMQG9ev8')

fresh_tomatoes.open_movies_page([madmax])
