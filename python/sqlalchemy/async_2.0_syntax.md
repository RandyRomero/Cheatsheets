### How to select exactly one Project by id?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```
How to return a Project with id 1?

Example:
```python
async def get_specific_project(session: AsyncSession, project_id: int) -> Project:
    # your code here
```


answer:
```python
async def get_specific_project(session: AsyncSession, project_id: int) -> Project:
    query = select(Project).where(Project.id == project_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
```

question id: 7bcfbc14-82b9-49b7-9b19-eac49f3b7c59



### How to select all values from a table?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How to return a list of all rows?
What would be the type of the result?

```python
 async with async_session() as session:
     # your code here
```


answer:
```python
async with async_session() as session:
    query = select(Project)
    result = await session.execute(query)
    return list(result.scalars())  # list of objects where each object represents a row
```

question id: d707b9c6-67c8-4706-b080-fa6dc6b5ed57


### How to select all rows filtered by an attribute?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How to return a list of all rows filtered by some attribute like `name`?

```python
async def get_projects_by_a_name(session: AsyncSession, name: str) -> list[Project]:
    # your code here
```

answer:

```python
async def get_projects_by_a_name(session: AsyncSession, name: str) -> list[Project]:
    query = select(Project).where(Project.name == name)
    result = await session.execute(query)
    return list(result.scalars())
```

question id: f9967c66-852c-4b76-a78e-e532c165906d


### How to use WHERE IN in SQLAlchemy ORM 2.0? 

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How find all rows where names are either Jack or John or Ivan?

```python
async def get_projects_by_names(session: AsyncSession, names: list[str]) -> list[Project]:
    # your code here
```

answer

```python
async def get_projects_by_names(session: AsyncSession, names: list[str]) -> list[Project]:
    query = select(Project).where(Project.name.in_(names))
    result = await session.execute(query)
    return list(result.scalars())
```

question id: 6d6940f9-9826-4e29-b7a2-341e1b44ac7a



### How to check whether a Project with a given name exists?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```


```python
async def project_exists(session: AsyncSession, name: str) -> bool:
    # your code here
```

answer:

```python
from sqlalchemy import exists
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from models import Project

async def project_exists(session: AsyncSession, name: str) -> bool:
    query = exists(Project).where(Project.name == name).select()
    result = await session.execute(query)
    return bool(result.scalar_one_or_none())
```

question id: 53f77820-7dc0-4d08-82b8-5115536b27b1


### How to insert a new row?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How to insert a new row with name "Jill"?


answer

```python
async with async_session() as session:
    project = Project(name=name)
    session.add(project)
    try:
        await session.flush()
    except Exception as err:
        await session.rollback()
        raise

    
    await session.commit()
    await session.refresh(project)
    return project.id
```

question id: 63faaf7e-e35e-4ec7-bc1b-fc372d6dacf7


### How to update fields of a row in bulk? (multiple variable fields for one row by its id)


You want a generic function that accepts any kwargs arguments and tries to apply them to your table model.
As a result you want a number of rows that were affected.

```python
async def update_in_bulk(session: AsyncSession, **kwargs):
    # your code here
```

answer:

```python
import typing as tp

async def update_in_bulk(session: AsyncSession, entity: tp.Type[BaseDBModel], **kwargs):
    if not kwargs:
        raise ValueError("No values were passed to update the entity.")
    
    query = update(entity).values(**kwargs).returning(entity.id)
    try:
        result = await session.execute(query)
    except sqlalchemy.exc.DatabaseError as error:
        await session.rollback()
        raise error
    
    await session.commit() 
    pprint(list(result.scalars()))
```

question id: 61c69828-9c87-4067-ba99-4e5f50153404



### How to get a parent object through a field of a child?

You have these two tables:
```python
class BaseDBModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())


class Project(BaseDBModel):
    __tablename__ = "project"
    name: str = Column(String(32), nullable=False)
    status: ProjectStatus = Column(String(32), nullable=False)
    owner_id: int = Column(Integer, ForeignKey('user_table.id', ondelete='NO ACTION'), nullable=True)

    def __repr__(self):
        return f"Project: id: {self.id}, created_at: {self.created_at}, name: {self.name}, status: {self.status}"

    owner = relationship("User", cascade="save-update, merge, expunge", back_populates="projects")


class User(BaseDBModel):
    __tablename__ = "user_table"
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"User: id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}"

    projects = relationship(Project, cascade="save-update, merge, expunge", back_populates="owner")
```

Where User is related to Project as One-to-Many. User is back referenced as Owner in Projects.

