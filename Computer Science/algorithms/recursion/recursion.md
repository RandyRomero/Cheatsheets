### Write a countdown function using recursion

```python
def countdown(i):
    pass

countdown(3)
# 3
# 2
# 1
```

answer
```python
def countdown(i):
    if i < 0:
        return
    print(i)
    countdown(i-1)

countdown(3)
# 3
# 2
# 1
```

question id: 



### What two parts should every recursive function have?

answer:

- a recursive case - when a function calls itself
- a base case - when a function doesn't call itself anymore (otherwise it will be stuck in an infinite loop)

An example:
```python
def countdown(i):
    if i < 0:
        return
    print(i)
    countdown(i-1)

countdown(3)
# 3
# 2
# 1
```

question id:  

