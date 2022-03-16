### What is RabbitMQ? 

RabbitMQ is a message broker: it accepts and forwards messages. What's broker? Broker is a service
that receives, stores and sends messages.

You can think about it as a post office: when you put the mail that you want posting in a post box, 
you can be sure that the letter carrier will eventually deliver the mail to your recipient. 
In this analogy, RabbitMQ is a post box, a post office, and a letter carrier.

question id: 23af12e4-9c07-490a-ab16-1520286bb7b3


### What protocol does RabbitMQ use?

AMQP - Advanced Message Queuing Protocol

question id: 9c70c4d2-220c-495a-8ccb-483a0cf908c4


### What is AMQP? 

AMQP - Advanced Message Queuing Protocol

questiod id: 2ddeed47-0e1f-4c3a-8dc6-983c1b443c89


### What are MQ pros over HTTP/REST?

- you can fire and forget, not wating for response of the receiver
- consumers can consume messages at their own speed
- where one process can continue to do work even if the other process is not available vs. HTTP having to retry.
- with MQ there is less hassle when you need to send the same message to different microservices
- message will be delivered and will be delivered exactly one time - more robust against network failures than http-requests
- can work as a loadbalancer (you sent a task, one of consumers, the least busy one, will take it)

question id: 70e5dd33-e750-4528-b6da-a0e3a434090c


### What are MQ cons in comparison to HTTP/REST?

- your producer doesn't know what was response of the consumer (maybe message wasn't valid and didn't make it). 
You can get answer via RPC, but it kinda ruins the point of MQ
- not as convenient as HTTP when you need to get something from other microservice immediately. Of cource you can use RPC pattern
with MQ, but it is nothing better than using REST, though REST has APIs, well known verbs and status codes that make 
working with it much more pleasant

question id: 1c9b1b94-33b6-411d-9dd3-8d2a50ba7a71


Examples:
#### Fire-and-forgen vs I need your answer immediately
One of the biggest differences is that REST implies synchronous processing while MQ is more often asynchronous. 
Which means with HTTP-requests you wait for the server to respond to you, while with MQ you just fire-and-forget

So one of the great difference for me is that we the HTTP we know whether receiver got our message and how 
it has responded (accepted, created new resource, denied our request and why).

With MQ you just fire-and-forget. It's very suitable for cases where your microservices is not the one who
cares whether message was caught and processed by someone.

#### Loose coupling. 
Where one process can continue to do work even if the other process is not available vs. HTTP having to retry.
MQ is a way to decouple producer and consumer so that they don't have to 
be online at the same time but the system would still be functioning as a whole.

#### One-to-one or one-to-many
With HTTP you can only make one request to one specific service at a time. If that's what
you want - perfect. If you want to send your message to a few other services - MQ is more sutable
as your service still send only one message, it does not waste time on multiple request.

For exapmle, if several of your microservices is interested in some event, 
there is less overhead in perfomance to use pub/sub model of MQ, than 
make http-request to each server. You don't even have to know about
them who want your event, you just send your events to message broker
and go back to your business. 



### What is a producer? 

A producer is a user application that sends messages.

question id: 0b17856e-22f5-47b6-9a26-a93d5f3ec8c1


### What is a consumer? 

A consumer is a user application that receives messages.

question id: e7c415b4-6513-49c0-9e0f-d1a5df90275d


### What is a routing key?

A key that the exchange looks at to decide how to route the message to queues. 
Think of the routing key like an address for the message.

question id: 75fb7e9a-daf1-42c9-bd75-d22aae77798d


### misc

Note that the producer, consumer, and broker do not have to reside on the same host; indeed in most applications they don't. 
An application can be both a producer and consumer, too.


## Queue

### What's queue? 

Queue is a buffer that stores messages, that have been sent buy publishers, received and distributed by an exchange and wait for being consumed.

question id: 37407e61-b5d4-4180-a8cb-c79fb1daffde



### How to identify a queue? 

All queues have a name, either defined by user or, as a fallback, server-generated. 

Server-named queues are meant to be used for state that is transient in nature and specific to a 
particular consumer (application instance). Applications can share such names in message metadata 
to let other applications respond to them (like in RPC).

question id: 2f3b1385-f1d5-47e0-bc72-0efebea69a89


### How big can a queue be? 

A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.
However, you can set maximum number of messages for a queue or TTL (either for a queue or messages)

