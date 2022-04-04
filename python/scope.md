### What's scope?

Scope of a name defines the area of a program in which you can unambiguously access that name, such as variables, 
functions, objects, and so on. A name will only be visible to and accessible by the code in its scope.


question id: 2b54f899-2c24-47cc-a232-4a2d28d1d413

### Why do we need a scope for variable names? 

For avoiding name collisions and unpredictable behaviors. 
Scope came about because early programming languages (like BASIC) only had global names. 
With this kind of name, any part of the program could modify any variable at any time, so maintaining and debugging 
large programs could become a real nightmare. 

question id: 9d2b8787-8dc9-4706-b029-8f97678239ce

### What are typical scopes?

- global scope
- local scope

question id: f937cefa-e726-4b84-9da9-9eddd84dbb5d

### What's global scope?

Global scope: The names that you define in this scope are available to all your code.

question id: 18de96ce-19f1-4a48-8879-9a5c8a8aab24

### What's local scope?

The names that you define in this scope are only available or visible to the code within the scope.

question id: 97a22f61-61c2-4d13-a3b3-54838515bea0

### How are scopes implemented in Python?

Python scopes are implemented as dictionaries that map names to objects. 
These dictionaries are commonly called namespaces. These are the concrete mechanisms that Python uses to store names. 
They’re stored in a special attribute called `.__dict__.`

This returns a list with all the names defined at the top level of the module:
```python
import sys
sys.__dict__.keys()  # dict_keys(['__name__', '__doc__', '__package__',..., 'argv', 'ps1', 'ps2'])
```

```python
def foo(baz):
    return baz

foo("a")  # 'a'

foo.bar = "Alaska"
foo.bar  # 'Alaska'

foo.__dict__.keys()  # dict_keys(['bar'])

foo.__dict__["bar"]  # 'Alaska'
```

question id: b61b9a75-c250-4e7c-bc0d-8cbb93223c6c


### What's namespace in Python?

A namespace is a mapping from names to objects. (с) official Python doc The place where a variable is stored. 
Namespaces are implemented as dictionaries (`__dict__`). There are the local, non-local, global
and built-in namespaces as well as nested namespaces in objects (in methods).

question id: c34b3b38-3800-40ab-bc38-4bd64318279b


### What's the difference between a namespace and a scope?

