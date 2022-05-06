### What is Dutch National Flag problem?

Long story short: it's an algorithm that allows you to sort an array
of 3 unique elements (with 0 or many duplicates of each value) in
linear time using constant space.

It is a programming problem proposed by Edsger Dijkstra. 
The flag of the Netherlands consists of three colors: white, red, and blue.

The task is to arrange balls of white, red, and blue in such a way that balls
of the same color are placed together. For DNF (Dutch National Flag), 
we sort an array of 0, 1, and 2's in linear time that does not consume any 
extra space. 
  
We have to keep in mind that this algorithm can be implemented only on an 
array that has three unique elements.


It works like these:
You need to define three pointers:
low, mid = 0, 0
high = len(array) - 1

Traverse the array from start to end and mid is less than high. (Loop counter is i)
If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1
If the element is 1 then update mid = mid + 1
If the element is 2 then swap the element with the element at index high and update high = high – 1 and do not update mid as the swapped element is not processed

https://algodaily.com/challenges/dutch-national-flag-problem

question id: https://algodaily.com/challenges/dutch-national-flag-problem