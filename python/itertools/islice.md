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

answer:
```python
lst = list(range(61))
n = 3
print(list((lst[i:i + n] for i in range(0, len(lst), n))))
```

question id: 