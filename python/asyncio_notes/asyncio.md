### How to run async script?

```python
import asyncio

async def main():
    pass

if __name__ == '__main__':
    asyncio.run(main())
```

The .run function always creates a new event loop and closes it at the end. If you were using the lower-level APIs, 
then this would be something you’d have to handle manually (as demonstrated below).

```python
import asyncio

loop = asyncio.get_event_loop()
loop.run_until_complete(hello_world())
loop.close()
```

question id: 0b778831-da0a-459e-b906-d99da99e44b4


### How to run an async function in a loop?

```python
import asyncio

async def foo(position):
    print(f'{position} run...')

async def main():
    tasks = [foo(i) for i in range(1, 11, 1)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
```

question id: 5680595e-209c-4daf-aa21-1767ee155da4


### What is the difference between threading and async in Python conceptually?

Threads are like workers. Each does it's task. But in Python only one worker is allowed to do something at any
given point in time because of the GIL. And Python switches between this workers all the time. 

With async you have only one worker. But he does all the tasks from the task queue. He constantly switches between them
in order to do them all not one by one, but somehow simultaneously.

So in Python because of the GIL it looks more or less the same in terms of performance.

question id: 9fc64221-a045-417e-adf6-cf3ed8e77295


### What is asyncio.create_task()?

answer
Method asyncio.create_task() schedules async function. It will run in background. And you don't have to await it, 
so you can run it even from synchronous function. For example, in `__init__()`. 

For example, lets assume that g() and f() are both async functions. The simplest way to run them would be: 
```python
result_f = await f()
result_g = await g()
```

However, the coroutines do not run concurrently. g() only starts executing after f() has finished.
To run them concurrently we can use asyncio.create_task() like this:

```python
task_f = asyncio.create_task(f())
task_g = asyncio.create_task(g())

await asyncio.sleep(0.1) # <- f() and g() are already running!
result_f = await task_f
result_g = await task_g
```

Your tasks now run concurrently and if you decide that you don’t want to wait for task_f or task_g to finish, 
you can cancel them using task_f.cancel() or task_g.cancel() respectively. Please note that you must create both tasks 
before you await the first one – otherwise you gain nothing. However, the awaits are only needed to collect the results 
and to clean up resources.

However waiting for each of them like this is not very practical. In real-life code you often enough don’t even know how 
many awaitables you will need to wrangle. What we need is to gather the results of multiple awaitables.

https://hynek.me/articles/waiting-in-asyncio/

question id: f105982c-afeb-4dee-b492-6796c678976e


### When could asyncio.create_task() be useful?

answer
- when you want to execute asynchronous function inside synchronous one. For example, in `__init__()`. 
- when you don't need to wait for it to be finished before move on to next line of code (short and forget)

https://hynek.me/articles/waiting-in-asyncio/

question id: 74d090eb-6581-4e92-8822-14199daa9997


### What is asyncio.ensure_future()? 

answer
I don't know for sure it, but you are most probably don't need asyncio.ensure_future(), it's pretty low-level. Use
asyncio.create_task() instead.

https://github.com/python/asyncio/issues/477#issuecomment-268709555

question id: 09ebbbfb-2186-46a2-b6f3-34cfecc7a31f
