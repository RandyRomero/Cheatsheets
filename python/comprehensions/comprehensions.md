### How to flatten this tuple ((1,2,3), (4,5,6), (7,8,9)) via comprehension?

```python
matrix = ((1,2,3), (4,5,6), (7,8,9))

tuple(number for nested_tuple in matrix for number in nested_tuple)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
```

question id: 02e420bb-6354-4daa-ae2c-5fbae0200428


### Calculate the price after tax for a list of transactions

Given:
```python
transactions = [1.09, 23.56, 57.84, 4.56, 6.78]

TAX_RATE = .08

def get_price_with_tax(txn):
    return txn * (1 + TAX_RATE)
```

Expected output:
```python
[1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```
 
There are at least two ways of doing it. 

answer:

via map():
```python
final_prices = map(get_price_with_tax, txns)
list(final_prices) # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

via list comprehension:
```python
final_prices = [get_price_with_tax(i) for i in txns]
final_prices  # [1.1772000000000002, 25.4448, 62.467200000000005, 4.9248, 7.322400000000001]
```

question id: 480290d1-0bfa-4ca9-aaff-bff23d258b33


### Change negative values with 0

You have a list of prices. Create a new list where negative prices are substituted with 0.

```python
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
```
expected output: [1.25, 0, 10.22, 3.78, 0, 1.16]

answer:
```python
original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
prices  # [1.25, 0, 10.22, 3.78, 0, 1.16]
```

question id: 41ba0a05-19d1-46e8-a8f7-5427477b45f6


### What is the general syntax for set comprehension?

```python
{x for x in some_iterable}
```

question id: 115891fe-9da5-4629-8126-52ce1fce55c2


### Create a dictionary where a key is a number and its value is the square of the number

numbers = [1, 2, 3, 4, 5, 6]

answer
```python
{n: n**2 for n in numbers}
``` 

question id: 928fb020-cb9a-4abf-a45b-de32ba5968bb


### How to create a matrix like this? 

```python
[
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4],
    [0, 1, 2, 3, 4]
]
```

answer
```python
[[i for i in range(5)] for _ in range(6)]
```

question id: 10bd6577-4cda-44cf-9611-ed6ad5cf8c6e



### What would be the output?

```python
field = "whatever"


class Work:

    def __init__(self, whatever):
        self.whatever = whatever


works = [Work(i) for i in range(3)]

params = {field: [getattr(work, field) for work in works]}

print(params) # ? 
```

answer
```python
{'whatever': [0, 1, 2]}
```

question id: f598e7bc-2677-4857-87dc-fe27fde58115


### When list comprehension creates a list for the result, does it allocate the corresponding array of the whole 
length of the iterable? Or does it work as a usual list.append() which relocates an array everytime when the current 
array is almost full?

answer:

It could, but it doesn't. The only thing why it's sometimes faster than for loop it is because it doesn't call
.append() all the time. Instead, it uses LIST_APPEND bytecode directly.

There were proposals to make this optimization, but they were rejected. 
This is one of them: https://bugs.python.org/issue36551

Though there is one place where this preallocation takes place: when you extend your list from another iterable.
https://github.com/python/cpython/blob/main/Objects/listobject.c#L934

question id: d6ff7aeb-746b-42a7-a841-60f3893d5735