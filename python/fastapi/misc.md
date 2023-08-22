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


### What's `embed` parameter in `Body` for?

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


### How to write the simplest app with FastAPI?

It has just return "Hello word" when you send GET request to "/"

answer:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

and then run with

`uvicorn main:app --reload`

and paste to your browser http://127.0.0.1:8000/

https://fastapi.tiangolo.com/tutorial/first-steps/

question id: 2fd0c2cb-0251-4aba-846c-6d75e40c6748


### How to check out swagger docs of a FastAPI app?

Given that the default address hasn't been changed.

answer:

www.yourfastapiapp.com/docs 

like

http://127.0.0.1:8000/docs

question id: f655a952-cb40-40bb-923e-03be99ff5b38


### What is 'path' in this url?

https://example.com/items/foo

answer:

/items/foo

question id: b177d5f5-460e-4607-a8b9-9f00abbfd723


### How to define a simple GET handle/enpoint function in FastAPI?

answer:

```python
@app.get("/")
def root():
    return {"message": "Hello World"}
```

where: 
- `app` is your FastAPI application object. It could also be router (`APIRouter`) objects instead of app object
- `get` is a one of available methods (get, post, put, patch, delete, options, header)
- `("/")` denotes the path - so this function will be available under this path. It could be `@app.get("/cats")` for example

question id: 0afe5261-d9d1-4be1-adaf-964eb7d910fc


### How to accept a path parameter?

For example, you have an endpoint like this to list some items:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items")
async def read_item():
    pass
```

and you want to add an endpoint to get a certain item by its id. How would you do so?

answer:


```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    pass
```

https://fastapi.tiangolo.com/tutorial/path-params/

question id: 637572c4-790d-429a-b70c-fc79ea5592b5


### What's wrong here?

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}
```

answer:

The order of the endpoints is wrong. You would never reach "/users/me", because "/users/{user_id"} would match
first. You need to swap them:

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

question id: e838c74f-9ef5-4c41-bfce-ffc0595225cc



### How to denote a predefined path parameter?

For example, you have and enpoint www.yoursite.com/drinks/%one_param_from_a_list%
and the very end of it you would like to make predifined from list
like coffee | tea | water


```python
from fastapi import FastAPI

app = FastAPI()


class BaseEnum(str, Enum):

    def __str__(self) -> str:
        return self.value

class Drinks:
    coffee = "coffee"
    tea = "tea"
    water = "water

@app.get("/drinks/")
async def get_a_drink():
    pass
```

answer:


```python
from fastapi import FastAPI

app = FastAPI()


class BaseEnum(str, Enum):

    def __str__(self) -> str:
        return self.value

class Drinks:
    coffee = "coffee"
    tea = "tea"
    water = "water

@app.get("/drinks/{drink_name}")
async def get_a_drink(drink_name: Drinks):
    if drink_name == Drinks.coffee:
        return {"message": "Drink coffee! Do more stupid things faster with more energy"}
```

question id: 379625f7-6c8d-4b9e-a3db-08d6fdb64f3b