### What is the difference between `yield` and `yield from`?

On the one hand, `yield from` can consume the generator iteratively, like this:
```python
def get_squares(num):
    """Example of a generator."""
    for i in range(num):
        yield i**2

def consume_generator_with_yield_from(gen):
    yield from gen
    
    """Equivalent of
       
        for i in gen:
            yield i
    """
```

on the other hand, it establishes a two-way channel to connect the outermost caller with the innermost sub generator, 
and automatically handles the exception and receives the value returned by the sub generator.

So, if you have a chain of coroutines, it will be very taxing to switch context consecutively from one to another.
yield from lets Python switch context directly to generator of interest. 

*context - state of generator function, state of variables of this generator function, that is saved between yield 
calls.

https://developpaper.com/two-differences-between-python-coroutine-and-go-coroutine/
https://www.sobyte.net/post/2022-01/python-asyncio/

yield from let switch the context directly 
https://stackoverflow.com/a/26109157/6337994

question id: 676f886d-ef36-468a-8382-03da89076aca


### What would be the output?

```python
def test_fun1():
    yield 1
    return 2

gen = test_fun1()
try:
    gen.send(None)
    gen.send(None)
except StopIteration as e:
    print(e.value)
```

answer
2

To get the return value of the return, either catch the exception with a try statement or get the value with 
a yield from expression.

https://www.sobyte.net/post/2022-01/python-asyncio/

question id: 7ac2a373-fc7d-48ed-9ab4-b51c36d9175d


### How to make a generator return None before it is exhausted?

```python
def a_generator(strings: list[str]) -> str:
    for string in strings:
        for letter in string:
            yield letter
```

How to return None before it raises StopIteration and why it could be needed?

answer:
You just need to explicitly yield None right after the loop

```python
def a_generator(strings: list[str]) -> str:
    for string in strings:
        for letter in string:
            yield letter
    yield None
```

It could be needed it you iterate through a zip() of two generators and they can
be of different length. You won't even know it that one is shorter than the other.
However, if None is an expected value, you can use another trick:

```python
from itertools import zip_longest

for whatever in zip_longest(iteratble1, iterable2, fillvalue=""):
    pass
```

question id: c1677e44-79c1-4420-9798-dd5e8d070332


### What would be the output?

```python
def a_generator(strings: list[str]) -> str:
    for string in strings:
        for letter in string:
            yield letter
    yield None

print(list(a_generator(["abc", "d"])))
```

answer:

['a', 'b', 'c', 'd', None]

question id: f433d501-ff2b-4a53-9e88-a2e590bff5b1