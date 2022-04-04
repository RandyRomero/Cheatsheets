### What is an Iterable?

Something that can be iterated (looped) over: iterator, sequences, lists, sets, files an so on
Basically, every object that implements `__iter()__` method.

question id: 6294615c-fea5-481a-ad3e-1358602e7bce



### What does `__iter()__` method do?

answer:

It returns an iterator

question id: ac0f0649-8f55-4180-aaf2-f758e6b8bd8c


### What is a Sequence? 

answer:

It is type of Iterable that can be indexed starting from 0 and ending with length-1

For example in Python sequences are list, tuple, string.
At the same type dict, set are iterables, but not sequences.

question id: 553df14a-6790-4129-9080-a6f6acd723f2


### What is `iter()`?

answer:

It's a built-in Python function that takes an iterable or callable as 
an argument and returns object which can be iterated one element at a time - an iterator.

https://www.programiz.com/python-programming/methods/built-in/iter

question id: 5a928d2a-f7b4-4c6a-a255-a281d3aacb6e


### What can we do with an iterator?

answer:

The only thing that we can do with iterator is to take next item from it
with built-in `next()` function like.

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
next(iterator)
# 1
next(iterator)
# 2
next(iterator)
# 3
next(iterator)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

question id: e033913a-73cc-40bc-89ad-ea8b8a13f1cc


### What is an Iterator in Python?

answer:

Iterator is an iterface that let's us go through the elements of different iterables in a similar fashion without loading 
these elements in memory all at once.

In Python, an iterator is an object with the methods __iter__() and __next__(). 

And __next__() should raise `StopIteration` exception if there is no more values to get through. 
And __iter__() in iterator must return `self` (it means the iterator itself).

Note that collections.abc.AsyncIterator tests for __aiter__ and __anext__ methods. This is a new addition in 3.6.

question id: 7f948a0a-b04a-4382-b031-7c00ce2a9c39


### What are main properties of an Iterator in Python? (6)

answer:

- iterator has a state which it uses to remember where it is during iteration
- iterator can't be reset and they can't go back
- iterators are subset of iterables
- iterator doesn't know it's length (while some iterables know)
- iterator can't be indexed
- iterators are lazy iterables (allows us to save memory)

question id: 9a84bb52-c79e-411e-aa21-24dd64c8b7eb


### Why not all iterables are iterators?

answer:

Because iterators cannot be indexed and they don't now it's length. S
ome iterables (sequences like list, for example) can be indexed and now its length.

question id: 6de1b7cc-5c70-4485-b8c9-a9e231109d0d
  

### What will it give us?


```python
numbers = [1, 2, 3]
iterator = iter(numbers)
iter(iterator) # ?
```

answer:

Iterators return themselves, so:

```python
numbers = [1, 2, 3]
iterator = iter(numbers)
iterator2 = iter(iterator)
iteraror is iterator2
True
```

question id: 71c3931a-79bc-4601-aebd-670d9c933e8d


### Write a function similar to of itertools.islice()

Write a function that takes any iterable (list, TextIOWrapper, etc) and returns a new iterable that will return values 
of the given iterable from 0 to the n-th one.

It should be lazy iterable (not load all results to the memory at once)

For example:
```python
def islice(itrbl, stop):
    # your code here

with open("whatever", "r") as infile:
    first_three_lines = islice(infile, 3)
    print(first_three_lines)
```

answer:
```python
import typing as tp

VALUE = tp.TypeVar("VALUE")

def islice(itrbl : VALUE, stop: int) -> tp.Iterator[VALUE]:
    for i, item in enumerate(itrbl):
        if i >= stop:
            return
        yield item
```

question id: 4bcf717b-df8c-4471-917a-864c3668778b


### Why `itertools.islice()` is faster than if you write it yourself?

I guess because `itertools.islice()` is written in C

question id: 6f6ef78a-119b-4ff8-a1f1-7fda41b66e5c


### How to write `more_itertools.chunked()` as a class?

Write a class that takes an iterable (list, TextIOWrapper etc.) and returns an iterator that return a chunk of iterable 
values at each iteration as a list of values

For example:
```python
class Chunked:
    # your code here


with open("whatever", "r") as infile:
    for three_lines in Chunked(infile, 3):
        save_to_another_file(three_lines)
```

answer:
```python
import typing as tp

from itertools import islice

VALUE = tp.TypeVar("VALUE")

class Chunked:
    """Divides given iterable by chunks lazily."""

    def __init__(self, iterable: tp.Iterable[VALUE], chunk_size: int):
        """Init."""
        # We need to get an iterator from given iterable to save the state
        # traversing given iterable
        self.iterable = iter(iterable)
        self.chunk_size = chunk_size

    def __iter__(self) -> "Chunked":
        """Returns itself."""
        return self

    def __next__(self) -> tp.List[VALUE]:
        """Return a list with n values from the given iterable."""
        result = list(islice(self.iterable, self.chunk_size))
        if not result:
            raise StopIteration
        return result
```

question id: 228024d2-fed2-4b1a-b802-5487b58f49c4


### How to write `more_itertools.chunked()` as a function?

Write a function that takes an iterable (list, TextIOWrapper etc.) and returns an iterator that return a chunk of iterable 
values at each iteration as a list of values

For example:
```python
from itertools import islice

lst = list(range(350))
chunk_size = 3

def chunked():
    pass

for twelve_items in chunked(lst, chunk_size):
    print(twelve_items)

# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]
# [9, 10, 11]
# [12, 13, 14]
# [15, 16, 17]
# [18, 19, 20]
# and so on
```

answer
```python
import typing as tp

from itertools import islice

VALUE = tp.TypeVar("VALUE")

def my_chunked(iterable: tp.Iterable[VALUE], chunk_size: int) -> tp.Iterator[tp.List[VALUE]]:
    """Returns one chunk of the given iterable at a time"""
    # we need to be sure that we store an iterator in closure in order to keep
    # the state of iteration
    iterable = iter(iterable)
    def wrapper():
        # we need a closure to save state of iterator, otherwise it will
        # always start over and return first n elements on every call
        return list(islice(iterable, chunk_size))
    # The second argument of iter is what will return on stop iteration.
    return iter(wrapper, [])
```

question id: 24f305fb-2a39-47b5-af8c-d3a4edfa9f21


### How to split you Sequence by chunks of given size?

```python
lst = list(range(61))
n = 3

for chunk in ...:
    print(chunk) # [1, 2, 3]  
```

answer
```python
numbers = list(range(61))
chunk_size = 3
print(list((numbers[i:i + chunk_size] for i in range(0, len(numbers), chunk_size))))
```

question id: bf2a9e82-b428-442b-9ec8-28214c87b352