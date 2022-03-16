https://www.rabbitmq.com/tutorials/tutorial-one-python.html


### What is RabbitMQ? 

 Advanced Message Queuing Protocol (AMQP).

RabbitMQ is a message broker: it accepts and forwards messages. 

You can think about it as a post office: when you put the mail that you want posting in a post box, 
you can be sure that the letter carrier will eventually deliver the mail to your recipient. 
In this analogy, RabbitMQ is a post box, a post office, and a letter carrier.

question id: 


Some RabbitMQ argot:
- program that sends messages is a producer

message can only be stored inside a queue.
A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer.

Consuming has a similar meaning to receiving. A consumer is a program that mostly waits to receive messages

Note that the producer, consumer, and broker do not have to reside on the same host; indeed in most applications they don't. An application can be both a producer and consumer, too.

before sending we need to make sure the recipient queue exists. If we send a message to non-existing location, RabbitMQ will just drop the message.

Creating a queue using queue_declare is idempotent ‒ we can run the command as many times as we like, and only one will be created.


A producer is a user application that sends messages.
A queue is a buffer that stores messages.
A consumer is a user application that receives messages.

There are three AMQP entities in RabbitMQ:
- Exchange
- Binding
- Queues

Messages published by a publisher are first received by the Exchange in RabbitMQ, then Exchanges will distribute message copies to Queues. 
To send appropriate messages to the appropriate queues, rules called Bindings are used.

The core idea in the messaging model in RabbitMQ is that the producer never sends any messages directly to a queue. 
Actually, quite often the producer doesn't even know if a message will be delivered to any queue at all.

Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. 
On one side it receives messages from producers and the other side it pushes them to queues. 
The exchange must know exactly what to do with a message it receives. 
Should it be appended to a particular queue? Should it be appended to many queues? 
Or should it get discarded. The rules for that are defined by the exchange type.


### How to send a message?

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

question id: 

What type of messages? Typically binary


### What type could the messages be?

question id: 


### Why do we declare queues each time we start a producer/consumer or whatever? 

You may ask why we declare the queue again ‒ we have already declared it in our previous code. 
We could avoid that if we were sure that the queue already exists. For example if send.py program was run before. 
But we're not yet sure which program to run first. 
In such cases it's a good practice to repeat declaring the queue in both programs.

question id: 


