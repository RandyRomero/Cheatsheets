### What are item_id, item, user and importance parameters in handle update item mean?

```python
from typing import Optional

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(  # what do these parameters mean?
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
```

answer:

item_id is a path parameter (not query parameter)
item and user - two json dicts that the handle expects in the request body
importance - another json key that handle expects in the request body

So the acceptable request body should look like
```python
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

https://fastapi.tiangolo.com/tutorial/body-multiple-params/#singular-values-in-body

question id: f8aa2b9a-c568-40e0-9a18-1f0fc84f4b0d


### What does `embed` parameter in `Body` for?

As in:
```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    pass
```

answer:

First fact:

Handle like this:
```python
@app.put("/items/{item_id}")
async def update_item(item: Item):
    pass
```

where item is:
```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
```

...expects json like this:
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

The second fact:
If you provide in handle parameters with several models or keys via Body, like this:
```python
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None

@app.put("/items/{item_id}")
async def update_item(  # what do these parameters mean?
    item_id: int, item: Item, user: User, importance: int = Body(...)
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
```

...then the handle will expect json like this:
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
```

But what if you have only one parameter like `item`, but incoming json is like this:
```json
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}
```

and not like:
```json
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2
}
```

Then use `item = Body(..., embed=True`) in your handle like:
```python
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    pass
```

Also, if you don't have model, only one body key, also use Body(..., embed=True)) to denote
that you expect this key like

```python
@app.put("/items/{item_id}")
async def update_item(importance: bool = Body(..., embed=True)):
    pass
```

to expect json like this:
```json
{
  "importance": true
}
```

https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter

question id: 6b625196-2d7a-4440-ac70-e28913379429