question id: 5ace5f49-3411-4581-9348-13d504576838


### Will creating a queue with same name and same properties cause an error?

Creating a queue using queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created.
But if you try to create a queue with existing name, but other properties, you will get an error.

Before a queue can be used it has to be declared. Declaring a queue will cause it to be created if it does not already exist. 
The declaration will have no effect if the queue does already exist and its attributes are the same as those in the declaration. 
When the existing queue attributes are not the same as those in the declaration a channel-level exception with code 406 (PRECONDITION_FAILED) will be raised.

question id: 182c0866-f0e4-4b45-9d09-d31076c064b


### What properties does a queue have?

- name
- durable
- exclusive
- auto-delete
- arguments

question id: 9eddccce-6cdc-4e95-b5c3-aaece49c8cf3


### What does 'durable' property of a queue mean?

When RabbitMQ quits or crashes it will forget the queues and messages unless you tell it not to.
And if there is no queue, exchange will just drop new messages that are dedicated for this queue.

So durable=True flag will prevent from queue to be lost on RabbitMQ restart.
```python
channel.queue_declare(queue='task_queue', durable=True)
```

Although messages still will be lost unless you mark them as persistent on publishing 
by supplying a delivery_mode property with a value 2.


```python
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```

question id: fd8b00a5-8319-476b-a5c2-9b58618da3ce


### How not to lost messages due to broker restart?

Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.

First, we need to make sure that the queue will survive a RabbitMQ node restart. 
In order to do so, we need to declare it as durable:

```python
channel.queue_declare(queue='task_queue', durable=True)
```

At that point we're sure that the task_queue queue won't be lost even if RabbitMQ restarts. 
Now we need to mark our messages as persistent - by supplying a delivery_mode property with a value 2.


```python
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```


Note on message persistence
Marking messages as persistent doesn't fully guarantee that a message won't be lost. 
Although it tells RabbitMQ to save the message to disk, there is still a short time window when RabbitMQ has accepted a message and hasn't saved it yet. 
Also, RabbitMQ doesn't do fsync(2) for every message -- it may be just saved to cache and not really written to the disk. 
The persistence guarantees aren't strong, but it's more than enough for our simple task queue. If you need a stronger guarantee then you can use publisher confirms.

Both persistent and transient messages can be written to disk. 
Persistent messages will be written to disk as soon as they reach the queue, 
while transient messages will be written to disk only so that they can be evicted from memory while under memory pressure. 
Persistent messages are also kept in memory when possible and only evicted from memory under memory pressure. 
The "persistence layer" refers to the mechanism used to store messages of both types to disk.

question id: d32f8e60-cca4-4074-8810-9b1e3d342c5f




### What is the difference between a durable and transient queue?

Transient queues will be deleted on node boot. They therefore will not survive a node restart, by design. 
Messages in transient queues will also be discarded.

Durable queues will be recovered on node boot, including messages in them published as persistent. 
Messages published as transient will be discarded during recovery, even if they were stored in durable queues.

question id: c8585694-7e66-4b55-988a-b683ab3f22c8


### What is an Exclusive queue and why do we need it? 

An exclusive queue can only be used (consumed from, purged, deleted, etc) by its declaring connection. 
An attempt to use an exclusive queue from a different connection will result in a 
channel-level exception RESOURCE_LOCKED with an error message that says cannot obtain exclusive access to locked queue.

Exclusive queues are deleted when their declaring connection is closed or gone (e.g. due to underlying TCP connection loss). 
They therefore are only suitable for client-specific transient state.

It is common to make exclusive queues server-named.

question id: 3f4c5ef5-2b35-4997-823f-b1af2c0de018



## Exchange

### What is Exchange?

Exhange receives messages from producers and pushes them to queues depending on rules defined by the exchange type. 
To receive messages, a queue needs to be bound to at least one exchange.

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. 
Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.

Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. 
On one side it receives messages from producers and the other side it pushes them to queues. 
The exchange must know exactly what to do with a message it receives. 
Should it be appended to a particular queue? Should it be appended to many queues? 
Or should it get discarded. The rules for that are defined by the exchange type.

question id: 4bdc6c1d-ddbe-43c6-a92f-9b8b56117da5


### What are exchange types?

- Direct exchange
- Fanout exchange
- Topic exchange
- Headers exchange

question id: ac0b6cd1-279d-466f-b606-26894b565ba5


