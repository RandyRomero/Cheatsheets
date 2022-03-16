import asyncio
import asyncpg

from settings import settings


async def get_connection():
    return await asyncpg.connect(
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
    )


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