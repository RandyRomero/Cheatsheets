https://www.youtube.com/watch?v=0Om2gYU6clE

### Do python variables have types?

answer
No. In python variables do not have types. Python objects store type. Type of an object cannot
be changed. However, type of variable can be changed at a runtime.

```python
foo = 1
foo = 'hello'  # legit in Python, although mypy may argue with you about that
```

question id: 04b1665d-b794-4ddb-ab65-7d2f8a7d35e6



### What the difference in '==' and 'is' operators in Python?

answer

'==' compares values of operands, and 'is' compares their id (address in memory)

That's why:
```python
x = [1, 2, 3]
y = [1, 2, 3]

x == y  # True
x is y  # False
```

question id: ca9db94d-ca22-46e7-a3a6-6edb67c88a72



### What would be the value of nums on the last line?

```python
def assign_new_value(my_list):
     my_list = [42, 34, 27]


nums = [1, 2, 3]
assign_new_value(nums)
print(nums)  #?
```

answer
`[1, 2, 3]`

https://www.youtube.com/watch?v=0Om2gYU6clE&t=202s

question id: 2379f9fc-758c-4d34-8321-f88664adebc9



### Why the value of nums will be `[1, 2, 3]` on the last line?

```python
def assign_new_value(my_list):
     my_list = [42, 34, 27]


nums = [1, 2, 3]
assign_new_value(nums)
print(nums)  # [1, 2, 3]
```

answer

Because my_list = `[42, 34, 27]` makes `my_list` point to new list - `[42, 34, 27]` - instead of 
reassigning original variable - `nums` - to the new array. 

https://www.youtube.com/watch?v=0Om2gYU6clE&t=202s

question id: 58411508-5277-432a-8f45-c6cfb670befc



### How to change a list inside a function that was passed as an argument?

```python
def assign_new_value(my_list):
     # your code here


nums = [1, 2, 3]
assign_new_value(nums)
print(nums)
```

nums should contain `[42, 34, 27]` 

answer

```python
def assign_new_value(my_list):
     my_list[:] = [42, 34, 27]


nums = [1, 2, 3]
assign_new_value(nums)
print(nums)  # [42, 34, 27]
```

question id: 3a31e437-2b81-40c8-a22d-0b1f386292a0


### How to avoid using a list a default argument to the function?

```python
def foo(my_list: tp.List[str]):
    my_list = my_list or []
```

question id: 10cc2e09-2f7d-4977-9c3f-6afe91453f36


### What would be the result?

```python
x = [1, 2]
x_copy = x
x = x + [3, 4]

print(x) #?
print(x_copy) #?
```

answer
```python
print(x) # [1, 2, 3, 4]
print(x_copy) # [1, 2]
```

https://www.youtube.com/watch?v=0Om2gYU6clE&t=600s

question id: 3c690e3f-69bd-4e0f-99e0-040e0d73507d


### What would be the result?

```python
x = [1, 2]
x_copy = x
x = x += [3, 4]

print(x) #?
print(x_copy) #?
```

answer
```python
print(x) # [1, 2, 3, 4]
print(x_copy) # [1, 2, 3, 4]
```

https://youtu.be/0Om2gYU6clE?t=791

question id: e6bf482a-7b05-4dcf-89ba-1d269735fccf


# What would be the result? 

```python
t = 1, [2, 3, 10]
t[1] += [11, 12]
# ?
```

answer
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment

# however
print(t) # (1, [2, 3, 10, 11, 12])
```

https://youtu.be/0Om2gYU6clE?t=842

question id: 5f7e6691-8b73-4779-8eec-341d4f0b20a3
