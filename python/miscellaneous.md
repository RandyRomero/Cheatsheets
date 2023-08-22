### How to get a list of all attributes of an object via list comprehension?

```python
obj_attrs = [attr for attr in dir(your_obj) if not attr.startswith('_')]
```

question_id: 385f1c63-c2d2-46ba-a3bc-2e1a997653bf


### What's a thread?

A thread in Python is a separate flow of instructions.

Only one Python thread (within one Python process) can run at the same time. You can have a few threads, but they 
work in turn, no matter how many cores you CPU has.


### What the difference between multithreading and async programming in Python?

question id: 


### What's the difference between a thread and a process in Python? 5 facts

Process:
- Created by the operating system to run programs
- Processes can run in parallel
- Processes have more overhead than threads as opening and closing processes takes more time
- Processes do not share memory space, in python they share information by pickling data structures  | They share memory space and efficiently read and write to the same variables       
like arrays which requires IO time. 
- Better at CPU bound tasks (e.g. when you crunching some numbers)

Thread
- Threads are separate flows from the main flow of the program that live inside a process.
- Threads can only work one by one. GIL prevents them from working simultaneously.
- To spawn a thread is pretty quick
- They share memory space and efficiently read and write to the same variables
- Better at I/O bound tasks (when you wait a lot on something, like reading or writing, making a http request etc)

question id: 8ca7021a-0da6-4869-b9c0-58982d8fbbfa


### Python function is a first-class object. What does it mean? 

You can assign them to variables, store them in data structures, pass them as arguments to other functions, and even 
return them as values from other functions just like any other object (string, int, float, list, and so on). 
Everything is an object in Python. You remember it, don't you?

question id: b0ca6adc-2e9b-457b-8777-f96d27dc4ca9


### Sort this tuple buy the last item in it

```python
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```

answer: 
```python
student_tuples = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

sorted(student_tuples, key=lambda x: x[2])  # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```

question id: 8df22f20-0149-452b-a11d-5edc53e2cd4e


### What's the difference between sort() and sorted()?

answer:

`sorted()` is a built-in function, that takes an iterable and returns sorted list 
Strings are sorted alphabetically, and numbers are sorted numerically. 

`sort()` is a method of a list that sorts the list in-place

question id: a765ad69-dfd8-42f4-9834-baff679d3d96


### What is the default order of sorting in `sort()` and `sorted()`? How to change it?

Default sorting order for them is ascending. Both `sort()` and `sorted()` take an argument `reverse` which is False by 
default. If you pass True, the iterable will be sorted in a descending order.

question id: c6b5543e-bdf4-44f1-8345-f957eea6ddf5


### How to get caller's name?

How to get a name of a function/method that called the current function. In other words, who is calling the function
you are looking at?

answer

```python
import inspect

def f1(): f2()

def f2():
    print('caller name:', inspect.stack()[1][3])

f1()
```

question id: 80b435fe-5d31-4747-a3d9-2c1ad556656f


### What's pip?
answer
pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other 
indexes.

https://pypi.org/project/pip/

question id: 13f981f8-53ab-4986-9615-541ae6ba3fe7


### Which of the following data types can omit extra kwargs? 

- NamedTuple
- TypedDict
- dataclass
- pydantic.BaseModel

For example, you have a dict with different keys, but you want to create an object only with
specified fields from it and ignore others. So which of these data structures can help you?

answer

Only pydantic.BaseModel can omit extra kwargs. NamedTuple and dataclass will throw an error that
they do not expect some of your kwargs. TypedDict don't give a squat what you assign to it, but
mypy will complain about extra kwargs nevertheless.

dataclass won't help you
```python
from dataclasses import dataclass

@dataclass
class Whatever:
    name: str

data = {"name": "Alice", "age": 9}

whatever = Whatever(**data)

# Traceback (most recent call last):
#   File "/home/ayamikheev/pik_dev/misc/foo.py", line 23, in <module>
#     whatever = Whatever(**data)
# TypeError: __init__() got an unexpected keyword argument 'age'
```


