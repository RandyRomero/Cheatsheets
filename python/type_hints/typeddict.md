### How to use TypedDict?

```python
from typing import TypedDict

class Person(TypedDict):
  name: str
  age: int

person = Person(name='Michael', age=34)
# or 
person: Person = {'name': 'Michael', 'age': 34}
```

question id: 13debdea-96cd-4bdf-8d54-ab6305805edd


### How to instantiate TypedDict with only some keys?

```python
from typing import TypedDict

class Person(TypedDict, total=False):
  name: str
  age: int

person = Person(name='Michael')
# or 
person: Person = {'name': 'Michael'}
```

question id: b67c90eb-5327-4248-a664-661b5d74d7e4


### How to use something other than strings as keys in TypedDict?

answer:
You cannot. Keys of the TypedDict can only be strings.

question id: aab625d8-c0fd-4781-9174-10b9184c1f75


### How to use TypedDict in Python below 3.8?

answer

```python
from typing_extensions import TypedDict
```

question id: c09717cf-c68f-4299-bf02-94acf1eb20ce
