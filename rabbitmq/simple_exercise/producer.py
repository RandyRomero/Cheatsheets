import asyncio

from aio_pika import connect_robust, ExchangeType, Message

from constants import EXCHANGE_NAME, ROUTING_KEY, RABBIT_CREDENTIALS


async def main(loop):
    connection = await connect_robust(RABBIT_CREDENTIALS, loop=loop)

    channel = await connection.channel()

    exchange = await channel.declare_exchange(
        EXCHANGE_NAME, type=ExchangeType.DIRECT, durable=True
    )

    message = ""
    while message != "exit":
        message = input("Type something: ")
        await exchange.publish(Message(message.encode("utf8")), routing_key=ROUTING_KEY)

    await connection.close()
    print("exit")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
