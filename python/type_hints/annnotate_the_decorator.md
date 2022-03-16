### You have the following retry-decorator. Add type hints to it and check it with mypy:

```python
from functools import wraps
from time import sleep


def retry(*exceptions, attempts, timeout=1):
    def outer_wrapper(func):
        counter = 0
        wraps(func)
        def inner_wrapper(*args, **kwargs):
            nonlocal counter
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    counter += 1
                    print(f"{counter=}")
                    if counter >= attempts:
                        raise err
                    sleep(timeout)
        return inner_wrapper
    return outer_wrapper


@retry(KeyError, attempts=5)
def say_whee():
    cache = {}
    print(cache["some_nonexisting_key"])


say_whee()
```

answer

```python
import typing as tp

from functools import wraps
from time import sleep

FUNC = tp.TypeVar("FUNC", bound=tp.Callable[..., tp.Any])

def retry(*exceptions: tp.Type[Exception], attempts: int, timeout: float = 1) -> tp.Callable[[FUNC], FUNC]:
    def outer_wrapper(func: FUNC) -> FUNC:
        counter = 0
        @wraps(func)
        def inner_wrapper(*args, **kwargs):
            nonlocal counter
            for i in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as err:
                    counter += 1
                    print(f"{counter=}")
                    if counter >= attempts:
                        raise err
                    sleep(timeout)
        return tp.cast(FUNC, inner_wrapper)
    return outer_wrapper


@retry(KeyError, attempts=5)
def say_whee():
    cache = {}
    print(cache["some_nonexisting_key"])


say_whee()
```

Additional questions: 

1. Why `tp.Type[Exception]` instead of `Exception`?

    Because we pass to the function not an instance of KeyError, but its class. 
    
2. Why don't you annotate `wrapper()`? 
    
    "...note that the wrapper() function is not type-checked. Wrapper functions
    are typically small enough that this is not a big problem. This is also the 
    reason for the cast() call in the return statement in my_decorator(). 
    See Casts and type assertions."

    https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators
    

question id: 3a1b7276-f333-4a56-94bb-4f608ba107af