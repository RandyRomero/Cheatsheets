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




### You want to assign a mock to a ClientSession() method like .get() or .post() so this mock will 
return, for example, response object with code 200. With what should you patch it?

```python
import TokenRefresher

token_refresher = TokenRefresher()
token_refresher._session.get = # your mock here
```

```python
import asynctest

import TokenRefresher


token_refresher = TokenRefresher()
mocked_response = MockedResponse(status=web.HTTPOk.status_code)
token_refresher._session.get = asynctest.CoroutineMock(
        return_value=mocked_response
    )
```

MockedResponse is just a dummy class that you can write on your own, like this:
```python
class MockedResponse:  # usually you import MockedResponse from some utils or whatever
    """Mocked aiohttp-like response."""

    cookies = None

    def __init__(self, status=200, body=None, json=None):
        """Init."""
        self.status = status
        self._body = body
        self._json = json
```

question id: b07d1526-89a4-41e2-b1b8-0b8c0661beee


### How to mock some class, but so the resulting mock has all attributes and methods of this class?

answer
use autospeccing

Here's an example of it in use:
```python
from urllib import request

patcher = patch('__main__.request', autospec=True) 
mock_request = patcher.start() 

request is mock_request  # True 
mock_request.Request # <MagicMock name='request.Request' spec='Request' id='...'>
```

or like this:
```python
from urllib import request

mock_request = create_autospec(request)
mock_request.Request('foo', 'bar')  # <NonCallableMagicMock name='mock.Request()' spec='Request' id='...'> 
```

https://rapidken.ai/document/python-3*/python?documentURL=10015%2Fprd%2F3%2Flibrary%2Funittest.mock-Autospeccing-1687.html%23auto-speccing

question id: c19f3a89-4078-46e3-8895-9ff962ce3bba