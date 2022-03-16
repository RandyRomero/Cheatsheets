### What is Python string under the hood?

It is an array of characters. It is an array since the characters are all of the same size (like 4 bytes, 8 bytes) and
array if very fast.

question id: 09da1d63-41dd-4a66-8e95-9f1bec4aa84a


### How to make this string '1, 2, 3' out of this list - `[1, 2, 3]`?

```python
some_list = [1, 2, 3]
", ".join((str(value) for value in some_list))  # '1, 2, 3'
```

question id: 98546ece-f637-4cdc-a65b-473f06bd255d