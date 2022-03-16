import asyncio

from aio_pika import connect_robust, ExchangeType, IncomingMessage

from constants import EXCHANGE_NAME, ROUTING_KEY, RABBIT_CREDENTIALS

async def on_message(message: IncomingMessage):
    with message.process():
        print(message.body.decode())


async def main(loop):
    connection = await connect_robust(RABBIT_CREDENTIALS, loop=loop)

    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    exchange = await channel.declare_exchange(EXCHANGE_NAME, type=ExchangeType.DIRECT)

    queue = await channel.declare_queue("message_queue", durable=True)
    await queue.bind(exchange=exchange, routing_key=ROUTING_KEY)

    await queue.consume(on_message)
    

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
    loop.close()