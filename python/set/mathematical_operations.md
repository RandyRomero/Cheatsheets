### What's the use of intersection? How to use it?

Intersection returns set of elements common for both sets


```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 & s2  # output {3}
```

You can use `&` operator or method `some_set.intersection(another_set)`

question id: 83e4aa87-611b-4499-8a9d-346f6cbb1e6a

### What's the use of union? How to use it?

Union of s1 and s2 is a set consisting of all elements in either set, but without duplicates.

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 | s2  # output {1, 2, 3, 4, 5}  note that there is only one 3
```

Set union can also be obtained with the `.union()` method. 

The `.union()` method will take any iterable as an argument, convert it to a set, 
and then perform the union.

question id: 519d1749-1532-45b7-bb1b-37bb4041e2ac


### What is the use of difference operator of set? How to use it?

`x1.difference(x2)` and `x1 - x2` return the set of all elements that are in `x1` but not in `x2`

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 - s2  # output {1, 2}
s2 - s1  # output {4, 5}
```

question id: 2ccb6bf7-edc4-4b55-9326-3048c0a1c635

### What is the use of symmetric difference operator of set? How to use it?

`x1.symmetric_difference(x2)` and `x1 ^ x2` return the set of all elements in either `x1` or `x2`, but not both

In other words, it is the opposite of intersection - returns only elements, that do not present in both of sets 
simultaneously

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1 ^ s2  # output {1, 2, 4, 5}
```

question id: 03c8ad74-9aff-4de8-81d5-8f55149e7695


### How to delete values from set that are in another set?

For example, you have a set A {1, 2, 3, 4, 5} and set B {3, 4, 5} and you want to remove from set
A items that are in set B. How to do it in one line?

answer

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5}

a.difference_update(b)

print(a)  # {1, 2}
```

question id: 672622c1-1000-42e8-98d1-b1c2b0b1db8d


### What's the difference between:

```python
a = {1, 2, 3, 4, 5}
b = {3, 4, 5}

a.difference_update(b)
# and 
a - b
# ?
```

answer

The first one will update set a, it will contain {1, 2}
The second one will return {1, 2}, a will be left as it was before = {1, 2, 3, 4, 5}

question id: b8f67d18-de70-44f8-9678-cdd8897ef3ac


### What will this return: {1, 2, 3} - {1, 2}

answer
{3}

question id: b0e6d356-c456-4060-a194-e4390e9a931d


### How to find difference between two sets?

For example, you have these sets:
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
```

How to find the difference?
answer

```python
x - y  # {'banana', 'cherry'}

# or

x.difference_update(y)
print(x)  # {'banana', 'cherry'}
```

question id: 861fcc0b-3d1a-4cf0-9b04-a9000eea32e7


### What is set.difference_update() method for?

It removes elements from set a that are also present in set b.
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)  # {'banana', 'cherry'}
```

question id: 1eb39c90-f034-4322-b0cd-d8adb7b9d187
