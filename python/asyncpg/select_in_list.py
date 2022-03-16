import asyncio
import asyncpg

from settings import settings


async def get_pool():
    return await asyncpg.create_pool(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )


async def main():
    pool = await get_pool()
    await get_tickers(pool)


async def get_tickers(pool):
    sql = '''
    SELECT * FROM tickers
    WHERE id = any($1::int[])
    '''

    async with pool.acquire() as conn:
        try:
            resp = await conn.fetch(sql, [1,2,3])
            print(resp)
        except (asyncpg.DataError, asyncpg.UniqueViolationError) as err:
            print("error")
            print(err)


if __name__ == '__main__':
    asyncio.run(main())