You need to select all the Projects with their Owners and return or print out the Owner of the first Project in the list

presudocode:
projects = select projects
print(project[0].owner)

```python
async def get_owner(session):
    pass
```

answer
```python
async def get_owner(session):
    query = select(Project).options(joinedload(Project.owner))
    result = await session.execute(query)
    projects = list(result.scalars())
    print(projects[0].owner)  # User: id: 1, first_name: Randy, last_name: Cooper
```

question id: 6ef37a97-ca90-471b-9df4-bdc34beadc2a


### How to get a list of parent objects with its children objects and return/print the list of children of the first parent object?

You have these two tables:
```python
class BaseDBModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())


class Project(BaseDBModel):
    __tablename__ = "project"
    name: str = Column(String(32), nullable=False)
    status: ProjectStatus = Column(String(32), nullable=False)
    owner_id: int = Column(Integer, ForeignKey('user_table.id', ondelete='NO ACTION'), nullable=True)

    def __repr__(self):
        return f"Project: id: {self.id}, created_at: {self.created_at}, name: {self.name}, status: {self.status}"

    owner = relationship("User", cascade="save-update, merge, expunge", back_populates="projects")


class User(BaseDBModel):
    __tablename__ = "user_table"
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"User: id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}"

    projects = relationship(Project, cascade="save-update, merge, expunge", back_populates="owner")
```

You need to select all users, and to print out the list of projects of the first user
pseudo code

users = select_users_with_projects()
print(users[0].projects)

```python
async def get_projects_of_user(session):
    # your code here
```


answer
```python
async def get_projects_of_user(session):
    query = select(User).options(joinedload(User.projects))
    result = await session.execute(query)
    users = list(result.unique().scalars())  # mind unique() when loading parent object with it's children
    print(users[0].projects)
```

question id: 2e533579-7c6c-4aa8-a21b-f9a6fce15b95


### How to select all parent objects by an attribute of a child object?

You have these two tables:
```python
class BaseDBModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())


class Project(BaseDBModel):
    __tablename__ = "project"
    name: str = Column(String(32), nullable=False)
    status: ProjectStatus = Column(String(32), nullable=False)
    owner_id: int = Column(Integer, ForeignKey('user_table.id', ondelete='NO ACTION'), nullable=True)

    def __repr__(self):
        return f"Project: id: {self.id}, created_at: {self.created_at}, name: {self.name}, status: {self.status}"

    owner = relationship("User", cascade="save-update, merge, expunge", back_populates="projects")


class User(BaseDBModel):
    __tablename__ = "user_table"
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"User: id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}"

    projects = relationship(Project, cascade="save-update, merge, expunge", back_populates="owner")
```

You need to select all Users who have projects with name "build a bridge". How would you do it?

```python
async def get_users_by_project_name(session, name):
    # your code here
```

answer

```python
async def get_users_by_project_name(session, name):
    query = select(User).join(User.projects).where(Project.name == name)
    result = await session.execute(query)
    return list(result.scalars())  # you don't need .unique() here because you don't load projects by joinedload or whatever
```

question id: 5688a4ad-3f3d-40a3-9759-ac4771076135


### How to count all rows in a table?

You have a table like this:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How do you count a number of all rows in this table?


```python
async with async_session() as session:
    # your code here
```

answer

```python
async with async_session() as session:
    query = select(func.count()).select_from(Project)
    result = await session.execute(query)
    result.scalar_one() # either 0, 1, 2 or whatever It won't return None, so there will be no error
```

question id: 71032510-793b-457d-903d-3856b836c99a


### How to count rows in a table on a condition?

You have a table like this:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

How do you count a number of rows in this table where a name of a project is 'Sell the house"?


```python
async with async_session() as session:
    # your code here
```

answer
```python
async with async_session() as session:
    query = select(func.count()).where(Project.name == 'Sell the house').select_from(Project)
    result = await session.execute(query)
    print(result.scalar_one())  # either 0, 1, 2 or whatever It won't return None, so there will be no error
```

question id: 0c7dc608-1e9f-4dc1-8649-6997819f39c3


### How to count number of rows in a table on based on a column in a related table?

You have these two tables:
```python
class BaseDBModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())


class Project(BaseDBModel):
    __tablename__ = "project"
    name: str = Column(String(32), nullable=False)
    status: ProjectStatus = Column(String(32), nullable=False)
    owner_id: int = Column(Integer, ForeignKey('user_table.id', ondelete='NO ACTION'), nullable=True)

    def __repr__(self):
        return f"Project: id: {self.id}, created_at: {self.created_at}, name: {self.name}, status: {self.status}"

    owner = relationship("User", cascade="save-update, merge, expunge", back_populates="projects")


class User(BaseDBModel):
    __tablename__ = "user_table"
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"User: id: {self.id}, first_name: {self.first_name}, last_name: {self.last_name}"

    projects = relationship(Project, cascade="save-update, merge, expunge", back_populates="owner")
```


