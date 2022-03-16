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
    await get_ticker_by_name(pool)


async def get_ticker_by_name(pool):
    sql = f'''
    INSERT INTO tickers(name) VALUES($1)
    '''
    async with pool.acquire() as conn:
        try:
            await conn.execute(sql, 'QRVO')
        except (asyncpg.DataError, asyncpg.UniqueViolationError) as err:
            print("error")
            print(err)
        # tickers = [ticker.get("name") for ticker in resp]
        # print(tickers)

if __name__ == '__main__':
    asyncio.run(main())