### How do durable and transient Exchanges differ from each other?

Durable exchanges survive broker restart whereas transient exchanges do not (they have to be redeclared when broker comes back online). 
Not all scenarios and use cases require exchanges to be durable.

question id: 259f8e92-bd67-49ee-8db7-7916d2e20669


### What is default Exchange? 

The default exchange is a direct exchange with no name (empty string) pre-declared by the broker.

question id: ef1995e8-95a5-4fad-b1f1-b833140dd448



### What is special about Default Exchange?

The default exchange is a direct exchange with no name (empty string) pre-declared by the broker. 
It has one special property that makes it very useful for simple applications: every queue that is 
created is automatically bound to it with a routing key which is the same as the queue name.

For example, when you declare a queue with the name of "search-indexing-online", 
the AMQP 0-9-1 broker will bind it to the default exchange using "search-indexing-online" as the routing key (in this context sometimes referred to as the binding key). 
Therefore, a message published to the default exchange with the routing key "search-indexing-online" will be routed to the queue "search-indexing-online". 
In other words, the default exchange makes it seem like it is possible to deliver messages directly to queues, even though that is not technically what is happening.

question id: 9cda0df9-7071-4dc4-9746-0e277358e53b


### What is the difference between binding key and routing key?

Routing key is sent with published message. Binding key is key that is used when binding queues and exchanges.
Binding key can use stars and hashes to make queue able to get messages with different routing keys.

question id: b66e4674-5ad2-4a81-800f-413ef0b2ab62


### What is Topic type of an Exchange?

Messages sent to a topic exchange can't have an arbitrary routing_key - it must be a list of words, delimited by dots. 
The words can be anything, but usually they specify some features connected to the message. 
A few valid routing key examples: "stock.usd.nyse", "nyse.vmw", "quick.orange.rabbit". 
There can be as many words in the routing key as you like, up to the limit of 255 bytes.

The binding key must also be in the same form. The logic behind the topic exchange is similar to a direct one - 
a message sent with a particular routing key will be delivered to all the queues that are bound with a matching 
binding key. However there are two important special cases for binding keys:

'*' (star) can substitute for exactly one word.
'#' (hash) can substitute for zero or more words.

For example, we're going to send messages which all describe animals. 
The messages will be sent with a routing key that consists of three words (two dots). 
The first word in the routing key will describe a celerity, second a colour and third a species: "<celerity>.<colour>.<species>".

We created three bindings: Q1 is bound with binding key "*.orange.*" and Q2 with "*.*.rabbit" and "lazy.#".

These bindings can be summarised as:

Q1 is interested in all the orange animals.
Q2 wants to hear everything about rabbits, and everything about lazy animals.
A message with a routing key set to "quick.orange.rabbit" will be delivered to both queues. 
Message "lazy.orange.elephant" also will go to both of them. 
On the other hand "quick.orange.fox" will only go to the first queue, and "lazy.brown.fox" only to the second. 
"lazy.pink.rabbit" will be delivered to the second queue only once, even though it matches two bindings. 
"quick.brown.fox" doesn't match any binding so it will be discarded.

What happens if we break our contract and send a message with one or four words, like "orange" or "quick.orange.male.rabbit"? 
Well, these messages won't match any bindings and will be lost.

On the other hand "lazy.orange.male.rabbit", even though it has four words, will match the last binding and will be delivered to the second queue.

https://www.rabbitmq.com/tutorials/tutorial-five-python.html

Example uses:

Distributing data relevant to specific geographic location, for example, points of sale
Background task processing done by multiple workers, each capable of handling specific set of tasks
Stocks price updates (and updates on other kinds of financial data)
News updates that involve categorization or tagging (for example, only for a particular sport or team)
Orchestration of services of different kinds in the cloud
Distributed architecture/OS-specific software builds or packaging where each builder can handle only one architecture or OS

https://www.rabbitmq.com/tutorials/amqp-concepts.html#exchange-topic

question id: 965671c9-c264-412c-9fd6-baf712f7a1a7


### What is Fanout type of an Exchange?

A fanout exchange routes messages to all of the queues that are bound 
to it and the routing key is ignored. If N queues are bound to a fanout exchange, 
when a new message is published to that exchange a copy of the message is delivered to all N queues. 
Fanout exchanges are ideal for the broadcast routing of messages.

Because a fanout exchange delivers a copy of a message to every queue bound to it, its use cases are quite similar:

