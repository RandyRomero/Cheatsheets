### How to create database with asyncpg?

sql doesn't matter

```python
import asyncio
import asyncpg

from settings import settings

async def get_connection():
    return await asyncpg.connect(dsn)


async def main():
    conn = await get_connection()
    await create_database(conn)


async def create_database(conn):
    sql = '''
    CREATE DATABASE whatever
    '''

    try:
        await conn.execute(sql)
        print("database created")
    except Exception as err:
        print(err)
    finally:
        await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
```

question id: 9d9e666e-fe0e-4f5a-88f9-fabd10f50250