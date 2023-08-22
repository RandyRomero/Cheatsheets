import asyncio

import aio_pika

EXCHANGE_NAME = "auth"
ROUTING_KEY = "experimental"
RABBIT_CREDENTIALS = "amqp://guest:guest@localhost/"
QUEUE_NAME = "message_queue"


async def process_message(message_body: str) -> None:
    print(message_body)


async def main(loop):
    connection = await aio_pika.connect_robust(RABBIT_CREDENTIALS, loop=loop)
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=100)

    exchange = await channel.declare_exchange(
        EXCHANGE_NAME, type=aio_pika.ExchangeType.DIRECT, durable=True
    )
    queue = await channel.declare_queue(QUEUE_NAME, durable=True)

    await queue.bind(exchange=exchange, routing_key=ROUTING_KEY)

    async with queue.iterator() as queue_iter:
        async for message in queue_iter:
            async with message.process(
                ignore_processed=True, reject_on_redelivered=True
            ) as message:
                try:
                    await process_message(message.body.decode())
                    message.ack()
                except Exception as err:
                    message.nack(requeue=False)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    loop.run_forever()
    loop.close()
