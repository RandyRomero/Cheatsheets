### How does Twitter constructs you home timeline (list of tweets of people you follow)?

answer:
It already has it preconstructed in Redis cache with all tweet ids.
So it only need to go and get them from the database.

question id: 1020b302-9560-4f39-ad97-049c2fd6193


### How do Twitter preconstructed home timeline of a user look like?

answer:
tweet_id user_id some_meta(like was it reply, repost, etc)

question id: 1096ff8c-b901-4517-a8bc-9a5835e7146f


### Where does Twitter store precomputed user feed (home timeline)?

answer
On a cluster of Redises. For each user it replicates it 3 times.

question id: 9583bfa0-3db4-4e5d-9bd4-4a1927248ed3


### How do Twitter knows where on cluster of Redises to find home timeline of a specific user?

answer
It just uses a hash map.

question id: bfca2848-bd7d-454f-8118-79a00d3c73d0


### What's happening with a tweet you post?

answer
Apart from being saved in database, it automatically gets to 
home timeline cache of all people who you follow. Not the tweet itself,
but its id with your user id and some metadata. So that next time one of
your friends want to read his home timeline, all latest tweet will be
already there for him.

question id: 32182aee-cc18-40b6-8cac-1e206bc6ea2a


### What are constraint for Twitter user timeline?

answer
- for one user it stores not more than aroung 800 tweets
- for famous people it does not put tweets in cache for there followers
- it does not put tweets in cache of inactive people (who hasn't been twitter for around a month or more)

question id: ac41e78c-df0c-46bf-8c88-1e35e3ef0c57


### Why doesn't twitter puts tweets of celebrities in their followers home timeline cache?

answer:

Fanout for celebrities can get very slow and it was the biggest problem of Twitter.

There are people on Twitter who is followed by tens of millions of people. That
means, when lagy gaga tweets, her tweet should be cached in ~30 millions users'
home timelines + its replicas, which gives us 90 million insertions. 

Also when celebrities tweet, it produces a lot of race conditions in Twitter. 
For example, if you with not a lot of followers reply on tweet of Lady Gaga, your 
friends may see your reply much earlier than their precomputed timeline gets the
Lady Gaga tweet. 


So Twitter stop doing fanout for users with millions of followrs and just 
merge their tweets in home timeline of a user on read. So the whole home timeline
is precomputed with exception of tweets of celebrities. 

Still, if you have aroung 1 million of followers, your tweet will be delivered to all
of them in about 3.5 seconds. However, it gets pretty bad on scale of Lady Gaga (~30 million) - p99 can get up to 5 minutes.

question id: b565d97f-8d76-48a1-b5d6-b7611e0e9bfe



core features:

1. sending a tweet
2. timelines
- having a timeline (feed) where you can see other peoples' tweets
- see tweets of people that you don't follow, but that were reacted upon by someone you follow
3. 


timeline -> User Timeline (where there are your tweets and tweets that you retweeted)
         -> Home Timeline (where there are tweets of people you follow)


With User Timeline it's all simple: just retrieve all your tweets (tweets that you retweeted can be rows that contain foreign keys on someone elses tweets)


Very naive solution:
Use relation database like PostgreSQL, where you have User and Tweet table
User tweets a message and that is just one record in Tweet table. And Tweet
table has a column like user_id or sender_id. In this case, if a user
want's to check his home timeline, we need to join all people who he follows
and find in a Tweet table all their tweets and sort them chronologically.

However at some point the Tweet table would become enormous. 


If you think about how people use Twitter and what are most important characteristics of it,
you can agree that people read tweets much more than they post them. 

So what you really want is to optimise reading tweets, make reading as fast as it could be.
Of course, you want to make posting fast too. Particularly, when you friend posts something,
you want to be able to see it as fast as possible. However, if posting can take some time
(as a background task, of course), it's not that big of a deal. Much worse if it
takes seconds as if you would have to wait seconds until your feed updates.


So, in order to make computing home feed for every user extremely fast, Twitter does
the following: it precomputes home feed for every user in Redis. And every time
a user posts a new tweet, his followers precomputed timelines get this tweet.

However, not all the users, only recently active (we don't want waste our time
on those who reads Twitter once in a couple of weeks.)

That means that if you have 100 followers, posting a tweet will trigger 100 operations to
update home feeds of your friends. Actually, 3 times more, or 300 operations, as Twitter
allegedly has 3 replicas of Redis where it stores user feeds.

However, it doesn't work well for people with millions of followers, because it takes too
much time to update millions of feed-caches. So for such user Twitter makes an exception -
their tweets doesn't get to cache until a user asks for feed upload.



============================ Timelines at Scale ==============================
https://www.infoq.com/presentations/Twitter-Timeline-Scalability/


Two main types of timelines that users interact to:
- User timeline (all tweets that user has sent)
- Home timeline (tweats of people you follow)



Cache stores not more than 800 tweets for every user home timeline. 
No, if you scroll down, twitter won't pull older tweets for you. 
You, user, can't get more than 800.

If your timeline not in Redis, it would be reconstructed on demand.
It means, that once again Twitter figures out all of your friends
from Social Graph service. Then pulls ids of tweets and their senders
from database to your home timeline cache in Redis.

It's a relatively taxing operation, that's why Twitter replicates 
user timeline cache for every user three times. Probability
that all three Redis-machines would be down is not that high.


User timeline cache stores only tweet ids, not tweets itself. 
So twitter still have to go and get the actual tweets



Challenge #2 

Fanout for celebrities can get very slow and it was the biggest problem of Twitter.

There are people on Twitter who is followed by tens of millions of people. That
means, when lagy gaga tweets, her tweet should be cached in ~30 millions users'
home timelines + its replicas, which gives us 90 million insertions. 

Also when celebrities tweet, it produces a lot of race conditions in Twitter. 
For example, if you with not a lot of followers reply on tweet of Lady Gaga, your 
friends may see your reply much earlier than their precomputed timeline gets the
Lady Gaga tweet. 


So Twitter stop doing fanout for users with millions of followrs and just 
merge their tweets in home timeline of a user on read. So the whole home timeline
is precomputed with exception of tweets of celebrities. 

Still, if you have aroung 1 million of followers, your tweet will be delivered to all
of them in about 3.5 seconds. However, it gets pretty bad on scale of Lady Gaga (~30 million) - p99 can get up to 5 minutes.

There are around 400 million tweets per day. 4600 tweets per second.


2016:

Twitter delivers 20 million tweets per second to users home timeline. 
Almost 2 trillion tweet deliveres per day.
150 000 000 redis operations per second.