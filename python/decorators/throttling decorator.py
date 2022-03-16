# Like Throttle in DRF which returns an error if you go to the same endpoint
# more than N times per N seconds/minutes/hours etc

from functools import wraps
from time import perf_counter, sleep

class TooManyCalls(Exception):
    def __init__(self, timeout: float, message: str = "You've already made too many calls. Chill for at least {:.2} seconds"):
        self.timeout = timeout
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.timeout)


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
                raise TooManyCalls(timeout=timeout-time_diff)

            return func(*args, **kwargs)

        return inner_wrapper
    return outer_wrapper


@throttle(timeout=1, attempts=2)
def say_whee():
    print('wheee')


say_whee()
say_whee()
sleep(1.5)
say_whee()
say_whee()


# old crap

#
# def throttle(times: float, seconds: float):
#     if times <= 0 or seconds <= 0:
#         raise ValueError("times and seconds arguments should be more than 0.0")
#     def outer_wrapper(func):
#         call_number = 0
#         start_time = 0.0
#         def inner_wrapper(*args, **kwargs):
#             nonlocal call_number
#             nonlocal start_time
#             if call_number == 0:
#                 start_time = time()
#
#             call_number += 1
#             if call_number > times and time() - start_time < seconds:
#                 raise TooManyCalls(timeout=(seconds - (time() - start_time)))
#             if time() - start_time > seconds:
#                 start_time = 0.0
#                 call_number = 0
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return outer_wrapper

#
# def throttle(times: float, seconds: float):
#
#     if times <= 0 or seconds <= 0:
#         raise ValueError("times and seconds arguments should be more than 0.0")
#
#     def outer_wrapper(func):
#         call_number = 0
#         last_invoked = 0.0
#         def inner_wrapper(*args, **kwargs):
#             nonlocal call_number
#             nonlocal last_invoked
#
#             if call_number == 0:
#                 last_invoked = time()
#
#             call_number += 1
#             elapsed_time = time() - last_invoked
#
#             if call_number > times and elapsed_time < seconds:
#                 raise TooManyCalls(timeout=seconds - elapsed_time)
#             if elapsed_time > seconds:
#                 call_number = 0
#                 last_invoked = time()
#
#             return func(*args, **kwargs)
#         return inner_wrapper
#     return outer_wrapper