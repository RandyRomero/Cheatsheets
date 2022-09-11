### What is a decorator in Python?

A decorator is any callable Python object that is used to extend the behavior of a function or method without 
explicitly modifying it

question id: 10b1242c-d863-41de-91d4-3d82f4eb094a


### Write a simple decorator, decorate and call given function with it and without using @

There is your function that you have to decorate:
```python
def say_whee():
    print("Whee!")
```

answer

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()

# > Something is happening before the function is called.
# > Whee!
# > Something is happening after the function is called.
```

question id: 040d2d70-37c8-4f58-b278-b02457701ea9


### Write a simple decorator, decorate and call given function with it and using @

There is your function that you have to decorate:
```python
def say_whee():
    print("Whee!")
```

answer

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# > Something is happening before the function is called.
# > Whee!
# > Something is happening after the function is called.
```

question id: 7250dd97-e280-4fbf-a996-f734af4a0bb8


### What does @my_decorator syntax represent?

```python
some_function = my_decorator(some_function)
```

question id: 40b5d67a-ffb2-461b-b04c-9fff3fca8c67


### What does @my_decorator(some_arg='some_value') syntax represent?

```python
some_function = my_decorator(some_arg='some_value')(some_function)
```

question id: 802d3642-7996-4af4-b2f4-7c292c42465d


### How to write a decorator for an asynchronous function with type annotations?

For example, you have some async function
```python
import asyncio

async def foo():
    await asyncio.sleep(1)
```

How to write a decorator for this func?

answer

```python
import asyncio
import typing as tp
from functools import wraps


def deco(func: tp.Callable[..., tp.Awaitable[T]]) -> tp.Callable[..., tp.Awaitable[T]]:
    @wraps(func)
    @tp.no_type_check
    async def wrapper(*args, **kwargs):
        # do_something
        return await func(*args, **kwargs)
    return wrapper

@deco    
async def foo():
    await asyncio.sleep(1)
```

question id: 510b188c-f255-4247-8569-d306606ccc02


### You have a decorator, but it doesn't let you to pass arguments to the decorated function. How to fix it?

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hi, {name}")

greet("Homer")
# error
```

answer

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hi, {name}")

greet("Homer")
# Hi, Homer!
```

question id: 9f579baf-16ca-4d78-88be-de0c495e8d53


### How to preserve `function.__name__` and documentation for decorated function?

Usually if you decorate a function and then try to introspect it, you will get the name and documentation of your
decorator. What do you need to avoid it?

answer
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return my_wrapper

@my_decorator
def whatever():
    pass

whatever.__name__
# whatever
```

question id: 1089c044-4c97-40b1-9198-d79f07a95c0b

### If you have several decorators stacked together above a function, in which order will they apply?

example
```python
@debug
@time
@authanticate
def my_func():
    pass
```

answer

In the order they are listed, top-down.

question id: c165bece-c7d0-4585-9b51-0fd82662520a


### Write a decorator then accepts arguments

```python
from functools import wraps

def my_decorator(my_arg):
    def outer_wrapper(func):
        wraps(func)
        def inner_wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return inner_wrapper
    return outer_wrapper
```

question id: f0155034-90b6-48dc-be36-552abd6f3fb8


### Make a decorator that counts how many times given function was called

answer

```python
from functools import wraps

def decorator(func):
    counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"{func.__name__} was called {counter} times.")
        return func(*args, **kwargs)
    return wrapper
    
@decorator
def foo():
    print("foo has run")
    
    
foo()
foo()
foo()

# foo was called 1 times.
# foo has run
# foo was called 2 times.
# foo has run
# foo was called 3 times.
# foo has run
```

question id: 8eae0d9c-71cb-4f27-b486-924507edb5f4


### Make a class-based decorator that counts how many times given function was called

```python
import functools

class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def say_whee():
    print("Whee!")
```

question id: aa60f844-a790-4495-9c9f-306f31decfdf


### Can you decorate a class?

Yes.

Example:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do_something
        return func(*args, **kwargs)
    return wrapper

@my_decorator
class MyClass():
    pass # let's imagine there is some logic inside this class

my_class = MyClass() # that's where the decorator is applied
```

question id: 2df59bf9-094a-4f9f-a9ce-8cb37279b6b6


### If you decorate a class, when the decorator are called exactly?

When you make a new instance of a class

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # do_something
        return func(*args, **kwargs)
    return wrapper

@my_decorator
class MyClass():
    pass # let's imagine there is some logic inside this class

