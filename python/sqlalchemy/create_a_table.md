### How to give a name to a table using SQLAlchemy ORM?

answer:

Define `__tablename__` class attribute like this:

e.g.
```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Blog(Base):
    __tablename__ = "blog"

    pass
```

question id: 8fcda85d-024b-490b-9677-8ad43905c643