### What's new in Python 3.9?

#### The zoneinfo module for dealing with time zones
#### Union operators that can update dictionaries
#### More expressive decorator syntax:
You can get your decorator from dictionary now
```python
buttons = {
  "hello": QPushButton("Say hello"),
  "leave": QPushButton("Goodbye"),
  "calculate": QPushButton("3 + 9 = 12"),
}

@buttons["hello"].clicked.connect
def say_hello():
    message.setText("Hello, World!")
```

#### You can store in type hint some additional metadata
```python
from typing import Annotated

def speed(
    distance: Annotated[float, "feet"], time: Annotated[float, "seconds"]
) -> Annotated[float, "miles per hour"]:
    """Calculate speed as distance over time"""
    fps2mph = 3600 / 5280  # Feet per second to miles per hour
    return distance / time * fps2mph
```

#### PEG parser was added. It will one day substitute basic LL(1) parser, that parses source code into parse trees

https://realpython.com/python39-new-features/

question id: 40f6792f-9293-4592-88dd-697cdf4d07ca
