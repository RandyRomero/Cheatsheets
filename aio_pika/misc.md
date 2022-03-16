### How to get exchange by name, not declare? 

answer

Pass flag "passive=True" to await channel.declare_exchange(...) 

```python
await self.channel.declare_exchange(
            self.exchange_name, type=aio_pika.ExchangeType.TOPIC, durable=True, passive=True,
        )
```

according to aio_pika docs for "passive=True":

"Do not fail when entity was declared previously but has another params. Raises 
:class:`aio_pika.exceptions.ChannelClosed` when exchange doesn't exist."

https://aio-pika.readthedocs.io/en/latest/_modules/aio_pika/channel.html

https://github.com/mosquito/aio-pika/issues/281

question id: 545554bc-9e0e-4920-976b-b7bac175aec5