my_class = MyClass() # that's where the decorator is applied
```

question id: 257a7497-ff0f-4e94-bc3c-148fb3f0b798


### Name some examples of useful real-world decorator

- retry decorator: if function is failed, try again several times (useful in web)   
        https://pypi.org/project/retrying/
- caching decorator: caches the result of a very taxing function by the input
https://realpython.com/lru-cache-python/
- throttle decorator: impose the limit of how many times the function can be called
- descriptive decorators: add the decorated function or class to some sort of collection
- wrapping decorators: do things around function call, do not modify the behavior of a function 

question id: cfb45439-181e-4a04-9450-8cfa43c48ca3

### Is it possible to write a decorator that can accept arguments only if they are given?

Yeeees.. 

```python
from functools import wraps

def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper

    if _func is None:
        return decorator_repeat
    return decorator_repeat(_func)

@repeat(num_times=10)
def say_whee():
    print('wheee')

say_whee()
```

https://realpython.com/primer-on-python-decorators/#both-please-but-never-mind-the-bread

question id: 91abd37e-795e-496d-9b64-d7889b6e50d5

### Write a decorator that measures the time of execution of some function

```python
from functools import wraps
from time import perf_counter

def timing(func):
    wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        print(f"{perf_counter() - start_time:0.10f}")
        return result

    return wrapper

@timing
def say_whee():
    print("wheeee!")

say_whee()
```

question id: 8a66fc67-e0c0-4315-ba47-d3586a67f4f5


### Describe how throttling decorator in Python works

Like Throttle in DRF which returns an error if you go to the same endpoint 
more than N times per N seconds/minutes/hours etc

0. You need a decorator that takes arguments: timeout and max number of calls within this timeout
1. Define call counter and variable that saves point in time when timer should start.
    For example, your function was called at 14:33:00, so until 14:33:05 you cannot make more than given number of calls
2. At each call you have to increase call counter by one
3. At each call you have to measure how many time passed since the first call in a row
4. If there is more time passed than the time limit: 
   - reset the call_counter, 
   - reset point in time when the function was called for the first time in a row
   - call decorated function with arguments
5. If there call counter exceed the limit of attemtps - raise an error
6. If time that passed have not exceed the limit and call_counter has not exceed the limit - just call
   the decorated function with arguments

question id: 13bec20b-f5f9-4384-a720-6911066e0179


### Write an example of a throttling decorator

Like Throttle in DRF which returns an error if you go to the same endpoint 
more than N times per N seconds/minutes/hours etc

Take this custom error to use in your throttle decorator

```python
class TooManyCalls(Exception):
    def __init__(self, timeout: float, message: str = "You've already made too many calls. Chill for at least {:.2} seconds"):
        self.timeout = timeout
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.timeout)
```

answer:

```python
from functools import wraps
from time import perf_counter, sleep

# custom error
class TooManyCalls(Exception):
    def __init__(self, timeout: float, message: str = "You've already made too many calls. Chill for at least {:.2} seconds"):
        self.timeout = timeout
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.timeout)

#decorator
def throttle(timeout, attempts):
    """Decorator that return error if the decorated function is called too many times."""
    if timeout <= 0 or attempts <= 0:
        raise ValueError("times and seconds arguments should be more than 0.0")

    def outer_wrapper(func):
        counter = 0
        last_called = 0.0
        wraps(func)
        def inner_wrapper(*args, **kwargs):
            nonlocal counter
            nonlocal last_called

            counter += 1

            time_diff = perf_counter() - last_called
            if time_diff > timeout:
                counter = 1
                last_called = perf_counter()
                return func(*args, **kwargs)

            if counter > attempts:
                raise TooManyCalls(timeout - time_diff)

            return func(*args, **kwargs)

        return inner_wrapper
    return outer_wrapper


@throttle(timeout=1, attempts=5)
def say_whee():
    print('wheee')


say_whee()
say_whee()
sleep(1.5)
say_whee()
say_whee()
```

question id: 581f45cb-84b4-43b5-b207-d1deae7ce6f6



### Write an example of a memoize/caching decorator

answer

```python
import pickle
from functools import wraps
from time import sleep


def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper (*args, **kwargs):
        key = (pickle.dumps(args), pickle.dumps(kwargs))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper

@memoize
def get_fib(n):
    if n <= 2:
        return 1

    return get_fib(n - 1) + get_fib(n - 2) 

print(get_fib(50))  # will take a lot of time without memoization
```

question id: cc497cdb-5540-4c7f-856a-ef96568b3916


### Write an example of retry decorator

```python
from time import sleep

def retry(*exceptions: Exception, times: int, backoff: float = 1):
    def outer_wrapper(func):
        counter = 0
        def inner_wrapper(*args, **kwargs):
            nonlocal counter
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    counter += 1
                    print(f"{counter=}")
                    if counter >= times:
                        raise err
                    sleep(backoff)
        return inner_wrapper
    return outer_wrapper


@retry(KeyError, times=5)
def say_whee():
    cache = {}
    print(cache["some_nonexisting_key"])


say_whee()
```

question id: 3e9535a0-405a-4177-bcd8-8b8c080841e5


### memoize-decorator? 