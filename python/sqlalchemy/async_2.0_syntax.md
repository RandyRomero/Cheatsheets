### How to check whether a Blog with a given name exists?

```python
from sqlalchemy.orm import sessionmaker

from models import Blog  # Blog has 'name' field

async def make_query(blog_name: str):
    async with sessionmaker() as session:
        # check if there is at least one row in Blog table with the given name
```

answer:

```python
from sqlalchemy import exists
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from models import Blog

async def make_query(blog_name):
    async with sessionmaker() as session:
        query = exists(Blog.id).where(Blog.name == blog_name).select()
        result = await session.execute(query)  # you cannot chain .scalar_one(), it won't work
        return resulst.scalar_one()
```

question id: 53f77820-7dc0-4d08-82b8-5115536b27b1