from functools import wraps
from time import sleep


def retry(*exceptions, attempts, backoff=1):
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
                    sleep(backoff)

        return inner_wrapper

    return outer_wrapper


@retry(KeyError, attempts=5)
def say_whee():
    cache = {}
    print(cache["some_nonexisting_key"])


say_whee()
