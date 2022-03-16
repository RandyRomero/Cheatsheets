### What's a descriptor in Python?

a descriptor in Python is an object which has any of following methods: __get__(), __set__(), __delete__()

A descriptor lets you to intercept calling of a specific class attribute(s) and embed some logic. 
For example, Python's property decorator uses descriptor protocol to change a behavior of getting, 
setting and deleting of a specific attribute

https://docs.python.org/3/howto/descriptor.html

question id: fe3331f5-0084-4c67-969f-4fc5c589a377