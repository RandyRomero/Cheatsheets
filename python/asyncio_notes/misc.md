### How to start async REPL?

```shell
python -m asyncio
```

Works only with Python 3.8 and higher

question id: 4ebef3f6-b318-41b4-bf1c-8d2ead2bf1f9


### What is an Event Loop?

Python Event Loop is a mechanism that allows cooperative multitasking in Python using coroutines

Event loop is basically a while loop that iterates over a queue of coroutines and also puts callbacks on 
whatver a coroutine is waiting for, so when callback fires, event loop puts corresponding coroutine back
to the queue.

question id: d187862c-ad04-4933-8fe8-0999cd69e9db


### How does Event loop work in Python?

Event loop iterates over a queue of Tasks. Every Task contains a Coroutine. 
Task, when called, executes one iteration of its coroutine, schedules itself back to the end of the queue and suspends.

Between iteration over a queue of Tasks, Event Loop checks on sockets of OS. 
If a socket is ready to read/write, Event Loop puts a Tasks, that waits on this socket, to the task queue.

question id: 9ba1404a-7469-47da-aed5-0af7a5a08c68


### What's a coroutine? (5 attributes)

Coroutine is a function that:
- can pause its execution, saving its state (all variables, arguemnts)
- return control to the caller while paused
- resume from the point where it was paused, restoring its state
- yield values on pausing
- take some values on resuming

question id: 0f112e66-7773-49e5-956d-0c47b4fc60d3


### What's a Task?

Task class definition says that Task is a coroutine wrapped in a Future.

When the event loop executes the Task, Task executes only one iteration of its coroutine (like in 
generators, e.g. next(gen)), then Task schedules itself to the event loop again in order to be 
called again when Event Loop gets back to the Task in order to execute one more iteration of its
coroutine.

Btw, each task has its own call stack.

question id: 153cc61f-ebb5-442d-8d95-378ea1982def


### What is the opposite of a coroutine?

A subroutine. Subroutine is a function, that introduces new scope every time it is called and 
destroys it once it is finished. It does not retain variables and their values between calls. Every
time it is called, it starts from scratch.

question id: 42888d7d-d854-4e97-8a72-21b8e1637a86


### What's a Future?

It's an object, serving as a container for a result we don't have yet, but hopefully we will in the
future. Like Promise in JavaScript. 

It has special API (set of methods) which helps producer of the
value and consumer of the value communicate with each other. For example there are Future.done() 
to check whether the future is done, .cancelled() to check whether the future is cancelled). You 
can check out its result via .result() method or set the result via .set_result(). You can also
set an exception with .set_exception(). You can assign a callback to the future via 
.add_done_callback(). Btw, callbacks do not fire right away, instead they are scheduled to the 
event loop.

question id: 9d40982c-7394-46d2-8b0e-88fba955b56d


### What is Awaitable?

It's an object that has __await__ method

There are three main types of waiting objects: coroutines, Tasks, and Futures.

question id: 287dd24c-c6a9-40bd-b36f-be739cccf49e


### What does asynchronous code of block (async def foo(): pass) returns?

answer

It returns callable, that return object of type Coroutine when it is called.

The Python async def keyword creates a callable object with a name, when the object is called the 
code block of the function is not run. Eg.
```python
async def example_coroutine_function(a, b, c):
    # Asynchronous code goes here
    ...
```

means that example_coroutine_function is now a callable object which takes three parameters. 
When you invoke it like so:
```python
r = example_coroutine_function(1, 2, 3)
```
this does not cause the function code block to be run. Instead, an object of class Coroutine is 
created, and is assigned to r. To make the code block actually run you need to make use of one of 
the facilities that asyncio provides for running a coroutine. Most commonly this is the await 
keyword.

question id: 538b1af7-9420-4d1f-98f2-f62fbe923a61



### How to cancel an awaitable if we don't want to wait for too long?

Use asyncio.wait_for(awaitable, timeout) like this:

```python
async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')

async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())

# Expected output:
#
#     timeout!
```

question id: b9226d91-913e-43ce-99f1-6d2944f37ce1


### Why asyncio.wait_for(awaitable, timeout) doesn't always work?

Keep in mind than I may be wrong.
For example, you have a synchronous call somewhere inside a coroutine you are wait_for(). Maybe even
deeply nested. This synchronous call may take a loooong time. And until it is finished, event loop 
can't get the control back and do something about this looooooong call. In this case wait_for()
won't work.

