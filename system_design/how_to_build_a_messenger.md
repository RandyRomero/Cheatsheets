# How to build a messaging app? 

### 1st step - ask questions
- why don't we use a ready-made tool/product? 
- How many users are there going to be? One thousand or a billion?
- Do we need support of users groups?
- Do we need read receipts?
- Do we need media files support?
- etc

### 2nd step: overall architecture
I guess it's obvious that we have to have some 
client app which a user can use. We also need
some kind of backend to store user info, conversation
history, how has conversation with whom, things like that.

### 3rd step - client-server communication options

For example, one user client sends a messages, and it was registered 
on server. How would the other user know that there is a message 
for him?

One way is to use http **polling**. For example, one user sends
a message to the server. User client all the time asks the server
if there are some new information. As soon as there is some
new information, user client pulls it from the server.
Drawbacks: too may request from client to the server.

Another way is **long-polling**, when we still make a request from
client app to the server, but the server holds on this request
until there is some new information. Only then the request
is responded.

Third options is **web sockets**. In web sockets we still maintain an
open connection with the server, but it's a duplex connection, so we
can exchange information in real time.

### 4th step - scaling
what if we are going to have a lot of users
If we want to have a huge number of users, it's a good idea to
use several api servers at the same time, put gateway in 
front of them to route connections to the right server and 
a load balancer.

### 5th step - communication between microservices
How would our api servers communicate? 
We can establish a message broker like RabbitMQ or another pub/sub
message queueing system. So every server can publish to this 
broker and subscribe for messages for users that this server 
keeps an open connection with.
For example, Server 1 keeps an open connection with user Mike.
Mike sends a message for Lisa. Server 1 receives this message through
the connection. Server 1 puts this message to the queue. Server 2,
which keeps a connection with Lisa, gets Mike's message from the queue
and sends it to Lisa.

### 6th - define some tables that we would need
What tables do we need?
Some table to store users, namely user_id, user nickname, some bio and last_seen.
Also, we need a table for messages: id, user, conversation, text, media_url. 
For conversations: id, name
m2m user_conversation

### 7th step - caching
It would also be nice to add caching. Caching in the client application and database caching.

### 8th step - how to store media files
To store media we could use an external service like amazon or google s3. For that we just need
a microservice that would redirect request to get or put file to s3.

### 9th step - external notifications
Last thing - we need some kind of notification service that would send notifications when the user
if offline. For that purpose we need to subscribe another microservice to our message broker
and use something like android or ios api for Push Notifications.

https://www.youtube.com/watch?v=uzeJb7ZjoQ4


### What are 9 step to design a messaging app?

1. ask question
2. overall architecture
3. client-server communication options
4. scaling
5. communication between microservices
6. define some tables that we would need
7. caching
8. how to store media files
9. external notifications

question id: c8a41c28-1fdb-443f-9621-68346d76f132


### What is the 1st step of designing a messaging app is about?

answer
ask questions
- why don't we use a ready-made tool/product? 
- How many users are there going to be? One thousand or a billion?
- Do we need support of users groups?
- Do we need read receipts?
- Do we need media files support?
- do we need encryption?
- etc

question id: e373a9b4-b8da-4b17-87ec-e5674b4744ec


### What is the 2nd step of designing a messaging app - overall architecture - is about?

I guess it's obvious that we have to have some 
client app which a user can use. We also need
some kind of backend to store user info, conversation
history, how has conversation with whom, things like that.

question id: 79917522-6d34-4ee8-b435-7acc0f2acab8


### What is the 3rd step of designing a messaging app - client-server communication options - is about?

For example, one user client sends a messages, and it was registered 
on server. How would the other user know that there is a message 
for him?

One way is to use http **polling**. For example, one user sends
a message to the server. User client all the time asks the server
if there are some new information. As soon as there is some
new information, user client pulls it from the server.
Drawbacks: too may request from client to the server.

Another way is **long-polling**, when we still make a request from
client app to the server, but the server holds on this request
until there is some new information. Only then the request
is responded.

Third options is **web sockets**. In web sockets we still maintain an
open connection with the server, but it's a duplex connection, so we
can exchange information in real time.

question id: 3827f4d6-cb33-4d43-8b7e-ebfe54c1af85


### What is the 4th step of designing a messaging app - scaling - is about?

What if we are going to have a lot of users?
If we want to have a huge number of users, it's a good idea to
use several api servers at the same time, put gateway in 
front of them to route connections to the right server and 
a load balancer.

question id: 9357e55c-d310-4375-a6b0-df2fa711adde


### What is the 5th step of designing a messaging app - communication between microservices - is about?

How would our api servers communicate? 
We can establish a message broker like RabbitMQ or another pub/sub
message queueing system. So every server can publish to this 
broker and subscribe for messages for users that this server 
keeps an open connection with.
For example, Server 1 keeps an open connection with user Mike.
Mike sends a message for Lisa. Server 1 receives this message through
the connection. Server 1 puts this message to the queue. Server 2,
which keeps a connection with Lisa, gets Mike's message from the queue
and sends it to Lisa.

question id: faddd0d0-9d27-4a15-b80b-08889ffb43a2


### What is the 6th step of designing a messaging app - define some tables that we would need - is about?

What tables do we need?
Some table to store users, namely user_id, user nickname, some bio and last_seen.
Also, we need a table for messages: id, user, conversation, text, media_url. 
For conversations: id, name
m2m user_conversation

question id: da3d9c86-d6e5-4112-9e2c-5d02a9a40537


### What is the 7th step of designing a messaging app - caching - is about?

It would also be nice to add caching. Caching in the client application and database caching.

question id: 653e69ef-a667-422e-914e-657a3fbc2495


### What is the 8th step of designing a messaging app - how to store media files - is about?

To store media we could use an external service like amazon or google s3. For that we just need
a microservice that would redirect request to get or put file to s3.

question id: e5acb02c-57ce-46ac-884e-2401657343cb


### What is the 9th step of designing a messaging app - external notifications - is about?

Last thing - we need some kind of notification service that would send notifications when the user
if offline. For that purpose we need to subscribe another microservice to our message broker
and use something like android or ios api for Push Notifications.

question id: d9df7204-7737-4754-92f2-6fdda8c9aa61
