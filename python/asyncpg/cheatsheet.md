### How to create a connection?

```python
import asyncpg
# just as example

conn = await asyncpg.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )
```

https://magicstack.github.io/asyncpg/current/api/index.html

question id: 8eafc05e-feda-433a-8fb8-baf7a169f001


### How to create and use pool?

```python
import asyncpg

pool = await asyncpg.create_pool(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )

async with pool.acquire() as conn:
    await conn.execute("INSERT *...")
```

question id: d4b54d4d-41d9-49f9-8692-e1cbfbb17bdc


### How to select data from a database?

```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn)
    
    try:
        res = await conn.fetch("SELECT * FROM your_database")
        res # list of objects representing rows like [<Record id=1 name='SBUX'>, ...]
    except Exception as exc:
        print(exc)
    finally:
        await conn.close()

asyncio.run(main())
```

question id: 0925b83e-3897-4553-9f8e-096d42eebfee


### How to get rows where %field% is %value%?

```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn)
    field = 'name'
    ticker = 'TSM'
    sql = f"SELECT * FROM your_database WHERE {field} = $1"
    try:
        res = await conn.fetch(sql, ticker)
        res # list of objects representing rows like [<Record id=1 name='TSM'>, ...]
    except Exception as exc:
        print(exc)
    finally:
        await conn.close()

asyncio.run(main())
```

https://github.com/MagicStack/asyncpg/issues/208

question id: c8f80b44-2329-400e-a2e3-292334dc8c0d


### How to get a all ticker names as a list of strings?

For example you have a table like this:

```sql
CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
```

and some ticker in it already. How to get a list of all of them like:
```python
['SBUX', 'AAPL', 'TSM', 'MSFT', 'INTL', 'FAST', 'MNST']
```

answer
```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn)
    sql = f'''
    SELECT * FROM tickers LIMIT 100;
    '''
    resp = []
    try:
        resp = await conn.fetch(sql)
    except Exception as err:
        print(err)
    finally:
        conn.close()
    
    tickers = [ticker.get("name") for ticker in resp]
    print(tickers)

if __name__ == '__main__':
    asyncio.run(main())
```

question id: 27d6e9ce-ffd0-4a60-8f91-69287c0bb317

### What's the difference between connection.fetch() and connection.fetchrow()?

`fetch()` returns a list of Record objects
`fetchrow()` returns only one Record object, not in list

question id: 1c2a46ea-b07c-44af-b7e2-d7ecde1a4abf


### How do you return only value from a specific column?

For example you have a table like this:

```sql
CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
```

and you want the value of name field from the row with id 7

answer
```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn)
    sql = f'''
    SELECT * FROM tickers WHERE id = $1;
    '''
    resp = ''
    try:
        resp = await conn.fetchval(sql, 7, column='name')
    except Exception as err:
        print(err)
    finally:
        conn.close()
    print(resp)

if __name__ == '__main__':
    asyncio.run(main())
```

question id: ed012c52-ff86-48ad-ae5c-a38d1c78bdbb


### How to insert?

For example you have a table like this:

```sql
CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
```

and you want to insert one new ticker

answer
```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn)
    sql = f'''
    SELECT * FROM tickers WHERE id = $1;
    '''
    try:
        await conn.execute(sql, 'QRVO')
        print('success')
    except Exception as err:
        print(err)
    finally:
        conn.close()

if __name__ == '__main__':
    asyncio.run(main())
```


### When and why do we need to use `async with connection.transaction()`? 

You use this context manager when you have a consecutive group of operations that you want to do at a time and make sure
that if any of this operations fails (even that last one), all other operations will be rolled back and the db will not
change its state.

```python
from asyncpg import transaction

async with connection.transaction():
    await connection.execute("INSERT INTO mytable VALUES(1, 2, 3)")
    # await another database call
    # await another database call
```

Without wrapping several statements in transaction wrapper everyone will be committed disregarding of success of the 
rest of them. Think about transaction as of save point. 

question id: 6c25e48c-9e7f-4758-a9f5-0abc652845cb
