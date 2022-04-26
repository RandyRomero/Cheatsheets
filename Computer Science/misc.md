### What are Green Threads?

Green threads are threads that are completely 
controled within the app - as opposed to kernel-level threads
that are controlled by the OS.

question id: 9ae190ca-8538-43e8-aa2a-02e42ccd5a9b


### What is the difference between kernel-level threads and green (user-level) threads? (4)

0. Kernel-level threads are controlled by the host OS, so the OS decides when to switch between them.
   Green threads are controlled by your app, so your app manages switching between this threads.
1. Kernel-level threads use premtive-multitasking model. OS can switch threads whenever it (OS) decides
 that that is necessary. OS do not let 
CPU-heavy long-processes run for very long time. It can suspend the process and give the control
to another process. If you want your I/O-tasks do not wait forever for CPU-bound tasks, this is
the way.
Green threads use cooperative multitasking model, so every thread can hold control as much as it needed.
2. Green threads are much-much-much more lightweight than kernel-level threads.

3. Green theads are not affected by GIL, but they still run within one system thread and, therefore, one CPU thread/core. That why they
still can't run in parallel.

question id: c4bb9063-b0f9-484c-82ae-2008482e433f


### What is Round Robin?

It's a concept where all workers, processes etc get an equal share or some resource, one by one, in a cyclic manner.

For example you have a queue of tasks and three workers. You give:
- the 1st task to the 1st worker, then 
then 
- the 2nd task to the 2nd worker
then 
- the 3rd task to the 3rd worker
then
- the 4th task to the 1st worker
then
- the 5th task to the 2nd worker
and so on

question id: 49a116af-9d47-4fa0-9338-36b83a792507



### What is a pointer?

Pointers are variables that refer to some location in memory

questino id: caeaccc3-0ade-4697-b6dd-90b0a447bddd


### What's the difference between Strong Consistency and Eventual Consistency?

Eventual Consistency is a guarantee that when an update is made in a distributed database, 
that update will eventually be reflected in all nodes that store the data, 
resulting in the same response every time the data is queried.


Consistency refers to a database query returning the same data each time the same request is made. 
Strong consistency means the latest data is returned, but, due to internal consistency methods, 
it may result with higher latency or delay. With eventual consistency, 
results are less consistent early on, but they are provided much faster with low latency. 
Early results of eventual consistency data queries may not have the most recent updates 
because it takes time for updates to reach replicas across a database cluster.

https://www.scylladb.com/glossary/eventual-consistency/

question id: 784565e7-f73e-414c-b0f6-d0f8752610d5


### What does imperative in terms of programming lanugages mean?

An imperative language tells the computer to perform certain operations in a certain
order. You can imagine stepping through the code line by line, evaluating conditions,
updating variables, and deciding whether to go around the loop one more time.

question id: 69863856-1533-4bb3-8d99-45c8cf611b58


### What does declaritive in terms of programming lanugages mean?

In a declarative query language, like SQL or relational algebra, you just specify the
pattern of the data you want — what conditions the results must meet, and how you
want the data to be transformed (e.g., sorted, grouped, and aggregated) — but not how
to achieve that goal. It is up to the database system’s query optimizer to decide which
indexes and which join methods to use, and in which order to execute various parts
of the query.

question id: f8c3a8fb-cb5f-4b9f-9ea3-42a333789cf5


### What is MapReduce?

MapReduce is a programming model for processing large amounts of data in bulk
across many machines, popularized by Google 

question id: 906e2bb4-54a5-4b18-8215-b054c3a1181b


### What does it mean if an object is immutable?

An immutable object is an object whose state cannot be modified after it is created.

question id: f64df236-3ce5-42e1-90d7-715e7948c8f4