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


### Write an example of an abstract class with some abstract methods

answer

```python
from abc import ABC, abstractmethod
 
class Bird(ABC):
 
    @abstractmethod
    def fly(self):
        pass
 
class Hawk(Bird):
 
    def fly(self):  # overrides base class methods
        print("implements details of flying")

    def kill(self):
        print("killing animals to eat them")
```

question id: 652408d8-5afc-4223-9fac-060c7cbcec89


### What would be the output?

```python
class A:
    a = "foo"

x = A()
y = A()

x.a  # ?
y.a  # ?
A.a  # ?
```

answer:

```python
x.a  # foo
y.a  # foo
A.a  # foo
```

https://python-course.eu/oop/class-instance-attributes.php

question id: 78a33f0c-7e01-4588-9119-37b47455ca52


### What would be the output?


```python
class A:
    a = "foo"

x = A()
y = A()

x.a  = "bar"

x.a  # ?
y.a  # ?
A.a  # ?
```

answer:

```python
x.a  # bar
y.a  # foo
A.a  # foo
```

https://python-course.eu/oop/class-instance-attributes.php

question id: 14a00550-9968-42e2-81c8-fdc15b9baccc


### What would be the output?


```python
class A:
    a = "foo"

x = A()
y = A()

x.a  = "bar"

A.a = "baz"

x.a  # ?
y.a  # ?
A.a  # ?
```

answer:

```python
x.a  # bar
y.a  # baz
A.a  # baz
```

https://python-course.eu/oop/class-instance-attributes.php

question id: f6facce1-d384-4e07-ab26-ef1e4f7e01a9


### How to figure out in what order Python will search for a method or attribute of a class that inherits from other class or classes?
And what is the name of the algorithm for that?


Let's start with a simple example:
```python
class A:
  def method(self):
    print("A.method() is called")

class B(A):
  def method(self):
    print("B.method() is called")

b = B()
b.method()
```

The output will be "B.method() is called".
So the method/attribute is first searched in the class which was
mentioned (b.method() - b), than, if not found, in a parent class.


In cases less obvious than this you can just call dunder mro attribute
on the class (not object) to get the tuple with order of classes in which
a search of attributes/methods will be performed.

Like:
```python
class A:
  def method(self):
    print("A.method() called")

class B:
  def method(self):
    print("B.method() called")

class C(A, B):
  pass

class D(C, B):
  pass

# d = D()
# d.method() which method will be called?

print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
```

The algorithm which Python uses for definining in which order methods should be
inherited is called C3 Linearization.

question id: 0fcc8d77-16cc-4355-838e-89253ffe5666