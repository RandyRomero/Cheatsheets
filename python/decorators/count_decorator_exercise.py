from functools import wraps

def call_counter(func):
    counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
