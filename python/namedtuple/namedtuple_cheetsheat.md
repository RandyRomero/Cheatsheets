### How to create and initiate some typed NamedTuple?

```python
from typing import NamedTuple

class TestCase(NamedTuple):
    case: str
    result: int

case = TestCase(case="abcabcbb", result=3)

print(case.case) # abcabcbb
print(case.result)  # results
```

question id: 354b947d-28ba-4c5d-96a8-aadfbb5c21f6

