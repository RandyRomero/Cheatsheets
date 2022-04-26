### Write a simple Python aiohttp script to make a get request to https://jsonplaceholder.typicode.com/posts

```python
import asyncio

import aiohttp

async def main():

    async with aiohttp.ClientSession() as session:
        resp = await session.get('https://jsonplaceholder.typicode.com/posts')

        print("Status:", resp.status)
        print("Content-type:", resp.headers['content-type'])

        print(await resp.json())
        # html = await response.text()
        # print("Body:", html[:15], "...")

if __name__ == '__main__':
    asyncio.run(main())
```

question id: 40a555e7-cbdd-4162-89fd-388320b7700c


### How to save downloaded file to disk?

```python
import asyncio
import aiohttp

import aiofiles

async def main():
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url=url, headers=headers)
        print(resp.status)

        f = await aiofiles.open("file path and name on disk", mode='wb')
        await f.write(await resp.read())
        await f.close()
```

question id: 4c8e87da-a751-4c8b-ab39-a4fcd7d6c33f



### Write a simple asynchronous Python script that posts the following things to a server:

It should post to https://httpbin.org/post

Your headers are: 
```python
{"whatever": "whatever"}
```

Your payload is 
```python
{"some key": "some_value"}
```



```python
async def main():
    url = 'http://127.0.0.1:3000/'
    payload = {
        "operationName": "getUsers",
        "variables": {"user_ids": [2]},
        "query": USER_QUERY,
    },
    async with aiohttp.ClientSession() as session:
        resp = await session.post(url=url, headers=headers, json=payload)
        print(resp.status)
        pprint(await resp.json())

if __name__ == '__main__':
    asyncio.run(main())
```

question id: 