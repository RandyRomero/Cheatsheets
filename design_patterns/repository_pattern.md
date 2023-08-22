### What is Repository pattern?

https://www.cosmicpython.com/book/chapter_02_repository.html

The Repository pattern is an abstraction over persistent storage. It hides the boring details of data access by pretending that all of our data is in memory.


If we had infinite memory in our laptops, we’d have no need for clumsy databases. Instead, we could just use our objects whenever we liked. What would that look like?

```python
import all_my_data

def create_a_cat():
    cat = Cat(...)
    all_my_data.cats.add(cat)

def modify_a_cat(cat_id, new_name):
    cat = all_my_data.cats.get(cat_id)
    cat.change_name(new_name)
```


There is an example of a typical repository:
```python
class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session

    def add(self, cat):
        self.session.add(cat)

    def get(self, reference):
        return self.session.query(model.Cat).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(model.Cat).all()
```

So, basically, we have a class that abstracts all nitty-gritty details of queries and sessions etc and provides us aimple methods like add, get, list, update etc.

question id: 7e450353-ebc0-45ec-a6cf-42de2cecb386