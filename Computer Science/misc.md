### What are green threads?

In essence a green thread looks and feels exactly like a normal thread, except that the threads 
are scheduled by application code rather than by hardware. But the problem of handling shared 
memory still exists.

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
