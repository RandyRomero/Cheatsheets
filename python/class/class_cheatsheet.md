### What is the difference between `__init__()` and `__new__()`?

Short answer:
`__new__()` creates a new instance of a class
` __init__()` initialize the newly created instance

Long answer:

Most object-oriented programming languages such as Java, C++, C#..etc have 
the concept of a constructor, a special method that creates and initializes 
the object when it is created. 

Python is a little different - it has a constructor and an initializer. 
The constructor function is rarely used unless you're doing something exotic. 

`__new__()` - constructor function

` __init__()` - initializer function

`__new__()` is the first step of instance creation. It's called beore ` __init__()` and is responsible for returning a new instance of your class.

In contrast, ` __init__()` doesn't return anything; it's only responsible for initializing the instance after it's been created. So it changes the instance that has just been created
by the `__new__()` method.

question id: 88d8bb4e-ec8d-4d1c-8e6d-09acc56bf228

