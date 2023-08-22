### How to instantiate a model entry from a pydantic model?

For example, you have a blog db model like
```python
from sqalchemy.ext.declaritive import declaritive_base  

Base = declaritive_base()

class BlogDB(Base):
    __tablename__ = "blog"

    name = Column(String(100))
```

and a serializer