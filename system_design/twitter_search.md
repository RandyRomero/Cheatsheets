When a new tweet is posted, it (apart from getting to the database and to the cache of users in cluster of Redises),
gets to an Ingester.

Ingester figures out everything we want to index against in this tweet.

Then that tweet is send to an Early bird machine. 

In Twitter search is not precompucted (in opposite to Home Timeline).


earch results are personalized


### What is Lucene? 

answer:

Apache Lucene™ is a text search engine library written entirely in Java.

https://en.wikipedia.org/wiki/Apache_Lucene

question id: 9ce79f67-1275-482e-8b3e-ec7fcc732e2a


### What is Earlybird?

answer:

Earlybird, a real-time, reverse index based on Lucene

https://blog.twitter.com/engineering/en_us/a/2011/the-engineering-behind-twitter-s-new-search-experience

question id: 


Twitter also has internal precomputed activity timeline (number of likes, reposts, favourites) that are cached on write.
It is used, for example, to rank search results by number of different activities.