- Massively multi-player online (MMO) games can use it for leaderboard updates or other global events
- Sport news sites can use fanout exchanges for distributing score updates to mobile clients in near real-time
- Distributed systems can broadcast various state and configuration updates
- Group chats can distribute messages between participants using a fanout exchange (although AMQP does not have a built-in concept of presence, so XMPP may be a better choice)

question id: 135c458a-e149-4b26-8ba2-e3562a1be0ed


### What is Headers type of an Exchange?

A headers exchange is designed for routing on multiple attributes that are more easily expressed as message headers than a routing key. 
Headers exchanges ignore the routing key attribute. Instead, the attributes used for routing are taken from the headers attribute. 
A message is considered matching if the value of the header equals the value specified upon binding.

It is possible to bind a queue to a headers exchange using more than one header for matching. 
In this case, the broker needs one more piece of information from the application developer, namely, should it consider messages with 
any of the headers matching, or all of them? This is what the "x-match" binding argument is for. When the "x-match" argument is set 
to "any", just one matching header value is sufficient. Alternatively, setting "x-match" to "all" mandates that all the values must match.

Headers exchanges can be looked upon as "direct exchanges on steroids". Because they route based on header values, they can be used as 
direct exchanges where the routing key does not have to be a string; it could be an integer or a hash (dictionary) for example.

Note that headers beginning with the string x- will not be used to evaluate matches.

question id: 72a6df53-cba5-4850-9a2a-4bbe8007ac20 


### What is Channel?

A virtual connection inside a connection. When publishing or consuming messages from a queue - it's all done over a channel.

Some applications need multiple connections to the broker. However, it is undesirable to 
keep many TCP connections open at the same time because doing so consumes system resources
and makes it more difficult to configure firewalls. AMQP 0-9-1 connections are multiplexed with channels.

Every protocol operation performed by a client happens on a channel. Communication on a particular channel is 
completely separate from communication on another channel, therefore every protocol method also carries a 
channel ID (a.k.a. channel number), an integer that both the broker and clients use to figure out which 
channel the method is for.

A channel only exists in the context of a connection and never on its own. When a connection is closed, 
so are all channels on it.

For applications that use multiple threads/processes for processing, it is very common to open a new 
channel per thread/process and not share channels between them.

question id: d6016dac-6103-4c86-9747-b4e156d0d246


### What is virtual host and why do we need it in RabbitMQ?

Virtual hosts
To make it possible for a single broker to host multiple isolated "environments" (groups of users, 
exchanges, queues and so on), AMQP 0-9-1 includes the concept of virtual hosts (vhosts). They are 
similar to virtual hosts used by many popular Web servers and provide completely isolated environments 
in which AMQP entities live. Protocol clients specify what vhosts they want to use during connection 
negotiation.

question id: 1faf7e31-038a-4686-aaee-715b2ee581d2


### Describe steps to write simple producer

answer:
- create connection
- create channel
- declare exchange with name and type
- publish message to the exchange with routing key
- close connection

question id: 7ab559dc-5054-4dea-afdc-77c0530e567a


### Describe steps to write simple consumer

- create connection
- create channel
- set prefetch count
- declare exchange with name and type
- declare a queue with a name
- bind queue, exchange and routing key together
- write function that will process the message
- iterate over the queue
- process every message with your processing function
- nack message in case of exception
- ack message otherwise
- close channel and connection

question id: 3b34a8e6-2852-427f-9951-eeda7c4b64bf


### What is channel.set_qos(prefetch_count=1) or channel.basic_qos(prefetch_count=1)?

The client can request that messages be sent in advance so that when the client finishes processing a message, 
the following message is already held locally, rather than needing to be sent down the channel. Prefetching gives a 
performance improvement.

prefetch-count specifies how many messages will be prefetched by the consumer in advance

https://www.rabbitmq.com/confirms.html#channel-qos-prefetch

question id: 1dd3da49-d10f-443d-98bb-53a88dddb6a9


### Write simple producer which takes user's input and send it as a message


```python
import asyncio

EXCHANGE_NAME = "auth"
ROUTING_KEY = "experimental"
RABBIT_CREDENTIALS = "amqp://guest:guest@localhost/"


async def main(loop):
    # your code here

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
```

===================answer=============

