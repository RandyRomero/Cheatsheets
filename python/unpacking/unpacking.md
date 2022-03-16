https://stackabuse.com/unpacking-in-python-beyond-parallel-assignment/

### How is it called?

```python
(a, b, c) = 1, 2, 3
a, b, c = (1, 2, 3)
a, b, c = 1, 2, 3
```

answer
Each of these statements is tuple unpacking

question id: 3ed1ba5f-86ec-40e5-8423-b3274becd1c6


### What statements are legit? 

```python
(a, b, c) = 1, 2, 3
a, b, c = (1, 2, 3)
a, b, c = 1, 2, 3
```

answer
All of them are legit tuple unpacking.

question id: 3e744db0-7276-4417-8dbf-d4d93761c7e9


### What would be the output?

```python
a, b = 1, 2, 3
```

answer
```python
Traceback (most recent call last):
  ...
ValueError: too many values to unpack (expected 2)
```

question id: 1be12a93-7920-4375-9d08-3fd3c2eef4a8


### What would be the output? 

```python
a, b, c = 1, 2
```

answer
```python
Traceback (most recent call last):
  ...
ValueError: not enough values to unpack (expected 3, got 2)
```

question id: ccb42b2c-a53f-41ea-9ed3-4b0b05c5ad55


### What would be the result? 

```python
a, b, c = '123'
```

answer
```
>>> a
1
>>> b
2
>>> c
3
```

question id: 62dda4c9-6c95-44a7-86bc-cdd1678b457e


### What would be the result? 

```python
gen = (i ** 2 for i in range(3))
a, b, c = gen
```

answer
```
>>> a
0
>>> b
1
>>> c
4
```

question id: 030a94b8-9031-457e-b47d-2ba3896c37e6


### What would be the result? 

```python
my_dict = {'one': 1, 'two':2, 'three': 3}
a, b, c = my_dict
```

answer
```
>>> a
'one'
>>> b
'two'
>>> c
'three'
```

question id: 04e8417b-eca4-48ec-a823-c2b376804808


### How to unpack dict values to separate variables at once?

answer
```python
a, b, c = my_dict.values()  # Unpack values
```

```
>>> a
1
>>> b
2
>>> c
3
```

question id: 5b35464f-cfae-4cc7-bf1f-5c6671da66f2


### What would be the result? 

```python
a, b, c = my_dict.items()
```

answer
```
>>> a
('one', 1)
>>> b
('two', 2)
>>> c
('three', 3)
```

question id: e5c2e901-ab88-4d7c-b361-8e290122e222


### Isn't it a legit statement?

```python
x, y, z = range(3)
```

answer
Yep, it's totally legit.
```
>>> x
0
>>> y
1
>>> z
2
```

question id: f208643d-f38c-457c-81cc-6bb8df0f7490


### Can you unpack a set?

```python
a, b, c = {'a', 'b', 'c'}
```

answer
Yes, you can. But you cannot be sure which set member would be assigned to which variable
```
>>> a
'c'
>>> b
'b'
>>> c
'a'
```

question id: eb9d4cc3-f928-4215-9347-c8736f677841


### What will be the output?

```python
*a, = 1, 2
```

answer
```
>> a
[1, 2]
```

question id: 8725fe6f-0e39-4c5b-9f1f-41cf09a85192


### What will be the output?

```python
*a = 1, 2
```

answer

```python
  File "<stdin>", line 1
SyntaxError: starred assignment target must be in a list or tuple
```

For this code to work, the left side of the assignment must be a tuple (or a list). That's why we use a trailing comma. 

question id: 949676af-cab9-476c-b1fa-110961e325f0


### What will be the result?

```python
a, *b = 1, 2, 3
```

answer
```
>>> a
1
>>> b
[2, 3]
```

question id: 3c549fb8-b254-4251-a8cf-962f00b2a5b9


### What will be the result?

```python
*a, b = 1, 2, 3
```

answer
```
>>> a
[1, 2]
>>> b
3
```

question id: 1ae30468-c268-4efe-bbb5-7f65405d532a


### What will be the result?

```python
*a, b, c = 1, 2, 3
```

answer
```
>>> a
[1]
>>> b
2
>>> c
3
```

question id: f366abef-2057-4efb-b97e-3b0cbf278d8c


### What will be the result?

```python
*a, b, c, d = 1, 2, 3
```

answer
```
>>> a
[]
>>> b
1
>>> c
2
>>> d
3
```

question id: 9e4bd99c-b0d3-4ef8-974c-c160f62e2e86


### What will be the result?

```
*a, b, c, d, e = 1, 2, 3
```

answer
```
ValueError: not enough values to unpack (expected at least 4, got 3)
```

question id: ff9ad339-f060-451d-94bd-b36104433719


### How to save items of this generator to a new list?

```python
gen = (2 ** x for x in range(10))
gen  # <generator object <genexpr> at 0x7f44613ebcf0> 
```
answer

```python
*new_list, = gen
```

and of course you can do old by gold:

```python
new_list = list(gen)
```

question id: d22686e0-27d4-4102-9c17-8f722427c33e


### How to save range(10) to a new list?

```python
range_ten = range(10)
range_ten  # range(0, 10)
```
answer

```python
*r, = range_ten
```

and of course you can do old by gold:

```python
r = list(range_ten)
```

question id: 99f077ea-e5b6-4165-8a96-0bb20e03a68b


### What will be the result?

```
*r = range(10)
```

answer
```
 File "<input>", line 1
SyntaxError: starred assignment target must be in a list or tuple
```

question id: 482622e9-73a5-4d1e-9c00-6e0fc595a45b


### Save a list to three separate variables

You have a list
```python
["John Doe", "40", "Software Engineer"]
```

You need to save each value to a correspondent variable: name, age, job. How will you do that?

answer
```python
name, age, job = ["John Doe", "40", "Software Engineer"]
```

question id: ff690d10-93bb-45ee-a056-39c1091f3bf5


### How to swap values between these two variables?

```python
a = 100
b = 200
```

answer

```python
a, b = b, a
a  # 200
b  # 100
```

question id: bbd12bda-9e88-470a-95a4-74bc4dda910f


### What will be the result?

```python
seq = [1, 2, 3, 4]
first, *body, last = seq
```

answer
```
>>> first
1
>>> body
[2, 3]
>>> last
4
```

question id: 72ba98bb-c407-4dce-affb-99e72007c22d


### How to save this iterable `seq = [1, 2, 3, 4]` to three separate variables: first, everything_in_between, last?
There result should look like this:
 ```
>>> first
1
>>> everything_in_between
[2, 3]
>>> last
4
```

answer
```python
first, *everything_in_between, last = seq
```

question id: c1cf9af3-0d49-4af0-98e9-a97172517a85


### What's another way of writing `list(my_set) + my_list + list(my_tuple) + list(range(1, 4)) + list(my_str)` ?

answer
```python
[*my_set, *my_list, *my_tuple, *range(1, 4), *my_str]
```

question id: 3897326f-838e-42e1-b53f-239574fac896


### What will be the output? 

```
>> for first, *rest in [(1, 2, 3), (4, 5, 6, 7)]:
...     print("First:", first)
...     print("Rest:", rest)
```

answer

```
First: 1
Rest: [2, 3]
First: 4
Rest: [5, 6, 7]
```

question id: f6ce8cf9-1896-4e1d-aa5e-e6cb50e10260