Neither will NamedTuple
```python
from typing import NamedTuple

data = {"name": "Alice", "age": 9}

class Whatever(NamedTuple):
    name: str

whatever = Whatever(**data)

# Traceback (most recent call last):
#   File "/home/ayamikheev/pik_dev/misc/foo.py", line 23, in <module>
#     whatever = Whatever(**data)
# TypeError: __new__() got an unexpected keyword argument 'age'
```

TypedDict is pretty dismissive:
```python
from typing import TypedDict

class Whatever(TypedDict):
    not_name: str

whatever: Whatever = {'name': 'Alice', 'age': 9}
print(whatever)  # {'name': 'Alice', 'age': 9}
```

It just accepts everything. Although mypy will complain. So you still cannot pass extra arguments,
but now because of mypy.


If you already use pydantic in your project, it makes sense to utilize it:
```python
from pydantic import BaseModel

data = {"name": 999, "age": 9, "my_ass": [1, 2, 3], "myd": {"a": 1}}

whatever = Whatever(**data)
print(whatever.name)  # 999
print(type(whatever.name))  # <class 'str'>
```

However, what if you don't use pydantic? It is not awesome to use it just for one small case. 
Thankfully, you can get by a simple class (for simple cases).
```python
data = {"name": 999, "age": 9, "my_ass": [1, 2, 3], "myd": {"a": 1}}

class Whatever:

    def __init__(self, name: str, **kwargs):
        self.name: str = str(name)

whatever = Whatever(**data)
print(whatever.name)  # 999
print(type(whatever.name))  # <class 'str'>
```

question id: f3fe6d76-ca0a-44f6-b265-da9b3096d495


### How to check if a number is divisible by other number without a leftover?

answer
Use module operator

```python
4 % 2  # 0 - 4 is divisible by 2

4 % 3  # 1 - there is a leftover, so 4 is not divisible by 3
```

question id: 9e8afd1b-a4d5-462e-bdf0-fd6de123efe3


### Why don't we use mutable data types as default arguments?

Because mutable data types save their state between function calls

https://youtu.be/0Om2gYU6clE?t=556

question id: 3184c276-5f4e-45cc-bc18-1b8a882ea803


### Why mutable data types as default arguments to a function save their state?

A function is an object. It stores default arguments in dunder default attribute,
which stores default values as a tuple. Default arguments are initialized when
Python executes def statement of a function (so only once, not on every function call).
All default arguments are created when Python initiates your scirpt, once. So, 
while local scope of the function is destroyed every time a function exists, default
arguments live as long as your sciprt lives. That's why your default list or dict
preserve all data between funciton calls.

https://youtu.be/0Om2gYU6clE?t=556

question id: a9d95fb0-62dc-43fd-90c3-f56b38889630


### How to check whether at least one of x or y or z is truthy?

There are at least two ways:

answer

```python
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')
```

question id: 6017f580-520c-416e-b34c-9e16777d39bf

 
### What are immutable sequences? 

strings, tuples, bytes

question id: 25b292f5-9077-4814-a462-f1c77b715f96


### How to make an enumerable in Python?

answer

```python
from enum import Enum

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class Position(BaseEnum):
    UP = "UP"
    DOWN = "DOWN"

print(Position.UP)
```

question id: 3a514a3e-243e-4328-bac0-6989470af2a5


### How to make an enumerable with properties that return set of attributes?

For example you have enumerable
```python
from enum import Enum

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class Count(BaseEnum):
    ONE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
```

but you want to return also groups of attributes as a set, like

```python
Count.odd  # {<Count.FOUR: 'FOUR'>, <Count.TWO: 'TWO'>}
Count.even # {<Count.THREE: 'THREE'>, <Count.FIVE: 'FIVE'>, <Count.ONE: 'ONE'>}
```

How would you do this?

answer

```python
from enum import Enum

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


### How to get a path to the current Python executable programmatically?

answer:

```python
import sys

sys.executable  # "/path/to/bin/python"
```

question id: f28fecf1-49eb-42f7-9524-37bc1aaead93