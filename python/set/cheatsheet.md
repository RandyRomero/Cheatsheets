### How to check whether `['a', 'b', 'c']` in `['a', 'b', 'c', 'd', 'f']`?

Using set.issubset method
```python
{'a', 'b', 'c'}.issubset({'a', 'b', 'c', 'd', 'f'})  # True
{'a', 'b', 'c'}.issubset({'b', 'c', 'd', 'f'})  # False
```

question id: 814a2318-68c1-4404-a21b-9c3011e1bdb1


### How to check if some any of items in `['a', 'b', 'c']` is in `['a', 'b', 'c', 'd', 'f']`?

Using intersection
```python
{'a', 'b', 'c'}.intersection({'b', 'c', 'd', 'f'})  # {'c', 'b'}
```

question id: 41eb3fa0-ad0f-4897-9712-99579f26f332


### How to get an element from a set?

One way is to use .pop() method, it removes and returns a random element from your set

If you don't want to remove an element from a set, user next(iter(your_set))

question id: c0c88415-edd7-4ecf-843c-381dc35a2a19


### What is set.pop() method for?

It removes a random element from your set. 

question id: b7d058f9-245d-42b9-a6d9-bb2d7031b460


### What is an operator for? 

- set.intersection()
- set.union()
- set.difference()
- set.symmetric_difference()

answer

&
|
-
^

question id: 04391f51-3638-4a6f-a2be-bd7fc1ce8a11


### What is the method for the operator?

&
|
-
^

answer

- set.intersection()
- set.union()
- set.difference()
- set.symmetric_difference()

question id: 4109a855-d47a-455b-bc62-4bdd6d524867


### How to remove specific element from a set?

Use either .remove() or .discard()

The difference is that the .remove() method will raise an error if the specified item does not 
exist, and the .discard() method will not.

question id: a57a70cc-6a9e-45a6-ad8e-8fa7d183a915


### What is the use of sets?

Common uses for sets are: 
- fast membership testing 
- removing duplicates from a sequence 
and computing mathematical operations such as: 
- intersection
- union
- difference
- symmetric difference

question id: f1c74d3f-a768-4545-8f03-9072571f8d7f