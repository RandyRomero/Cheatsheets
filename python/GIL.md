### What's GIL?

GIL stands for global interpreter lock. It allows only one thread (within a process) to be executed at a time. 
Thread is a separate flow of instructions. 

The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance 
bottleneck in CPU-bound and multi-threaded code.

question id: 84ff2d94-d67e-4aab-98e7-548d0d3df3ba


### What Problem Did the GIL Solve for Python?

Python has a reference count system for every object as a tool to release acquired memory. So every object has
a count how many variables points to it. In order to avoid race conditions, when two threads are changing the
reference count of the same object, only one thread can be executed at a time. Otherwise there can be memory 
leakages and other nasty bugs. 

question id: 6e6efc46-800a-4262-9f83-483a6a682efe


### What was wrong with GIL before Python 3.2?

The old implementation of GIL worked horribly wrong on multicore machines.
It affected not only the performance of Python script you were running, but the
performance of the whole mahine. It was so bad that threaded versions of code 
worked significantly slower than the same code implemented sequentially.

The problem was that that on where there were more than one process core in system,
Python threads instead on waiting were always awake and always tryintg to get GIL,
which caused a lot of mess that slowed down the performance of the whole system.

question id: 0e7a7064-2f76-44bb-85c8-36016252e36a


### How is thread switching implemented in Python?

https://archive.org/details/pyvideo_580___changes-to-the-gil-in-python-3
https://www.dabeaz.com/python/NewGIL.pdf

I would like to start that the current implementation dates back to Python 3.2
and was suggested by by Antoine Pitrou because the previous GIL has issues 
on multicore machines (you can learn about it in David Beazley talk at the time.)

Let's say we have two threads, first one is currently running and the second
one is suspended. 
New GIL is time-based. Suspended thread makes a call to get the GIL and then waits
for 5 ms. If after 5 ms GIL is still held by the same thread, the suspended tread
raises bolean global variable `gil_drop_request` to one. Whenever it is raised,
the thread that is currently working finishes its current instruction, drops the GIL
and sends a signal that it has dropped the GIL. A thread that acquired the GIL
sends a signal that it has acquired the GIL. Thread that just gave up GIL cannot 
start waiting on it again until it gets signal that another thread got GIL.

However, there is no guarantee that the thread that raised the `gil_drop_request` 
will be the thread who gets the GIL next, because it is up to OS to decide.

question id: 643a24e8-b375-452f-bdd3-f32351c9404e


### What is default interval for thread switching in Python?

5 ms, but it can be set via `sys.setswitchinterval()`

question id: 262c4cd1-8260-4c57-9373-ba62bdf1261c


### When does a thread not raise `gil_drop_request`?

The rule is simple:
- if a thread keeps holding the GIL for more than 5 ms, 
- another thread can raise  `gil_drop_request`.
- if thread 1 gave up the GIL and thread 2 got the GIL while 
- the thread 3 was waiting 5 ms for the GIL, the thread 3 cannot raise `gil_drop_request`.

In other words:
If a suspended thread waits its 5 ms to get the GIL and after this timeout
it sees that GIL was droppped, but now another thread has it, the first thread
will just continue waiting for another 5 ms instead of raising `gil_drop_request`?

question id: c3d88f15-d220-44f6-b4c1-58dcffcb1e11



### new GIL

https://archive.org/details/pyvideo_580___changes-to-the-gil-in-python-3

new GIL was introduced in Python 3.2 by Antoine Pitrou (somewhere in 2009-2010)
because the old implementation of GIL worked horribly wrong on multicore machines
It affected not only the performance of Python sript you were running, but the
performance of the whole mahine. It was so bad that threaded versions of code 
worked significantly slower than the same code implemented sequentially.

Previous GIL kept track of number of ticks (intructions executed by the Python iterpreter)
Once a certain number of ticks had executed, a thread-switch signal was sent.

All of this is gone in the new GIL. New GIL is time-based. It tries to switch threads every 5
ms or so.

There is also a global variable `gil_drop_request`. A threads runs forever in the interpreter
unles this variable is set to 1. At which point the thread MUST drop the GIL.

Let's image a thread 1 is running. We are introducing a new thread - thread B. Thread
B starts in a suspended state. It makes a call like 'give me the GIL withing 5 miliseconds'.
If during this timout thread 1 gives up GIL voluntarily (because it has to wait on I/O or something,
it sends a signal 'I gave up the GIL'.)

If 5 ms after thread 2 asked for the GIL and thread 1 still hasn't gaven its up, thread 2 changes
the global variable `gil_drop_request` to 1 and returns back to waiting. Interpreter constanly checks
on `gil_drop_request` and once it raise, the currently working thread drops GIL immediately. Okay, it
finishes the current instruction first, then drops the GIL, then sends a signal that the GIL is
dropped. Than thread 1 sends signal that it started running. Second thread cannot start waiting for 
someone to drop the GIL until it gets signal that someone took the GIL and started running.

Default timeout for thread swithing is 5 ms, but you can adjust it with sys.setswitchinterval()

Interestingly enough, that if there several threads waiting on thread 1 to drop the GIL, and thread 2
just gets the GIL, other threads will go back to waiting again, not having raised `gil_drop_request` after
5 ms timeout. So, usually a thread waits for 5 ms and then raises the `gil_drop_request`. However, if
this thread sees that while it was waiting, there was a switching from between other threads, it will not
raise `gil_drop_request` and will continue to wait. And if there was thread switing within 5 ms, the thread
will raise the `gil_drop_request`. So that every thread had at least 5 ms to run.




Long running calculations in C may block thread switching because they are not preemptive. 