```python
import asyncio

from aio_pika import connect_robust, ExchangeType, Message

EXCHANGE_NAME = "auth"
ROUTING_KEY = "experimental"
RABBIT_CREDENTIALS = "amqp://guest:guest@localhost/"

async def main(loop):
    connection = await connect_robust(
        RABBIT_CREDENTIALS, loop=loop
    )

    channel = await connection.channel()

    exchange = await channel.declare_exchange(EXCHANGE_NAME, type=ExchangeType.DIRECT, durable=True)

    message = ""
    while message != "exit":
        message = input()
        await exchange.publish(Message(message.encode("utf8")), routing_key=ROUTING_KEY)

    await connection.close()
    print("exit")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
```

question id: dd7860bb-141d-49b8-be0c-f853c8eab183


### Write simple consumer

```python
import asyncio

EXCHANGE_NAME = "auth"
ROUTING_KEY = "experimental"
RABBIT_CREDENTIALS = "amqp://guest:guest@localhost/"
QUEUE_NAME = "message_queue"

# your code here
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
    loop.close()
```

=============================answer======================


```python
import asyncio

from aio_pika import connect_robust, ExchangeType

EXCHANGE_NAME = "auth"
ROUTING_KEY = "experimental"
RABBIT_CREDENTIALS = "amqp://guest:guest@localhost/"
QUEUE_NAME = "message_queue"

async def process_message_function(message_body, routing_key):
    print(message_body.decode())


async def main(loop):
    connection = await connect_robust(RABBIT_CREDENTIALS, loop=loop)

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    exchange = await channel.declare_exchange(EXCHANGE_NAME, type=ExchangeType.DIRECT, durable=True)

    queue = await channel.declare_queue(QUEUE_NAME, durable=True)
    await queue.bind(exchange=exchange, routing_key=ROUTING_KEY)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process(reject_on_redelivered=True, ignore_processed=True):
                try:
                    await process_message_function(message.body, message.routing_key)
                except Exception as exc:
                    # logger.error(data="Couldn't process message", exc=exc)
                    message.nack(requeue=False)
                    continue

                message.ack()
                # logger.info(data="Message processed")
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
    loop.close()
```

question id: 2604fefe-158b-46c4-bd5d-2c21f7423cc



## Acknowledge system

### What is automatic anknowledgement mode?

With automatic acknowledgement mode a message is considered to be successfully delivered immediately after it is sent.
It might not made it to the consumer app or made it, but wasn't processed due to many reasons.

question id: cab8813d-fa03-4528-a47e-7804f29a993b


### What are cons of automatic acknowledgement mode in RabbitMQ?

- There are many chances that the message will be lost before consumer actually processes it - network failure,
consumer failure etc. Manually acknowledge the message after it was processed by the consumer is much more robust approach.

- Consumer can be flooded with the messages and prefetch won't help. 
  Manual acknowledgement mode is typically used with a bounded channel prefetch which limits the number of 
  outstanding ("in progress") deliveries on a channel. With 
automatic acknowledgements, however, there is no such limit by definition. Consumers therefore can be overwhelmed 
by the rate of deliveries, potentially accumulating a backlog in memory and running out of heap or getting their 
process terminated by the OS.

question id: 7be7889a-45d6-485e-9918-d4fc690b75ee


### What can you do with a message when you negatively acknowledge it?

You can requeue it (put again in the queue it came from) or totally drop it.
In aio_pika its `message.nack(requeue=True|False)`

When a message is requeued, it will be placed to its original position in its queue, if possible. 
If not (due to concurrent deliveries and acknowledgements from other consumers when multiple consumers share a queue), 
the message will be requeued to a position closer to queue head.

Requeued messages may be immediately ready for redelivery depending on their position in the queue and the prefetch 
value used by the channels with active consumers. This means that if all consumers requeue because they cannot process 
a delivery due to a transient condition, they will create a requeue/redelivery loop. Such loops can be costly in terms 
of network bandwidth and CPU resources. Consumer implementations can track the number of redeliveries and reject 
messages for good (discard them) or schedule requeueing after a delay.

https://www.rabbitmq.com/confirms.html

question id: 917b1b5f-6e4a-4b20-b51e-5b8ff7272233



## How to check what queues RabbitMQ has and how many messages are in them via console?

```
(docker exec -it your_rabbitmq_container_name) rabbitmqctl list_queues
```
question id: 


rabbitmqctl most useful commands
https://www.rabbitmq.com/rabbitmqctl.8.html