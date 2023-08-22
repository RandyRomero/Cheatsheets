### What is unit of work?

answer:

https://www.cosmicpython.com/book/chapter_06_uow.html

The Unit of Work (UoW) pattern is an abstraction over the idea of atomic operations.
It allows us to aggregate several instructions, usually united by a business logic,
and execute these instructions together at once or discard them if one of them fails.

An example of Unit of Work for working with SQLAlchemy:

```python
import typing as tp

from sqlalchemy.orm import sessionmaker

class Database:

    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
        self._blog: tp.Optional[BlogRepository] = None  # _blog is a repository that contains methods to work with blog db table, like list, create, delete etc

    async def __aenter__(self) -> "Database":
        self._session = self.session_factory()  # inits a new SQLAlchemy session
        return self

    async def __aexit__(
        self, 
        exception_type: tp.Optional[tp.Type[Exception]], 
        exception_value: tp.Optional[Exception], 
        traceback: tp.Optional[TracebackType],
    ) -> None:
        """
        Will only rollback data that was not commited withitn the scope of context manager.
        
        For example, if there is an error.
        """
        await self._session.rollback()
        await sels._session.close()


    @property
    def blog(self) -> Blog:
        if not self._blog:
            self._blog = BlogRepository()
        return self._blog()

    async def commit(self):
        await self._session.commit()

    async def refresh(self, entity):
        await self._session.refresh(entity)

    async def rollback(self):
        await self._session.rollback()
```


An example of usage inside an endpoint:
```python
async def post(self, name):
    
    with Database as db:
        blog = db.blog.create(name=name)
        await db.commit()
        await db.refresh(blog)
    
    return {"blog_id": blog.id}
```

question id: fc2be767-4e4e-4875-bcd7-3aee4b88d509