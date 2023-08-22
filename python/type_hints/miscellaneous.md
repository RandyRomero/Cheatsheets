### How to annotate a Callable? For example some of your functions returns the following function:

```python
def sum(a: int, b: int) -> int: 
    return a+b
```

What would be returning type of such a function?

answer

```python
import typing as tp

tp.Callable[[int, int], int]
```

where `[int, int]` are parameters passed to the function, and `int` is type of what is returned


question id: 1b40cbfa-30ff-4341-a3bc-6b480d7dc242


### How to annotate async function?

Which, for example, accepts two integers and returns one integer.

```python
import typing as tp

tp.Callable[[int, int], tp.Awaitable[int]]
```

where you can use any types instead of `int` - it is just for example

question id: 61799592-03f2-4694-8dd1-1c0ea9f1b8f7

### How to annotate generator?

```python
import typing as tp

tp.Generator[yield_type, send_type, return_type]
```

for example

```python
import typing as tp

def echo_round() -> tp.Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return 'Done'
```

"If your generator will only yield values, set the SendType and ReturnType to None" 

"Alternatively, annotate your generator as having a return type of either 
`Iterable[YieldType]` or `Iterator[YieldType]`:"

```python
import typing as tp

def infinite_stream(start: int) -> tp.Iterator[int]:
    while True:
        yield start
        start += 1
```

https://docs.python.org/3/library/typing.html#typing.Generator

question id: 97b5a2b9-bb73-4cce-84c7-1b5693e71f21


### What is `typing.TypeVar` for? Write an example

`typing.TypeVar` is used to ensure that the same type is used 
in multiple inputs or output arguments, like following:

```python
from typing import TypeVar, Dict
Key = TypeVar('Key')
Value = TypeVar('Value')

def lookup(input_dict: Dict[Key, Value], key_to_lookup: Key) -> Value:
    return input_dict[key_to_lookup]
```

This appears to be a trivial example at first, but these annotations require that the types of the keys in input 
dictionary are all the same, and they are required to match the type of the key_to_lookup argument. The dictionary 
values also must all be the same type, and the return type of the function must match that type.

The keys and values as a whole could be different types, and for any particular call to this function, they could be 
different (because Key and Value do not restrict the types), but for a given call, the dict must have the keys and the 
lookup key be all the same type, and the same for the values and the return type.

question id: 8b97b009-07c0-4dba-93a7-5dd1d32ea71c


### Tell us about typing.TypeVar that limit the types with an example

answer

If you create a new TypeVar and limit the types to `float` and `int`:
```python
import typing as tp

ADDEND = tp.TypeVar("ADDEND", str, int)

def sum(a: ADDEND, b: ADDEND) -> ADDEND:
	return a + b
```

This function requires that `a` and `b` either both be `str`, or both be `int`, and the same type must be returned. 
If `a` were a `str` and `b` were an `int`, the type checking should fail.

question id: ee66b122-8e5d-4228-bda5-3702a79a0d1b


### What's `bound` argument in typing.TypeVar?


```python
import typing as tp

class Shape:
    pass

A = tp.TypeVar("A", bound=Shape)
```

That means that A must be type or subtype of Shape

question id: 117a4ac1-e2a6-4add-84d3-e7e743004f1c
