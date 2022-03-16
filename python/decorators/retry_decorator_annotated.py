import typing as tp
from functools import wraps
from time import sleep


FUNC = tp.TypeVar("FUNC", bound=tp.Callable[..., tp.Any])

def retry(*exceptions: tp.Type[Exception], attempts: int, timeout: int = 1) -> tp.Callable[[FUNC], FUNC]:
    def outer_wrapper(func) -> FUNC:
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
        return tp.cast(FUNC, inner_wrapper)
    return outer_wrapper


@retry(KeyError, attempts=5)
def say_whee():
    cache = {}
    print(cache["some_nonexisting_key"])


say_whee()