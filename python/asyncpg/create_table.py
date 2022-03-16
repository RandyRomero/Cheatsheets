import asyncio
import asyncpg

from settings import settings

async def get_connection():
    return await asyncpg.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,)


async def main():
    conn = await get_connection()
    await create_table(conn)


async def create_table(conn):
    sql = '''
    CREATE TABLE tickers(
        id SERIAL PRIMARY KEY,
        name VARCHAR(10) NOT NULL UNIQUE
        )
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