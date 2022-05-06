https://www.techinterviewhandbook.org/algorithms/array/

### What is an array?

Array is a linear data structure that holds values of the same type at contiguous memory locations.
Each element also has its own index, which is used to access the element.

question id: b875f917-ff48-4853-8939-e5fe90c008b5


### Why is array so useful and ubiquitous?

- you can store multiple values at a time with one single variable name
- you can access values pretty fast - (O(1)) - if you know their index

question id: 3008c056-7ccf-4503-a09f-855e8863c378


### What are downsides of an array as a data structure? (2)

- addition and removal of elements into/from the middle an array is slow 
because they remaining elements need to be shifted to accommodate the new/missing element.
- arrays are usually of a fixed size. So if you want to add more elements, you have to allocate new array that will
all elements, and copy old element to it as well as put new ones

question id: 7349eedd-1d8e-417b-9915-0c0f2329544c


### What is time complexity of adding elements to a fixed-size array?

Arrays are usually of a fixed size. So if you want to add more elements, 
you have to allocate new array and copy old elements to it as well as put new ones.
The act of creating a new array and transferring elements over takes O(n) time.

question id: 7ecf6bfa-d0e9-4c80-a914-dba71c72fc15


### What is time complexity of accessing an element within an array and why? 

It is O(1)

Array holds values of the same type at contiguous memory locations. For each
element in an array the same amout of memory in bytes are allocated. In other
words, there is the same amout of memory reveserved for every element. Knowing
this, and knowing the index of the value of interest, we can just multiply
the index by amount of bytes that is needed for storing one element and therefore get the
address of a cell in memory where the element is.

For example, in our array one element takes 4 bytes. And we are looking
for an element under index 10. We multiple 4 by 10 and get the 40 - that
means that we can jump to the 40 byte in a row to get our element.

question id: 01627704-96db-468b-81b1-5c9b90f68471


### What is a subarray?

https://www.techinterviewhandbook.org/algorithms/array/#common-terms

A range of contiguous values within an array.

Example: 
given an array [2, 3, 6, 1, 5, 4], [3, 6, 1] is a subarray while [3, 1, 5] is not a subarray.

question id: 775a1a76-df55-4e8e-9bc4-903b0aeccfb6


### What is a subsequence?

A sequence that can be derived from the given sequence by deleting some or 
no elements without changing the order of the remaining elements.

Example: given an array [2, 3, 6, 1, 5, 4], [3, 1, 5] is a subsequence but [3, 5, 1] is not a subsequence.

question id: c1787f85-6d31-4393-b709-53141618f0e7


### What is time complexity of searching an element in an array?

O(n) if it is not sorted
O(log(n)) if it is sorted

question id: 4a0c3abe-7198-45e8-b9b4-cd8088d575b2


### What is time complexity of inserting an element in the array?

O(1) if you insert in the end of the array
O(n) if you insert in the middle or beginning of the array

It also can take reallocation of an array and copy of all its elements if you try
to add element to the array that is already or almost full

question id: 7597b346-5531-482e-beb7-a03da3d52217


### What is time complexity of removing an element from an array?

O(1) if you remove the last element
O(n) if you remove element from the middle or from the beginning

question id: 964ee8d4-d83a-44e6-bc89-259c536fb72c


### What is Sliding Window Technique?

Sliding Window Technique is a computational technique which aims to reduce 
the use of nested loop and replace it with a single loop, thereby 
reducing the time complexity.

In this technique two pointers usually move in the same direction will 
never overtake each other. This ensures that each value is only visited 
at most twice and the time complexity is still O(n).

question id: 