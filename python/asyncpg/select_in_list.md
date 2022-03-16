### How to select rows where id is 1 or 3 or 4?

For example you have a table like this:

```sql
CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
```

answer

```python
import asyncio
import asyncpg

async def get_connection():
    return await asyncpg.connect(dsn)


async def main():
    ids = [1,3,4]
    await get_tickers(ids)


async def get_tickers(ids):
    sql = '''
    SELECT * FROM tickers
    WHERE id = any($1::int[])
    '''

    conn = await asyncpg.connect(dsn)
    try:
        resp = await conn.fetch(sql, ids)
        print(resp)  # [<Record id=1 name='SBUX'>, <Record id=3 name='AAPL'>, <Record id=3 name='TSM'>]
    except (asyncpg.DataError, asyncpg.UniqueViolationError) as err:
        print("error")
        print(err)

if __name__ == '__main__':
    asyncio.run(main())
```

question id: 95eaf9e4-c1e9-4104-9b55-59b81aabf7a4