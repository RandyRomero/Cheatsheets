### How to start a few copies of the same function but with different arguments in separate threads?

Let's say, you want to make 1000 api calls, but with different ids using threads.

For example, you have a `http_post` function that takes car_id as a keyword argument.
And a list of many many car ids `car_ids`. How to call this `http_post` function
simultaneously in separate threads? How to get results? How to catch errors?

answer:

```python
import concurrent
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers) as executor:
    # load workers with tasks
    # note: it's better to use for loop with a condition to stop adding new tasks, 
    # e.g. if you want to stop it when one task fails
    futures = [executor.submit(http_post, car_id=car_id) for car_id in car_ids]
    
    for future in concurrent.futures.as_completed(futures):
        result = future.result()  # re-raises error from a thread if there is one
        # do whatever you want with result here
```

question id: 8be6604e-e904-4dcc-bff5-106da1d27afc


### How to stop threads if one raises error

For example, you have a `http_post` function that takes car_id as a keyword argument.
And a list of many many car ids `car_ids`.
And you use something like this to fire off `http_post` in separate threads.


```python
import concurrent
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers) as executor:
    # load workers with tasks
    futures = [executor.submit(http_post, car_id=car_id) for car_id in car_ids]
    
    for future in concurrent.futures.as_completed(futures):
        result = future.result()  # re-raises error from a thread if there is one
        # do whatever you want with result here
```

Just explain with words, no need to write code

answer:

I would write a decorator to wrap a function that is passed to executor.submit
that would:
- take an instance of threading.Event
- if event is set - do not event execute the wrapped function
- if the wrapped function raised an error - set the event and reraise
Also, I would add a condition in a for loop that executes `executor.submit()` 
that check if the event is set

An example:
```python
import concurrent
import logging
import typing as tp
from concurrent.futures import ThreadPoolExecutor
from threading import Event

FUNC = tp.TypeVar("FUNC", tp.Callable[..., tp.Any])

logger = logging.getLogger()

def stop_event_wrapper(func: FUNC, stop_event: Event) -> tp.Callable[[FUNC], tp.Any]:
     """A decorator that won't execute the given function if the given event is set."""
 
     def inner_wrapper(*args: tp.Any, **kwargs: tp.Any) -> tp.Any:
         if stop_event.is_set():
             logger.debug("Do no start the thread due to stop event set...")
             return
         try:
             return func(*args, **kwargs)
         except Exception as err:  # noqa: B902 blind except Exception: statement
             logger.debug(f"Setting stop event due to an err: {err}")
             stop_event.set()
             raise
 
     return inner_wrapper
 
 
def process_s3_objects_in_threads(
     max_workers: int,
     s3_client: S3Client,
     bucket_name: str,
     dataset_path: str,
     func_to_submit: FUNC,
 ) -> int:
     """Go over s3 files and apply a given function to each of them in a separate thread."""
 
     stop_event = Event()
     func_to_submit = stop_event_wrapper(func_to_submit, stop_event)
 
     process_files = 0
     with ThreadPoolExecutor(max_workers) as executor:
         futures = []
         for s3_object in list_s3_objects(s3_client, bucket_name, dataset_path):
             if stop_event.is_set():
                 logger.debug("Stop submitting functions to threads because of the error in one of the threads...")
                 break
             futures.append(executor.submit(func_to_submit, s3_object=s3_object))  # type: ignore
 
         for future in concurrent.futures.as_completed(futures):
             future.result()  # re-raises error from a thread if there is one
             process_files += 1
 
     return process_files
```

question id: 5770128d-74f3-48d7-a1d1-484158b6eda8


### How to gracefully shutdown threads?

answer:
I guess there can be multiple answers, but I would say that it makes sence to pass a threading.Event
to a thread on start, and write your func so to check on this event and when it set - to finish working and exit.

question id: ccce5921-39fa-4693-a6dc-06da3eea5ca1
