### What is cooperative multitasking?

Cooperative multitasking is a means of providing the appearance that more than one task
(executing process) is running at a time by switching tasks rapidly. In cooperative multitasking,
tasks are designed to give up their control of the CPU to other applications voluntarily (in
comparison, in preemptive multitasking host itself gets back control from the task).

As an example of cooperative multitasking we can take Python Asyncio library. Event loop cannot
get back the control from the Task until the Task releases the control voluntarily.


https://www.technipages.com/definition/cooperative-multitasking

question id: 370dd3d3-c3ed-4425-8c5d-dda43b966a3



### What is preemptive multitasking?

In preemptive multitasking, the operating system can initiate a context switching from the running
process to another process. In other words, the operating system allows stopping the execution of
the currently running process and allocating the CPU to some other process. The OS uses some
criteria to decide for how long a process should execute before allowing another process to use the
operating system. The mechanism of taking control of the operating system from one process and
giving it to another process is called preempting or preemption.

https://www.geeksforgeeks.org/difference-between-preemptive-and-cooperative-multitasking/

question id: 7af26763-4d88-4f3c-ae5c-b5cebcea4e7d