question id: 6f887c03-a132-414f-8553-4328943faa4


### Does asyncio.wait_for() block execution of the following code or create/schedule a new task in a background?

It's an asynchronous functions, meaning that you have to await as usual:
```python
await asyncio.wait_for(your_function(your_argument), timeout=5)
```
And, while you can fire and forget asyncio.create_task(), you cannot do the same with 
asyncio.wait_for() - you have to wait until it's finished.

question id: 5a915d0c-3700-4847-9e8f-3518b8895e6a


### What is asyncio.wait() for?

coroutine asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED) takes an iterable of 
awaitables (e.g., could be set of Tasks) and returns two sets of Tasks: done and pending.
It has timeout arg after which it returns. However, it does not cancel its awaitables after meeting
the timeout. 

It's seems to be alike with asyncio.gather(), but it is actually different. .gather() returns you
the result of your coroutines, .wait() returns two sets of Tasks: done and pending (means still 
pending after reaching the timeout).

question id: fe2f5467-1f7b-4df2-b55f-3eed18bcaa27


### How to go through a dynamic array of asynchronous tasks?

```python
todo = {} 

while len(todo):
    done, _pending = await asyncio.wait(todo, timeout=0.5)
    todo.difference_update(done)  # delete tasks that are done from the set
```

https://youtu.be/-CzqsgaXUM8?t=2430

question_id: 69ca2cd0-b681-4af7-98dc-22f0b4aaa72d


### What is the difference between `with` and `async with` context managers?

Usual `with` call two synchronous magic methods of a class: `__enter__` and `__exit__`. However, what
if we want these methods to be asynchronous? In order to run asynchronous code inside them. Then
we use `async with` context manager, which in turn calls, or awaits two other magic methods of a 
class: `__aenter__` and `__aexit__`. Inside them, you can use asynchronous code. 

question id: c705eff5-80c6-4174-9a71-daa190846df7


### What's the difference between for loop and async for loop?

Async for loop allows you to use asynchronous method (`__anext__`) of getting next value, which 
means your method will be able to pause its execution at the every step of this for loop. 
Otherwise, your coroutine won't return the control to the event loop till the end of the loop, 
which can take quite a lot of time without switching to another Tasks (remember that event loop
can only deal with other tasks when the current task voluntarily give the control back to the 
event loop).

question id: ebd5a276-1dbd-4810-b1e8-3a339916ff0b



### In asyncio.gather(), if one of the awaitables gets an error, will the rest of awaitables be completed?

answer

The rest of awaitables will continue to be executed only in one case:
- you start asyncio.gather() with return_exceptions=True (so Exceptions will be returned as legit result of a function, they will not be raised)

https://python-forum.io/thread-21211.html

question id: 565c296d-f642-462a-ad82-97e48dee13ff


### How to handle exceptions in asyncio.gather()?

```python
results = await asyncio.gather(task1(), task2(), task3(), return_exceptions=True)
for result in results:
    if isinstance(result, Exception):
        raise result
```

