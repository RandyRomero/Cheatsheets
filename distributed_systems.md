### It's difficult to guarantee exactly one delivery in distributed systems. What can we do instead?

Instead, we can do one of two things or a combination of both:

1) Make messages idempotent

If no matter how many times you send a message, the result is the same, you can rely on it
rather than try to fight with "more than one delivery". The problem is that not every operation
could be idempotent. For example, if you set exact state, like "something = True", it is
idempotent. However, if your change of state depends on a previous state, e.g, "account += 100",
you have better not receive the same message twice or more

2) message de-duplication

You can attach some id to your message, like a hash of a message for example, so the sender can
check whether it has already received the message recently. Hovewer, the time you store the hashes
of all seen messages should be reasonable, don't store them for eternity.

The decision is simple: where you can rely on idempotency, rely on idempotency. Where you can't,
use message de-duplication.

https://lostechies.com/jimmybogard/2013/06/03/un-reliability-in-messaging-idempotency-and-de-duplication/

question id: ad7ef6a8-af3f-4903-b18c-c0c6a0d0b40a