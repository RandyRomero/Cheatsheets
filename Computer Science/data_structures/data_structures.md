### Why array is fast? 

answer

- because all items lie in memory right next to each other in one unbreakable sequence
- because you can get any element of array by index simply multiplying ordinal number by number of bytes that consumes
one item of this type of values that you have stored in this array. Like Unicode codepoints take 4 bytes, hence to get
the 4th byte means to get 16th to 19th items from your array

question id: 1f94cb75-f8e7-4cea-bd2d-82760f38fbf8


### What is queue?

Queue is a linear data structure with flexible size where you can take an element that you just enqueued only after taking all the elements that were put there before in order
they were put there before. 

You can only put something in the tail of a queue and remove an element from the head of the queue 

FIFO (first in first out).

Purpose: message queueing for example.

question id: 5632eea8-bc22-4f4c-b46c-d2f582d73d10


### What is stack? 

Stack is a linear data structure with flexible size where you can put and push elements only to the very end of the collection. 
So in order to get the earlist put element you have to pop all other elements.

LIFO (last in first out)

Purpose: We can see stack-like behavior with a redo-undo features at many places like editors, photoshop and forward and backward feature in web browsers

question id: 31e62b71-99fa-4648-b0b9-e256a29f9475



### What is deque?

Deque is an achronym for double ended queue

Dequeu is a linear data structure with flexible size
You can add or remove an item both from head and tail of the deque

question id: ecc0f886-8623-46cb-8290-9ca92d0f7e0c