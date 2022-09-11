### How would you make an instance of Pydantic model with your data from orm model?

For example you have sqlalchemy model like this and Pydantic model like this:

```python
from typing import List
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, constr

Base = declarative_base()


class CompanyOrm(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True, nullable=False)
    public_key = Column(String(20), index=True, nullable=False, unique=True)
    name = Column(String(63), unique=True)
    domains = Column(ARRAY(String(255)))


class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]

co_orm = CompanyOrm(
    id=123,
    public_key='foobar',
    name='Testing',
    domains=['example.com', 'foobar.com'],
)
```

You can't just toss co_orm to CompanyModel like
```python
CompanyModel(co_orm)
```
It would give you an error. So what should we do?

answer:

In your Pydantic model you should include

```python


class Config:
        orm_mode = True
```

like

```python
class CompanyModel(BaseModel):
    id: int
    public_key: constr(max_length=20)
    name: constr(max_length=63)
    domains: List[constr(max_length=255)]

    class Config:
        orm_mode = True
```

then 

```python
co_model = CompanyModel.from_orm(co_orm)
print(co_model)  #> id=123 public_key='foobar' name='Testing' domains=['example.com',
```

https://pydantic-docs.helpmanual.io/usage/models/#orm-mode-aka-arbitrary-class-instances

question id: df463ddc-f804-40ca-8d4d-d513033265c0

### How to give a field a static default value?

You have a model like this

```python
from pydantic import BaseModel

class Blog(BaseModel):
    name: str
```

You want that every time that name is not provided to set the value of it to be 'player`
How would you do this?

answer:

```python
from pydantic import BaseModel, Field

class Blog(BaseModel):
    name: str = Field(default="player")
```

question id: 30ef94a1-a1bc-441b-a899-bfc79ad48730



### How to give a field dynamic default? Something that a function would return on each call

You have a model and a function like this

```python
from pydantic import BaseModel

class Blog(BaseModel):
    name: str

def get_random_name():
    pass  # implementation doesn't matter
```

How would you assign this function to give a default name for Blog model on creation by default?

answer:

```python
from pydantic import BaseModel, Field

def get_random_name():
    pass

class Blog(BaseModel):
    name: str = Field(default_factory=get_random_name)
```

Note that `Field(default=get_random_name())` won't properly work - it will remember once 
evaluated value and give it by default every time

question id: 0a48c21f-608c-4fbb-934c-ae9036ce857d


### How to preprocess a field?

You have a model like this:
```python
from pydantic import BaseModel

class Blog(BaseModel):
    name: str
```

You want to replace in `name` every white space with an undersocre. How would you do this?

answer:

```python
from pydantic import BaseModel, validator

class Blog(BaseModel):
    name: str

    @validator("name", pre=True):
    def change_name(cls, value: str) -> str:
        return value.replace(" ", "_")
```

Note: if you just want to strip whitespace from the beginning and the end, you need:

```python
class Blog(BaseModel):
    name: str

    class Config:
        anystr_strip_whatespace = True
```
but it will work on all fields. And it is googled easily.


question id: 7b83a720-5d32-4975-82f1-71047697f834


### How to validate a list of choices (enum)?

```python
from enum import Enum
from pydantic import BaseModel

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class SomeChoices(BaseEnum):
    SOME = "SOME"
    CHOICES = "CHOICES"

# valid list
some_list = ["SOME", "CHOICES"]

# invalid list
invalid_list = ["SOME", "FAILED"]
```

How to validate these lists with Pydantic?


answer:
```python
from enum import Enum
from pydantic import BaseModel

class BaseEnum(str, Enum):
    def __str__(self) -> str:
        return self.value


class SomeChoices(BaseEnum):
    SOME = "SOME"
    CHOICES = "CHOICES"

# valid list
some_list = ["SOME", "CHOICES"]

# invalid list
invalid_list = ["SOME", "FAILED"]


class SomeChoiceSerializer(BaseModel):
    some_choices: list[SomeChoices]


valid_choices = SomeChoiceSerializer(some_choices=invalid_list)

print(valid_choices)
```

question id: b897f0a8-139a-49f0-9d46-2d4c633667f2


### How to validates several fields with Pydantic validator?

Suppose you have a model like this:

```python
from pydantic import BaseModel, validator

class Person(BaseModel):
    first_name: str
    last_name: str
```

How to validate both of these fields?

answer:

```python
from pydantic import BaseModel, validator

class Person(BaseModel):
    first_name: str
    last_name: str

    @validator("first_name", "last_name"):
    def validate_names(cls, value: str) -> str:
        #do something
```

question id: 0a9ba6d9-16b0-42ce-baa4-7bc50a8c8be6