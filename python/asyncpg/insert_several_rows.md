### How to insert several rows in a table at once?

For example you have a table like this:

```sql
CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
```
and you want to insert a bunch of tickers:
```python
tickers = ['SBUX', 'AAPL', 'TSM', 'MSFT', 'INTL', 'FAST', 'MNST']
```

how would you do this with asyncpg?

```python
import asyncio
import asyncpg


async def get_connection():
    return await asyncpg.connect(dsn)


async def main():
    conn = await get_connection()
    tickers = ['SBUX', 'AAPL', 'TSM', 'MSFT', 'INTL', 'FAST', 'MNST']
    await insert_tickers(conn, tickers)


async def insert_tickers(conn, tickers):
    sql = '''
    INSERT INTO tickers(name)
    VALUES ($1)
    '''

    tickers_prepared = [(ticker,) for ticker in tickers]
    try:
        await conn.executemany(sql, tickers_prepared)
        print("success")
    except (asyncpg.DataError, asyncpg.UniqueViolationError) as err:
        print("error")
        print(err)
    finally:
        conn.close()


if __name__ == '__main__':
    asyncio.run(main())
```

question id: 72976720-6bc9-44a9-b878-037b1abfab17