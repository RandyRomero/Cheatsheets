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