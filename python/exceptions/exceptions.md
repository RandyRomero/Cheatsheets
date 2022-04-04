### Make a custom exception `TooManyCalls` that accepts how many time is left before the cool down

```python
class TooManyCalls(Exception):
    def __init__(self, timeout: float, message: str = "You've already made too many calls. Chill for at least {:.2} seconds"):
        self.timeout = timeout
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.timeout)
```

https://www.programiz.com/python-programming/user-defined-exception

question id: 1b0dc139-c5ec-4696-b507-82779a432165