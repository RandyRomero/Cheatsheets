### What is JSON? 

JSON is a lightweight format for storing and transporting data
(текстовый формат обмена данными)

question id: ad0a4d34-6c5f-4a94-b4f6-3007b5e15c4e


### What does JSON stand for?

JavaScript Object Notation

question id: 7bc6e17f-1b56-45bd-844a-de7bc0ef9a0f


### What is serialization?

Serialization is the process of turning an object in memory into a stream of bytes so you 
can do stuff like store it on disk or send it over the network.

What does it mean and why do we need it?

In a programming languages data structures are not necessarily stored
in one contiguous part of memory. For example, let's take liked list: it's values
can be spread all over the operating memory. To serialize it to file means to put all
the values together as one stream of bytes.


If you think Python's list looks exactly like this in operating 
memory - [1, 2, 3, 4, 5] - you are wrong. It's an object with different 
information: about it's type, ref count, it's size, with the pointer to where 
the actual array in the memory is. And even the actual array doesn't 
store your values, it just stores pointer to memory 
cells for every value. Do you need all this crap when you want to 
transfer [1, 2, 3, 4, 5] through the network to another service? Absolutely not. 
So to convert all this machinery and metadata that Python
list is - you need to serialize it to simple [1, 2, 3, 4, 5].

So, serialization is the process of converting data and data structures of
language to format that can be transmitted.

question id: 3e7cdf20-3904-489e-bd51-3773012ecd73


### What is deserialization? 

Deserialization is turning a stream of bytes into an object in memory.
What's that? For example, you have a string like this `[1, 2, 3, 4, 5]`.
To be able to use it as a list of integers in, for example, Python, 
you need to deserialize it. That means to parse the string and construct
a list object in operationg memory. And Python list object in memory is
more complicated that plain and simple `[1, 2, 3, 4, 5]`.


question id: f5e3219a-21f8-4ded-8be0-e78bc823d27d


### What are JSON Types?

Strings: "Hello World"
Numbers (integers and floats): 10 17 1.7
Booleans: true false
null: null
Arrays: [1, 2, 3], ["Hello", "World"]
Objects: {"key": "value", "age": 30} 

question id: 30d6c696-140d-4795-a8df-53410848a2fa