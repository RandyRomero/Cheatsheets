import asyncio


async def foo(position):
    print(f"{position} run...")


async def main():
    tasks = [foo(i) for i in range(1, 11, 1)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
