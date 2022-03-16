### How to return first word from the random string?

Write a function that takes a string and returns the first word it finds in that string. 
If the function doesn’t find a space in the string, the whole string must be one word, 
so the entire string should be returned.

answer
```python
def get_first_word(the_string: str) -> str:
    return the_string.split(" ")[0]
```

question id: 062b100b-1c9c-4ee4-8525-a74ae86e8b2d