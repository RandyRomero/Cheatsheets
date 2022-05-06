### What is k sorted array?

answer
A k sorted array is an array where each element is at most k distances away from its target position in the sorted array. 

Examples:
{3, 2, 1, 5, 6, 4}, k = 2 is k sorted array b because every element is at most 2 distance away
from its target position in the sorted array.

{13, 8, 10, 7, 15, 14, 12}, k = 3 is not a k sorted array because 13 is more than k = 3 distance away
from its target position in the sorted array. 

question id: 5170a7aa-d8a1-4458-ad8f-7803290572fd


### What does mean 'stable' sorting algorithm?

Stable sorting algorithms preserve the relative order of equal elements, 
while unstable sorting algorithms don’t. In other words, stable sorting 
maintains the position of two equals elements relative to one another.

question id: e5ff9f4e-de23-4e1d-b91c-8501c771e37b


### Does stability of a sortding algorithm matter?

answer:

When you need to sort a bunch of numbers, stability doesn't matter at all.
Order of duplicate numbers won't change anything.

However, there is another case. 
Long story short: if you need to sort not a bunch of integers,
but a bunch of tuples by integers (like [('Mike', 12), ('Lisa', 9)]) and you want to preserve
original order (if, e.g., they were sorted alphabetically), you need a stable sort or you
will ruin previous order.

Good explanation is here:
https://www.baeldung.com/cs/stable-sorting-algorithms#:~:text=Stable%20sorting%20algorithms%20preserve%20the,elements%20relative%20to%20one%20another.

question id: b2d4adc1-14f8-4da7-a4db-c5d90e587faf
