### What is itertools.islice for? 

answer:

It creates an iterator that iterates over the EXISTING list(s)

Example:
```python
import itertools

data1 = range(10)

# This creates a NEW list
data1[2:5]

# This creates an iterator that iterates over the EXISTING list
itertools.islice(data1, 2, 5)
```

question id: c54f8a55-a40c-4f4e-9beb-58cb1e13992f



### How to iterate through two or more lists at once without creating a new list from them?

answer:

```python
import itertools

data2 = [1, 2, 3]
data3 = [4, 5, 6]

# This creates a NEW list
data2 + data3

# This creates an iterator that iterates over the EXISTING lists
itertools.chain(data2, data3)
```

question id: ac7d18eb-f897-4214-81ca-d8b63cc9efaa


### How to get one chuck at a time from your list?

For example, you are going through millions of elements and want to do something with every 100 000 of them.
You can you for loop and module operator to divide elements to chunks, but if the last chunk is not full, elements
will be lost. How to split list or tuple to chunks properly?

Provide two ways

answer:
```python
foo = list(range(100))

chunk_size = 10

# manual
for i in range(1, len(foo), chunk_size):
    print(foo[i:i+chunk_size])  # you chunk of data
# the downside - you create a new list size of chunk_size every time

# with more_itertools.ichucked
from more_itertools import ichunked

for chunk in ichunked(foo, chunk_size):
    print(type(chunk))

# it will return iterables instead of lists, so you will spare some memore avoiding list creating
```

question id: 59b76b7e-1839-4d86-b00d-2b14b49b8c92