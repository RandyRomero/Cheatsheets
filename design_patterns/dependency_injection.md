### What is dependency injection?

Dependency injection is a design pattern. The idea is that if a class depends on an object,
that class shouldn't be responsible for constructing this object. It should accept the object as 
a parameter instead. 

This way we make code less coupled and writing tests easier.

https://youtu.be/2ejbLVkCndI

question id: 867af2ab-26ee-4d45-ac88-68b6049ddaca


### What is the difference between dependency injection and dependency inversion?

Dependency injection is a design pattern that states that a class should not construct
an object it depends on. It should take it as a parameter instead.

Dependency inversion principle is one of the SOLID principles that is used to
decouple concrete classes using abstractions: abstract classes or interfaces.

Dependency inversion is not possible without dependency injection.

https://youtu.be/2ejbLVkCndI

question id: 49d61655-6614-410e-a254-5108fcff99fe