How to count a number of Projects which owners has first name 'Randy'?

```python
async with async_session() as session:
    # your code here
```

answer:

```python
async with async_session() as session:
    query = select(func.count()).where(User.first_name == 'Randy').select_from(Project).join(Project.owner)
    result = await session.execute(query)
    print(result.scalar_one_or_none())
```

question id: e6fa6636-01fe-4d7b-8087-d44664fb6ddb


### How to update a loaded object?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```

You selected and loaded one row. How to update a field of this object?

```python
async with async_session() as session:
    query = select(Project).where(Project.name == 'to stroke a cat')
    result = await session.execute(query)
    project = result.scalar_one_or_none()
    project.name = "to feed a dog"

# how to actually commit it to the database?
```

answer:
```python
async with async_session() as session:
    query = select(Project).where(Project.name == 'to stroke a cat')
    result = await session.execute(query)
    project = result.scalar_one_or_none()
    project.name = "to feed a dog"

    try:
        await session.flush()
    except Exception:
        await session.rollback()
        raise

    await session.commit()
    await session.refresh(project)
    print(project)
```

question id: 3d36a677-5995-4c71-816e-0a37546d5a40


### How to count all rows where the length of a text field more than N?

You have a table:
```python
class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, server_default=func.now())
    name = Column(String(32), nullable=False)

    def __repr__(self):
        return f"Project: id: {self.id}, name: {self.name}"
```
How to count all the rows where the length of a name field is more than 100?

Example:
```python
async def count_rows(session: AsyncSession) -> Project:
    # your code here
```

answer:

```python
async def count_rows(session: AsyncSession) -> Project:
    query = select(func.count()).where(func.length(Project.name) > 1).select_from(Project)
    result = await session.execute(query)
    print(list(result.scalar_one()))
```

question id: bd1df376-da14-443d-af1e-3683b5591f95s


### How to filter on one condition? On two conditions? How to do it dynamically?

How to filter by one known condition?
How to filter by two known conditions?
How to filter by a variable number of unknown conditions? Like if you get dictionary `kwargs` like
```python
kwargs = {"id": 1, "name": "whatever", "owner_id": 1...}
```

answer

one
```python
query = select(Blog).where(Blog.id == 1)
result = await session.execute...
```

two
```python
query = select(Blog).where(Blog.id == 1).where(Blog.name == "whatever")
result = await session.execute...
```

dynamically
```python
from functools import reduce
from operator import and_

kwargs = {"id": 1, "name": "whatever", "owner_id": 1...}

conditions = reduce(and_, ((getattr(db_model, key) == value) for key, value in kwargs.items()))
# which is in a less dynamic way is 
conditions = reduce(and_, ((getattr(Blog, "id") == 1), (getattr(Blog, "name") == "whatever")))
# or even less...
conditions = reduce(and_, ((Blog.id == 1), (Blog.name == "whatever"),.. ))

query = select(Blog).where(conditions)
result = await session.execute...
```

question id: da2663cc-26d2-4a6d-bac1-9a087c604f75


### Snippet of how to construct where clauses dinamically if you need not only equality, but IN clause also

```python
from functools import reduce
from operator import and_

def get_conditions(**kwargs: tp.Any):
    conditions = []
    for key, value in kwargs.items():
        if isinstance(value, (list, tuple, set)):
            conditions.append((getattr(self.entity, key).in_(value)))
        else:
            conditions.append((getattr(self.entity, key) == value))
return reduce(and_, conditions)
```


### How to return only one field (e.g. id) of an entity?

for example, names of all Projects like this ["some", "names", "of", "some", "projects]

answer:

```python
query = select(Project.name)
result = await session.execute(query)
list(result.scalars()) # ["some", "names", "of", "some", "projects]
```

question id: 9ecb183c-bb82-465e-a1da-74ee8c386d1d


### How to select rows but get specific fields?

for example, entity Project have 10 diffrenet columns, but you only want to select id and name

answer:

```python
query = select(Project.id, Project.name)
result = await session.execute(query)
result.fetchall() # [(1, 'build a bridge'), (3, 'find a job'), (2, 'write a poem'), (4, 'to stroke a cat')]
```

question id: 1fa2b01a-7a62-4250-ade3-25fd9886f076