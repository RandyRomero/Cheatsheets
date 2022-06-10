### What is SOLID?

SOLID is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin
that make software designs more understandable, flexible, and maintainable

question id: ba2e03b3-579e-4138-8e9d-7d7601e33395


### Name SOLID principles

S - Single-responsiblity Principle
O - Open-closed Principle
L - Liskov Substitution Principle
I - Interface Segregation Principle
D - Dependency Inversion Principle

question id: 8652aeb7-1375-410d-99ee-c872e7c97e7a


### What is Single-Responsibility Principle (SRP)?

answer

The Single Responsibility Principle (SRP) - S in SOLID principles - states 
that a function or a class should have only one responsibility, in other words, 
to do just one thing. For example, making a request, or calculating some
 value, or traversing through files, or storing information to a database.

question id: 9555d1ad-6880-482d-9e50-35fb6874090e


### What are benefits of Single-Responsibility Principle (SRP)? (3)

answer:

SRP is one of the SOLID principles that states that a function (method, class)
should have only one responsiblity, in other words, to do only one thing.

- small functions are easier to understand
- small functions easier to debug
- small functions with one responsibility are much easier to reuse in other places, 
so you reduce code duplication

question id: 5e2f4774-ac4c-4b75-8919-e0adb4101a52


### Where is not a good idea to use Single-Responsibility Principle (SRP)? (2)

answer:

SRP is one of the SOLID principles that states that a function (method, class)
should have only one responsiblity, in other words, to do only one thing.

- it's not really a good idea to make a whole separate function from just one
line of code
- where it seems like a premature optimization. There is no point in splitting
a function to smaller once in advance if you are sure you are not
going to reuse them. You could waste time in building something you just aren’t going to need. 
Remember that premature optimization is the root of all evil. 
Resist the urge to split up functions based on edge cases that you may never encounter.

question id: 82ad3700-26d8-4fa6-b787-36910fdb6c72


### What is Open-closed Principle?

answer:

This is one of the SOLID principles that states that your 
class or function should be open to adding new functionality
but closed to modification.

In other words, the code should be organized in such a way that 
new modules can be added without modifying the existing code.

A bit far away example. You write a software that supports adding some
plugins/extensions to it. You have to write your software in such a way,
that it would be easy and convenient to write a new plug-in
without changing the original software itself.

question id: 5065d79d-76e7-42cc-be1e-c7737f526b88


### What is Liskov Substitution Principle?

answer:

The Liskov substitution principle states that a child class must be 
able to substitute its parent class not causing any errors.

What the LSP indicates is that subtype behavior should match 
base type behavior as defined in the base type specification.

Example
```python
from abc import ABC, abstractmethod
 
class Bird(ABC):
 
    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def walk(self):
        pass
 
 
class Hawk(Bird):
 
    def fly(self):  # overrides base class methods
        print("implements details of flying")

    def kill(self):
        print("killing animals to eat them")

class Penguin(Bird):

    # Penguin can't fly / doesn't have any implementation of fly()

    def swim():
        print('swimming')
```

What's wrong here? Right. A penguin cannot fly. So if we substitue Bird class with Penguin class,
it can cause an error. So we need to fix it.

```python
from abc import ABC, abstractmethod
 
class Bird(ABC):

    @abstractmethod
    def walk(self):
        pass

class BirdsThatCanFly(Bird):
    @abstractmethod
    def fly(self):
        pass
 
class Hawk(BirdsThatCanFly):
 
    def fly(self): 
        print("implements details of flying")

    def kill(self):
        print("killing animals to eat them")

class Penguin(Bird):

    def swim():
        print('swimming')
```

question id: 620caf48-cc21-4a66-98bd-5063c7897d83


### What is Interface segregation principle (ISP)?

answer

It's one of the SOLID principles that states that client
should not be forced to implement an interface that it does not use

Take a look at this simple example:

```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def fly(self):
        pass

class Aircraft(Vehicle):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")

    def fly(self):
        raise Exception('The car cannot fly')
```

In this design the Car class must implement the fly() method from 
the Vehicle class that the Car class doesn’t use. Therefore, this 
design violates the interface segregation principle.

To fix this, you need to split the Vehicle class into small ones and 
inherits from these classes from the Aircraft and Car classes:

```python
class Movable(ABC):
    @abstractmethod
    def go(self):
        pass

class Flyable(Movable):
    @abstractmethod
    def fly(self):
        pass

 class Aircraft(Flyable):
    def go(self):
        print("Taxiing")

    def fly(self):
        print("Flying")

class Car(Movable):
    def go(self):
        print("Going")   
```

In this design, the Car only need to implement 
the go() method that it needs. It doesn’t need to implement 
the fly() method that it doesn’t use.

https://www.pythontutorial.net/python-oop/python-interface-segregation-principle/

question id: 59584d49-4963-4377-845f-b29bf62411c4


### What is Dependency Inversion Principle?

answer:

This is one of the SOLID principles that states two things:
 - high-level modules should not depend on low-level modules. Both should depend on abstractions.
 - abstractions should not depend on details. Details should depend on abstractions.

So what does it mean? It mean that our module/class/function etc must not depend on 
specific implementation of something.

For example, our class Vehicle should not depend on a specific model of engine. Because if 
we want to use another engine in the future, we will be forced to change the code of our 
Vehicle class. It is better if we could make an abstract class of Engine, that provides some common
interface, like methods start and stop, and make our class Vehicle depend on it.
And every speific engine we would inherit from this Engine abstraction. Then, if we want
to change the Engine, we will not be forced to change the code of Vehicle. 

Let'c check out a code example:

```python
class InternalCombustionEngine:

    def start():
        print("Start internal combustion engine")

class Vehicle:

    def __init__(self, ice: InternalCombustionEngine) -> None:
        self.ice = ice

    def start_engine(self):
        self.ice.start()
```

What's wrong with this code? Right, our Vehicle depends on specific 
type of Engine. We cannot use, for example, Electrical engine without
changing code in Vehicle class. So we either have to change it,
or to create a separate ElecticVehicle class or whatever, which leads
to code duplication. Instead, we will make an abstract Engine, and
our Vehicle will depend on it.


```python
from abc import ABC, abstractclassmethod

class Engine(ABC):

    @abstractclassmethod
    def start():
        pass


class InternalCombustionEngine(Engine):

    def start():
        print("Start internal combustion engine")

class ElectricEngine(Engine):
    
    def start():
        print('Start electric engine')


class Vehicle:

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def start_engine(self):
        self.engine.start()
```

https://medium.com/@zackbunch/python-dependency-inversion-8096c2d5e46c
https://www.youtube.com/watch?v=Kv5jhbSkqLE

question id: 715093e6-cb0e-47f4-954f-4c3d23e0e479