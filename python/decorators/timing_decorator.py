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

