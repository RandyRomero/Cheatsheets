### How would you get all Task(s) without given list of task ids?

Let's say you have Task model and you want get all tasks, but not with these ids: [1, 2, 3].
How would you do this? 

answer:

```python
exclude_ids = [1, 2, 3]

db.query(Task).filter(Task.id.not_in(exclude_ids)).all()
```

question id: 12bfe683-7c18-4bdb-bf25-0f75817472e3


### How do you create a new instance and add it to the database?

Let's say you have user model like this:

```python
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                                self.name, self.fullname, self.nickname)
```

answer:

```python
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session.add(ed_user)
# At this point, we say that the instance is pending; no SQL has yet been issued 
# and the object is not yet represented by a row in the database.
session.commit()
```

session.commit() flushes the remaining changes to the database, and commits the transaction. 
The connection resources referenced by the session are now returned to the connection pool. 
Subsequent operations with this session will occur in a new transaction, which will 
again re-acquire connection resources when first needed.

question id: 