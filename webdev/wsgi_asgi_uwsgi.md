### What is WSGI?

answer:

It's a protocol, a standart of communication between Python Web Server (like Gunicorn, Bjoern, uWSGI) and Python web
application (written in Djano, Flask etc). 

Btw it's syncronous. Asynchronous SGI is called ASGI and its more modern. 

WSGI is just an interface, that look like this:

```python
def application(environ, start_response):
    body = b'Hello world!\n'
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    start_response(status, headers)
    return [body]
```

Tediously profound explanation is here: https://www.toptal.com/python/pythons-wsgi-server-application-interface

question id: 59a346ee-65af-4359-954d-9c7d95808bcb


### What are limitations of WSGI?

answer: 

It's old, so it doesn't support some of modern features.

- it doesn't have official support of websockers (but there are some unofficial workarounds) - (at least it was like that in 2019)
- doesn't work with http2
- not suitable for asynchronous web applications (not 100% sure)

question id: e71834b4-04f0-49b3-be5d-f02b0c0f7cbf


### What is uWSGI?

answer: 

It's a Python web server like Gunicorn and Bjorn, that supports WSGI protocol.

question id: 5c75e9fa-fa2f-4843-bd72-edc1eebd3fed



### What is ASGI? 

answer:

It's Asynchronous Server Gateway Interface. It's a protocol, a standart of communication between 
Python Web Server (like uvicorn) and Python web application (written in FastApi, Starlette etc).


```python
async def application(scope, receive, send):
    event = await receive()
    ...
    await send({"type": "websocket.send", ...})
```

Great talk about ASGI is here https://www.youtube.com/watch?v=uRcnaI8Hnzg

question id: 38fbe476-aba9-4305-9318-742b1da6ecca


### What are upsides of ASGI in comparison to WSGI?

+ supports HTTP2
+ supports WebSockets
+ supports asyncrhronous Web Apps

question id: 77be30f3-0f1e-4ee5-89d1-77bd8f6323ad


### What Server Gateway Interface do aiohttp use?

aiohttp contains server app itself, so it doesn't need gunicorn or uvicorn to be run by,
so you can use just nginx+aiohttp. Thereby aiohttp doesn't need Server Gateway Interface.

WSGI and ASGI are just standarts of communication betwen server app and web app. And aiohttp is server app and
web app in one product.

Take for example FastApi:
client -> server(uvicorn) -> web app(fastapi app)

and aiohttp
client -> server+app(aiohttp)

question id: 22e13580-a555-419f-b481-14b0a96a0ba4