A namespace is a mapping from names to objects. Namespaces in Python are implemented as dictionaries (`__dict__`).
Scope is what namespaces you can see and from where. A module stores its variables in its own namespace (dictionary),
some local function in another namespace (it's own dictionary), but in the same time you can see global variables from
function local scope, but cannot see function variables from global scope. 

question id: a9ccf48c-a3fd-44b1-a035-8251779d198b


### How does Python resolve a name of a variable?

Python resolves names using the so-called LEGB rule, which is named after the Python scope for names. 
The letters in LEGB stand for Local, Enclosing, Global, and Built-in. 
if you reference a given name, then Python will look that name up sequentially in the local, enclosing, global, 
and built-in scope. If the name exists, then you’ll get the first occurrence of it. 
Otherwise, you’ll get an error.

In summary, when you use nested functions, names are resolved by first checking the local scope or the innermost 
function’s local scope. Then, Python looks at all enclosing scopes of outer functions from the innermost scope to 
the outermost scope. If no match is found, then Python looks at the global and built-in scopes. 
If it can’t find the name, then you’ll get an error.

question id: bd4c9546-3c98-43fc-8441-15069f6928a4


### What's local scope in Python?

This Python scope contains the names that you define inside a **function** (or lambda). These names will only be
visible from the code of the **function**. It’s created at function call, not at function definition, so you’ll have
as many different local scopes as function calls. When the function returns, the local scope is destroyed and the 
names are forgotten.

```python
# global scope
x = 5
def whatever():
    # local scope
    x = 4 
    print("whatever")
```

question id: 34c07aa7-5790-49ad-ba99-8f537ae3d225

### What's enclosing scope in Python?

Enclosing scope is the scope of the outer or enclosing function. It can be accessed within function itself and from 
functions defined within this function. 

```python
def outer():
    foo = 4
    # you can access foo from here
    # you cannot access baz from here
    def inner():
        baz = 'baz'
        # you can also access foo from here
```

question id: 5be78ac8-e07c-447e-8279-4f5a9456bd43

### What's global scope in Python? 

Everything defined within the module (though not in function or classes), and everything that is imported. 
Names in this Python scope are visible from everywhere in your code.

question id: 9fd152a1-83a5-444d-8b85-6f6112cdbe27

### What would be the output?

```python
def outer_func():
    var = 100
    def inner_func():
        print(f"Printing var from inner_func(): {var}")
        print(f"Printing another_var from inner_func(): {another_var}")

    inner_func()
    another_var = 200 
    print(f"Printing var from outer_func(): {var}")

outer_func()
```

answer 

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    outer_func()
  File "<stdin>", line 7, in outer_func
    inner_func()
  File "<stdin>", line 5, in inner_func
    print(f"Printing another_var from inner_func(): {another_var}")
NameError: free variable 'another_var' referenced before assignment in enclosing
 scope
```

That is because `another_var` was assigned after the `inner_func()`. All the names that you create in the enclosing 
scope are visible from inside inner_func(), except for those created after you call inner_func().

question id: 9bed2bc6-ccb2-49f7-bcfe-652f95edf053

### What would be the output? 

```python
var = 100
def increment():
    var = var + 1

increment()
```

answer 

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    increment()
  File "<stdin>", line 2, in increment
    var = var + 1
UnboundLocalError: local variable 'var' referenced before assignment
```

You can’t assign global names inside functions unless you explicitly declare them as global names using a 
global statement.

question id: 05cb8fd5-6b05-4d21-96e5-e4a643e2a1a4

### What would be the output? 
```python
var = 100
def func():
    print(var)
    var = 200

func()
```

answer

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    func()
  File "<stdin>", line 2, in func
    print(var)
UnboundLocalError: local variable 'var' referenced before assignment
```

You likely expect to be able to print the global var and be able to update `var` later, but again you get an 
`UnboundLocalError`. What happens here is that when you run the body of `func()`, Python decides that var is a local
variable because it’s assigned within the function scope. This isn’t a bug, but a design choice. Python assumes that 
names assigned in the body of a function are local to that function.

question id: 259f7c14-ba94-40e5-8a86-44fea1d7d6bd


### Where do all of Python’s built-in objects live and how to get a full list of them?.

In module named `builtins`. 
You can get the full list of them by inspecting `__builtins__`.
```python
dir(__builtins__)  # ['ArithmeticError', 'AssertionError',..., 'tuple', 'type', 'vars', 'zip']
``` 

question id: 4e7b467c-1caa-4754-8565-e71a7735ec1b

### How to restore reassigned built-in name?

Use `del`

```python
print = 15
print('whatever')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

del print
print(15)
15 
```

question id: 5da94bae-aff1-408d-8cdd-7aa61cbbd67e

### Why do we need `global` statement?

We need `global` statement when we want to change value of a global variable from inside some function

```python
counter = 0  # A global name
def update_counter():
    global counter  # Declare counter as global
    counter = counter + 1  # Successfully update the counter
update_counter()
counter
1
```

question id: 78ed15d5-dea4-47a4-9bb9-f63d390f6a89


### How to change global variable from inside a function?

With the help of `global` statement

```python
counter = 0  # A global name
def update_counter():
    global counter  # Declare counter as global
    counter = counter + 1  # Successfully update the counter
update_counter()
counter
1
```
Without `global` statement will will get `UnboundLocalError`

question id: 6abcff13-408e-4779-9be4-1ef139aebfe0

### How to create a global variable from inside a function?

```python
def create_lazy_name():
    global lazy  # Create a global name, lazy
    lazy = 100
    return lazy

create_lazy_name()
100
lazy  # The name is now available in the global scope
100
dir()
['__annotations__', '__builtins__',..., 'create_lazy_name', 'lazy']
``` 

question id: 625f7b83-e49a-4138-af80-65158c6435c5

### Why do we need `nonlocal` statement?

`nonlocal` let us change variable value of enclosing function from inside nested function

```python
def func():
    var = 100  # A nonlocal variable
    def nested():
        nonlocal var  # Declare var as nonlocal
        var += 100
    nested()
    print(var)
func()
200
```

question id: e66d50cb-4a83-4042-b643-fed122f770d0

### Where can you use `nonlocal` statement?

Only in nested functions. Any attempts to use it on top level or inside not nested function will lead to a 
`SyntaxError`.

question id: b465fd1d-51a3-45c2-89e6-0aec8c4f0351

### How to change a variable of enclosing function from inside a nested function?


`nonlocal` let us change variable value of enclosing function from inside nested function

```python
def func():
    var = 100  # A nonlocal variable
    def nested():
        nonlocal var  # Declare var as nonlocal
        var += 100
    nested()
    print(var)
func()
200
```

question id: 6c0aef80-0871-42e8-8406-b52ab9e93b12


### Where can you use global statement?

It's legal to use it even in global scope, though it doesn't make sense.

question id: f1652bc1-316e-4c6f-9c65-994eb9843799 


### What would be the output? 

```python
def foo():
    a = 1
    print(a)
    def baz():
        a = 2
        print(a)
    baz()
foo()
```

answer

```python
1
2
```

In the nested function `baz()` you create a new local variable with shadow name `a`. You are not trying to change the 
value of `a` from enclosing function. 

question id: f6c17ed2-e2db-4bc5-b29c-233cf22c6e31

### What would be the output? 

```python
def foo():
    a = 1
    print(a)
    def baz():
        a += 2
        print(a)
    baz()
foo()
```

answer

```python
Traceback (most recent call last):
  File "<string>", line 10, in <module>
File "<string>", line 9, in foo
  File "<string>", line 7, in baz
UnboundLocalError: local variable 'a' referenced before assignment
> 
```

question id: 9de3ca63-f39b-4203-ad5c-ded350205476


### Can we create nonlocal variable this way?

```python
def func():
    def nested():
        nonlocal lazy_var  # Try to create a nonlocal lazy name
```

answer
Nope.
```python
File "<stdin>", line 3
SyntaxError: no binding for nonlocal 'lazy_var' found
```

question id: 04bbd414-6ea1-4fe0-a6dd-83e06ec905c1

### What's closure?

A closure is an inner or nested function that carries information about its enclosing scope, even though this scope 
has completed its execution.

question id: efa11cbc-04a2-4fab-ba51-7e0a4f119e67

### Make a function factory that takes an argument `exp` and returns a new function that takes a `base` as argument
and returns `base` to the power of `exp`

So you can use this function like this:

```python
square = power_factory(2)
square(10)
100
power_factory(3)
cube(10)
1000
cube(5)
125
square(15)
225
```

Answer: we need to use a closure

```python
def power_function(exp):
    def power(base):
        return base ** exp
    return power
``` 

question id: d754b730-2fd1-4c4d-8aed-5516783fb315

### What does this code do?

```python
def power_function(exp):
    def power(base):
        return base ** exp
    return power
``` 

answer

It is a function factory (or closure). It takes an `exp` and return a new function which would take a `base` 
and return `base ** exp`

like this

```python
square = power_factory(2)
square(10)
100
power_factory(3)
cube(10)
1000
cube(5)
125
square(15)
225
```

question id: 416a788c-232d-422d-a81b-84ef3854cd52

### Write a function that takes a int and returns an average of all taken arguments.

Like this

```python
current_mean(10)
10.0
current_mean(15)
12.5
current_mean(12)
12.333333333333334
current_mean(11)
12.0
current_mean(13)
12.2
```

answer

You need to use a closure

```python
from typing import Callable

def mean() -> Callable:
    total = 0
    length = 0
    def _mean(number: int) -> float:
        nonlocal total, length
        total += number
        length += 1
        return total / length
    return _mean

current_mean = mean()
current_mean(10) # 10.0
current_mean(15) # 12.5
```

question id: 5970daa7-97c3-40c9-8d0a-96eccbfed805


### What is Python built-in function `partial()` for?

`partial` can be used for creating a new function out of old but a new one will remember one or several args/kwargs 
passed on initialization.

example
```python
from functools import partial
def power(exp, base):
    return base ** exp

square = partial(power, exp=2)
square(10)
100
```

So you can create more specific function out of more broader function by freezing some of its arguments

question id: a32b92eb-3683-48e5-b90c-6e815c688225

### How to see what's in current global scope?

```python 
dir()  # ['__annotations__', '__builtins__',..., '__spec__']
```

or 

```python
globals()  # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': ...}

```

question id: 6295f543-0302-468c-a6f2-4a5d88e041a1

### What would be the output? 
```python
[item for item in range(5)]
[0, 1, 2, 3, 4]
item
```                                               

answer

```python 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'item' is not defined
```  

The loop variable in a comprehension is local to the structure. Once you run the list comprehension, the variable item 
is forgotten and you can’t access its value anymore.

Note that this only applies to comprehensions. When it comes to regular for loops, the loop variable holds the last 
value processed by the loop.

question id: 2108a331-f2c0-4431-984f-6f2d57c1b5d0


### What would be the output?

```python
for item in range(5):
    print(item)
0
1
2
3
4
item  # Access the loop variable
```

answer

```python
4
```

You can access for loop variable after for loop finishes. The loop variable holds the last value processed by the loop.

question id: 7f7dd038-2790-464f-9fda-ec34e94faf59

### What would be the output?

```python
lst = [1, 2, 3]
try:
    lst[4]
except IndexError as err:
    # The variable err is local to this block
    # Here you can do anything with err
    print(err) # "list index out of range"

err # Try to access err 
```

answer

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    err
NameError: name 'err' is not defined
```

You can use `err` only inside the code block of the except clause. 

To work around this behavior, you can define an auxiliary variable out of the try statement and then assign the 
exception to that variable inside the except block.


```python
lst = [1, 2, 3]
ex = None
try:
    lst[4]
except IndexError as err:
    ex = err
    print(err) # "list index out of range"

ex  # Holds a reference to the exception - "list index out of range"
```

question id: 7790f880-1e2c-4439-a02f-9581968900be

### What is the difference between function local scope and class local scope?

Local scope of a function is created at call time (when this function is called).
Local scope of a class is created at execution time (when Python parsers parses this class definition)

question id: 85d088ef-f60e-4e87-b5e5-bbe0a075deaf

### How to inspect class attributes?

```python
class A:
    attr = 100

A.__dict__.keys()  # dict_keys(['__module__', 'attr', '__dict__', '__weakref__', '__doc__'])
```

This dictionary represents the class local scope. The names in this scope are visible to all instances of the class 
and to the class itself.

question id: 54b95525-c8cb-48e4-8a7c-28cc7ef68f90


### What is the difference between class attributes and instance attributes?

Class attributes are specific to the class object, but you can access them from any instances of the class. It’s 
worth noting that class attributes are common to all instances of a class. If you modify a class attribute, then 
the changes will be visible in all instances of the class.

Instance attributes are local and specific to each instance. This means that if you modify an instance attribute, 
then the changes will be visible only to that specific instance. Instance attributes can’t be accessed using class 
 objects.

question id: '06d8ee8c-6cc7-496c-91b0-482af8c5d268'

### What would be the output?

```python
class A:
    var = 100
    def print_var(self):
        print(var) 

A().print_var()
```

answer

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    A().print_var()
  File "<stdin>", line 4, in print_var
    print(var)
NameError: name 'var' is not defined
```

Although classes define a class local scope or namespace, they don’t create an enclosing scope for methods. Therefore,
when you’re implementing a class, references to attributes and methods must be done using the dot notation.

question id: 'aa628e8a-8d14-4012-a90d-35b55101e2a3'

### What would be the output?

```python
class A:
    var = 100
    def __init__(self):
        self.var = 200

    def access_attr(self):
        # Use dot notation to access class and instance attributes
        print(f'The instance attribute is: {self.var}')
        print(f'The class attribute is: {A.var}')

obj = A()
obj.access_attr()  # What would be the output?
```

answer
```python
The instance attribute is: 200
The class attribute is: 100
```

question id: a76384bf-baff-4f4a-9cd2-03da68e3df20

### What is `globals` for? 

answer

If you call `globals()` in a given module, then you’ll get a dictionary containing all the names that you’ve defined in 
that module, right before the call to globals(). Here’s an example:

```python
globals()
{'__name__': '__main__',..., '__builtins__': <module 'builtins' (built-in)>}
my_var = 100
globals()
{'__name__': '__main__',..., 'my_var': 100}
```

question id: 81b64a44-18ce-4437-bdf2-eb771ea39aaa

### What is `locals()` for?

If you call `locals()` in within a function scope, then you’ll get a dictionary containing all the names that you’ve defined in 
that function, right before the call to `locals()`. Though you won't get variables from enclosing scope.

Example: 
```python
def func(arg):
    var = 100
    print(locals())
    another = 200

func(300)
{'var': 100, 'arg': 300}
```

question id: a742e0a2-82dd-4e0d-94db-975413de4b9e

### What would be the output? 

```python
def func(arg):
    var = 100
    print(locals())
    another = 200

func(300)
```

answer 

```python
{'var': 100, 'arg': 300}
```

When you call locals() in a function block, you get all the names assigned in the local or function scope up to the 
point where you call locals().

question id: 1257f3cb-83ed-423f-b7ec-06a360758db3

### What would be the output? 

```python
def func():
    var = 100
    locals()['var'] = 200
    print(var)

func()
```                          

answer - 100

You can say that locals() is only useful for read operations since updates to the locals dictionary are ignored by
Python.

question id: ea9be6b9-7341-4274-8a6f-67d8c7cd1745


### What will be if you try to call `locals()` in the global Python scope?

answer 

You’ll get the same dictionary that you would get if you were to call `globals()`

question id: e54b6ce1-3fdb-4735-93af-7d180bc806c8

### What's `var()` for?

`vars()` is a Python built-in function that returns the `.__dict__` attribute of a module, class, instance, or any other 
object which has a dictionary attribute.

In comparison to `dir()`, `vars()` displays only attributes of an instance. It won't return class attributes or ancestor 
classes attributes of an instance.

```python
import sys

vars(sys) # With a module object
{'__name__': 'sys',..., 'ps1': '>>> ', 'ps2': '... '}
vars(sys) is sys.__dict__
True

class MyClass:
    def __init__(self, var):
        self.var = var
obj = MyClass(100)
vars(obj)  # With a user-defined object
{'var': 100}
vars(MyClass)  # With a class
mappingproxy({'__module__': '__main__',..., '__doc__': None})
```

question id: e02ffad7-6cbf-4a9f-9d10-fe47cb746169


### What's `dir()?`

It's a built-in function. 

Without arguments, return the list of names in the current local scope. 
With an argument, attempt to return a list of valid attributes for that object.

If the object is a module object, the list contains the names of the module’s attributes.

If the object is instance of a class, the list contains the object’s attributes’ names, the names 
of its class’s attributes, and recursively of the attributes of its class’s base classes.

More details: https://docs.python.org/3/library/functions.html#dir

question id: 913599e0-9187-42fd-b574-32fbe37f34e6


### What is the difference between `dir()` and `var()` built-in functions? 

`dir()` Function:
This function displays more attributes than `vars()` function, as it is not limited to an instance. It displays the class 
attributes as well. It also displays the attributes of its ancestor classes.

`vars()` Function:
This function displays only attributes of an instance

question id: 1dcf2d81-a3dc-4ea1-a19e-91ce7432c0c3

### What would be the output?

```python
vars(10)  # ?
dir(10)  # ?
```

answer 

```python
vars(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: vars() argument must have __dict__ attribute

dir(10)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__'...]
```

Instance of int doesn't have it's own attributes or classes, neither it has `__dict__` for storing them, so `vars()`
cannot use it. In the same time, `dir()` can show attributes and methods of base class and that's what we see here.


question id: d15e49d9-d57e-4b02-af37-cf62ff28b597


### What would be the output? 

```python
x = 0
y = 0
def f():
    x = 1
    y = 1
    class C:
        print(x, y)  # What does this print?
        x = 2
f()
```

answer 

0 1

First of all, code in class definition block runs at evaluation (parsing) time, not at execution time like in function. 
So everything you put into a class definition will be executed as soon as Python interpreter reads the file. 

Second, class definition has the same rules for name resolution, with an exception that unbound local variables are 
looked up in the global namespace.

What do all this mean? 
`y = 1` because it is looked up according to LEGB rule and was found within enclosing scope (within function that is 
enclosing to our class)
`x = 0` in the moment of printing because ... well, this is complicated.

First of all, if it was a function, not a class, it would ended up with an error. When you reference a variable in a
nested function before assignment it is considered to be local variable to this nested function even if it was not 
defined or assigned yet. So Python will not look it up anywhere higher throughout LEGB and throw an error. 

Something similar is with the class definition. The only difference that in this situation (nested class instead of 
nested function) is that if a variable is referenced before assignment, Python will look it up directly in global scope.  

question id: 18677745-616f-4ccb-a302-32bc1cb471ed
