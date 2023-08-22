import pickle
from functools import wraps
from time import sleep


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (pickle.dumps(args), pickle.dumps(kwargs))
        if key in cache:
            return cache[key]
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper


@memoize
def sum(a, b):
    sleep(3)  # as if the function is executing fow a while
    return a + b


print(sum(2, 2))
print(sum(2, 2))
print(sum(2, 5))
print(sum(2, 2))
