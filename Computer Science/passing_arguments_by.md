Passing by value vs passing by variables in Python and Go (theory)

Golang:
Strictly speaking, there is only one way to pass parameters in Go - by value. 
Every time a variable is passed as parameter, a new copy of the variable is created and passed to 
called function or method. The copy is allocated at a different memory address.

In case a variable is passed by pointer, a new copy of pointer to the same memory address is created.

Python:
Every time you pass something in a function in Python, you pass a pointer to that object in memory.
However there are difference between passing mutable and immutable objects. If you pass, for example,
dictionary or list as an argument and change it within a function, it will be changed both within
and without your function. However, if you pass an int or string to a func, you will work with a local
copy of it within your function.