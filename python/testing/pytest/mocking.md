### How to test this function?

```python
# my_module.py
from db import db_read

def total_value(item_ids):
    items = db_read(item_ids)  # for example, returns a list like [100, 200]
    return sum(items)
```

answer

```python
def test_total_value(mocker):
    db_read_mock = mocker.patch("my_module.db_read", return_value=[100, 200])
    assert 300 == total_value([1, 2])
    db_read_mock.assert_called_with([1, 2]))
```

mocker = [pytest-mock]('https://pypi.org/project/pytest-mock/')

question id: edfbb714-70e9-45ae-9ca3-2e80d944faf4


### How to mock a class with all of it methods and attributes?

answer:

use autospeccing like

```python
import pytest

def test_whatever_you_want_to_test(mocker):
    aiohttp_session = mocker.create_autospec(aiohttp.ClientSession)
```

mocker is a fixture from 
[pytest-mock]('https://pypi.org/project/pytest-mock/')

question id: 9d6b6264-9d7e-4329-9dac-419317db9ba5


### Python <= 3.7. You want to assign a mock to an async method of a class. How?

```python
import TokenRefresher

async def test_check_if_token_is_valid(redis_manager):

    token_refresher = TokenRefresher(redis_manager)
    token_refresher.some_method =  # assign your mock here
```

answer
Use CoroutineMock() from asynctest
```python
from asynctest import CoroutineMock

import TokenRefresher

async def test_check_if_token_is_valid():

    token_refresher = TokenRefresher()
    token_refresher.some_method = CoroutineMock(return_value='whatever you want')
```

question id: 2c2072d7-0180-4754-8de2-3b41d3341ec9


### Python >= 3.8. You want to assign a mock to an async method of a class. How?

```python
import TokenRefresher

async def test_check_if_token_is_valid(redis_manager):

    token_refresher = TokenRefresher(redis_manager)
    token_refresher.some_method =  # assign your mock here
```

answer
Use AsyncMock() from unittest.mock
```python
from unittest.mock import AsyncMock

import TokenRefresher

async def test_check_if_token_is_valid():

    token_refresher = TokenRefresher()
    token_refresher.some_method = AsyncMock(return_value='whatever you want')
```

question id: e3542df3-d6fb-43e6-8762-b16f2a2ba9e9


### How to mock async function so it return a new value each time it is awaited?

answer:

```python
from unittest.mock import AsyncMock

def test_something(mocker):
    mock = mocker.patch(
        'path.to.async.function', 
        side_effect=AsyncMock(side_effect=['first_value', 'second_value', 'and so on']))
```

question id: c4350ead-c7e2-4b1c-a9ca-01352d6ed0cc




