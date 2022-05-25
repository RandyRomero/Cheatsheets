### What is OOP?

Acronym for object-oriented programming which is a computer programming 
model that organizes software design around data, or objects, rather than 
functions and logic.

In this model we first establish distinct objects, e.g. Customer,
Product etc and desribe their specific attributes and behaviours.
The rest of the code is just interaction os these objects. Objects
can communicate with each other, use each other etc.

The point is that it makes our code more structured, more reusable
and more flexible to adding new features.

question id: 81191097-c9cf-40ae-aeca-6f5d98ca877e


### What is a Class in OOP?

Classes are user-defined data types that act as the blueprint 
for individual objects, attributes and methods.

question id: 41aa9981-40e6-4b61-9016-b7dc7f8d9118


### What is an Object in OOP?

Objects are instances of a class created with specifically defined data. 
Objects can correspond to real-world objects or an abstract entity.

question id: bd625d5d-8a5f-4826-97e4-6e5809a1320e


### What is a Method in OOP?

Methods are functions that are defined inside a class 
that describe the behaviors of an object.
Every method has a reference to an instance of its class.

question id: 31599187-6d09-4c44-a171-6e9621b1a348


### Name OOP principles

- encapsulation
- abstraction
- inheritance
- polymorphism

question id: 277306d6-0600-4b50-ac31-4311612ddfce


### What is Encapsulation?

Encapsulation is defined as the wrapping up of data under a single unit.

It is one of OOP principles that states that all important information is 
contained inside an object and only select information is exposed.
The implementation and state of each object are privately held 
inside a defined class. Other objects do not have access to this class 
or the authority to make changes. They are only able to call 
a list of public functions or methods.

question id: 7ff93118-94f6-4a9a-94af-143ef3f33a93


### What is Abstarction (in OOP)?

Abstraction is the concept of hiding a complex logic within a class,
and only provide to a user necessary methods. 

Like a coffee machine hides logic of making a coffee and provides as a 
button "make a coffee". We don't need to know what's going inside the machine,
all we need to know is to push the button.

The same with classes in OOP. Lke in Djano ORM, where class Model encapsulates
a lot of logic of mapping a object to a model and translating our code
to SQL queries. 

question id: 3bffbc5d-5286-4803-aa54-5f635192428d


### What is inheritance? 

Classes can reuse code from other classes. If one class inherits from another one,
it means that it gets all the attributes and methods of a parent class. It also
can define new ones or overwrite the parent's ones.

question id: 019f1fdc-684e-416e-8d24-6e4fe14252fc


### What is Polimorphism?

It's a OOP principle. 
For example, there are different data types in Python that can be iterated over. 
It can be a List, or a FileBuffer. These are completely different data types.

However, due to polimorphism, we can use `for loop` on both of these
types without taking in account how the iteration mechanism works under the hood in these
types.

In other words, poliphormism lest us use objects of different types in a completely same way
if these objects implepemt the same interface.

question id: 9d89d975-c1be-42ed-90ad-bc8efb242515