In this case, the rest of the tasks (that didn't fail) will proceed their execution. Otherwise, they
will be cancelled as gather catches the error from the failed task.

question id: 74cc4407-42b4-405d-92d9-47d4b89db80b


### Where will CancelledError be raised when you cancel a Task?

If you cancel a coroutine, the CancelledError will be raised within this coroutine in a
currently executing await statement

```python
async def do_something():
    await asyncio.sleep(10)  # here cancelled error will be raised, so you can wrap it into try except
```

question id: 9fc24ab4-a2f3-4ba7-8eb7-975f181c2404


### How to return only the first completed Task?

answer
Use coroutine asyncio.wait() with return_when=asyncio.FIRST_COMPLETED flag as here:

```python
import asyncio
from random import randrange


async def foo(n):
    s = randrange(5)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    print(f"n: {n}!")


async def main():
    tasks = [foo(1), foo(2), foo(3)]
    result = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(result)  # {<Task finished coro=<foo() done, defined at await.py:5> result=None>}, 
    # {<Task pending coro=<foo() running at await.py:8> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x10322b468>()]>>, 
    # <Task pending coro=<foo() running at await.py:8> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x10322b4c8>()]>>})


asyncio.run(main())
```

So it returns done and pending tasks as soon as there is at least one done task. 

https://www.integralist.co.uk/posts/python-asyncio/#wait

question id: 07614471-80f0-4d34-bfcf-a16d6888eeac 


### How to start several Tasks, but get them back in order they are finished?

answer

Use **asyncio.as_completed()** as shown in this example below:

```python
import asyncio
from random import randrange


async def foo(n):
    s = randrange(10)
    print(f"{n} will sleep for: {s} seconds")
    await asyncio.sleep(s)
    return f"{n}!"


async def main():
    counter = 0
    tasks = [foo("a"), foo("b"), foo("c")]

    for future in asyncio.as_completed(tasks):
        n = "quickest" if counter == 0 else "next quickest"
        counter += 1
        result = await future
        print(f"the {n} result was: {result}")


asyncio.run(main())
```
Code from https://www.integralist.co.uk/posts/python-asyncio/#as_completed


asyncio.as_completed() takes an iterable of awaitables and returns an iterator 
that yields asyncio.Futures in the order the awaitables are done.
There’s no way to find out which awaitable you’re awaiting though.
(c) https://hynek.me/articles/waiting-in-asyncio/


question id: 6fc10b44-8f2b-4d9a-8760-fe0c0e9c727f


### What is asyncio.Event() for? Bring an example of using it

answer

An asyncio event can be used to notify multiple asyncio tasks that some event has happened.

```python
async def wait_on_event(event):
    await event.wait() # will block the coro until the event status is set
    # do something

async def foo():
    event = asyncio.Event()
    asyncio.create_task(wait_on_event(event))
    event.set() # will unclock the coro
```

https://youtu.be/1lJDZx6f6tY?t=1002

question id: e149ffa1-7e82-4788-b033-f460b1a89e2d


### How to gracefully shutdown async Tasks before closing the event loop?

Or how to handle "Task was destroyed but it is pending!"

answer

In layman's terms:
- catch Exceptions that causes your event loop to stop
- get all current tasks that is still working
- async.gather() them to wait while they finish
- stop loop manually

```python
async def main():
  # whatever

async def shutdown():
    tasks = asyncio.all_tasks()  # get unfinished tasks
    await asyncio.gather(*tasks)  # wait when until they are finished

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:  # or whatever you want to catch
        pass
    finally:
        await shutdown()
    loop.close()
```

https://youtu.be/1lJDZx6f6tY?t=1199
https://stackoverflow.com/questions/37417595/graceful-shutdown-of-asyncio-coroutines

question id: 9bcd39d0-3e18-4116-836f-9d19b18e4fd5


### How to limit a number of coroutines running simultaneously?

Use a scheduler from a library called aiojobs
Start every coroutine within this scheduler

```python
scheduler = await aiojobs.create_scheduler(limit=100)

async def my_coroutine():
    pass

await scheduler.spawn(my_coroutine())
```

Suppose we have 100 active jobs already. Next Scheduler.spawn() call pushed a new job into pending list. Once one of already running jobs stops next job from pending list is executed.

https://aiojobs.readthedocs.io/en/stable/intro.html

question id: f03d88aa-7a81-4dfc-83ad-4cf0fbebc2f2




### What is an Event Loop?

Long story short:

- each thread has an Event loop. 
- event loop keeps track of Tasks, selects which one to execute, 
which one to wake up (if, for example, the event it waits for happen - e.g. socket are ready or
whatever). 
- every Task has its own stack of execution (in opposite to synchronous world where is one stack 
  per thread)
- Task based on Future object. Task wraps a coroutine, to provide an API that allows the event loop
execute this coroutine concurrently with other coroutines/Tasks.
- Task has a method _step(), that executes one iteration of the coroutine (```next(coro)```),
than schedules to call the _step() once again on the event loop. So on each step Task creates a 
callback that should execute one iteration of the coroutine until it gets some result.
- When two or more different Tasks schedules one step at a time, they are able to run 
concurrently.



### What is an Event Loop?

You can think of an Event Loop as of While Loop, that executes one step of a Task at a time
(step of a Task is one iteration of your coroutine (like next(your_coroutine))), takes the control
back from the Task, executes another step of another Task and so on. 
It is able to wake up an idle Task when whatever this Task is waiting for becomes available 
(event loop binds callbacks to sockets - when socket is ready to read or write, callback calls 
correspondent Task). Thus two or more functions can co-operatively run together. This the main 
goal of an event loop.



You can think of an Event Loop as of While Loop, that takes one coroutine at a time (actually, 
a Task, that contains coroutine) , runs it, puts it on hold when this coroutine waits for some I/O
(e.g. some socket to be ready to read or 
write), starts another coroutine while the first one is waiting. It is able to wake up an idle 
coroutine when whatever that coroutine is waiting on becomes available (it binds callbacks to 
sockets - when socket is ready to read or write, callback calls correspondent coroutine).
Thus two or more functions can co-operatively run together. This the main goal of an event loop.


In the asyncio world we no longer only have one stack per thread. Instead, each thread has an object 
called an Event Loop. The event loop contains within it a list of objects called Tasks. Each Task 
maintains a single stack, and its own execution pointer as well. At any one time the event loop can 
only have one Task actually executing whilst the other tasks in the loop are all paused. The 
currently executing task will continue to execute exactly as if it were executing a function in a 
normal (synchronous) Python program, right up until it gets to a point where it would have to wait 
for something to happen before it can continue.
Then, instead of waiting, the code in the Task yields control. This means that it asks the event 
loop to pause the Task it is running in, and wake it up again at a future point once the thing it
needs to wait for has happened. The event loop can then select one of its other sleeping tasks to 
wake up and become the executing task instead. Or if none of them are able to awaken (because 
they’re all waiting for things to happen) then it can wait.

An event loop cannot forcibly interrupt a coroutine that is currently executing. A coroutine 
that is executing will continue executing until it yields control. The event loop serves to select 
which coroutine to schedule next, and keeps track of which coroutines are blocked and unable to 
execute until some IO has completed, but it only does these things when no coroutine is currently 
executing.

question id:

Event loop is a concept/programming/programming code that calls a coroutine, waits for it to yield
control back, sets a callback (e.g. if what this coroutine is waiting happened - resume this coroutine),
select other coroutine to run or resume - until all coroutines are finished. That's how functions
can use CPU time more effectively.
The event loop contains within it a list of objects called Tasks. Each Task 
maintains a single stack, and its own execution pointer as well. At any one time the event loop can 
only have one Task actually executing whilst the other tasks in the loop are all paused. The 
currently executing task will continue to execute exactly as if it were executing a function in a 
normal (synchronous) Python program, right up until it gets to a point where it would have to wait 
for something to happen before it can continue.
An event loop cannot forcibly interrupt a coroutine that is currently executing. A coroutine 
that is executing will continue executing until it yields control. The event loop serves to select 
which coroutine to schedule next, and keeps track of which coroutines are blocked and unable to 
execute until some IO has completed, but it only does these things when no coroutine is currently 
executing. 

https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html







### What is an Event loop?

You can think of an event loop as something like a while True loop that monitors coroutines, 
taking feedback on what’s idle, and looking around for things that can be executed in the meantime. 
It is able to wake up an idle coroutine when whatever that coroutine is waiting on becomes 
available (it binds callbacks to socket - when socket is ready to read or write, callback calls
correspondent coroutine).

The loop runs one function, while that function waits for IO, it pauses it and runs another. 
When the first function completes IO, it is resumed. Thus two or more functions can co-operatively 
run together. This the main goal of an event loop.

when I/O from a socket is ready for reading and/or writing, resume coroutine that 


Event loop schedules events, keeps track of coroutines, when a coroutine are idle on I/O, e.l.
pauses it and set's callback (resume the coroutine when corresponding socket is ready to read and/or 
write). 



Coroutine is a function that can pause its execution, yield some result, give away control flow 
back to the caller. Then, when the coroutine is called again, it can take some input, resume from 
the point where it was paused. This way control can bounce back and forth between the calling 
code and the coroutine code, letting you execute a bit of both flows as if in the same time, 
instead of waiting when one of the methods is completely finished.

Every coroutine that is executing is doing so inside a Task

question id: 



Async function in python is a function that creates a coroutine when it is (the function) called


Keep in mind that async function is not awaitable by itself. It returns coroutine, for example, when
it is called, and this coroutine is awaitable, but the function itself is not. 

```python
async def foo():
    await asyncio.sleep(3)

coro = foo()
type(foo)  # <class 'function'>  - not awaitale
type(coro)  # <class 'coroutine'> - awaitable
```







