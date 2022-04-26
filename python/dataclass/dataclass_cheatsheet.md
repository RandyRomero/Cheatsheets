### How to define and instantiate a dataclass?

```python
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float = 0.0

pos = Position('Oslo', 10.8, 59.9)
>>> print(pos)  # Position(name='Oslo', lon=10.8, lat=59.9)
```

question id: 40da471c-94d4-4e8f-8ec5-67b3d256dbcb