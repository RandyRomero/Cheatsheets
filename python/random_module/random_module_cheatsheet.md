### How to get a random integer between 0 and 10?

answer:

```python
from random import random

int(11 * random())
```

Why not `random.randint()`? Because it is dog slow
https://eli.thegreenplace.net/2018/slow-and-fast-methods-for-generating-random-integers-in-python/

question id: 4001755e-c4c4-4f9d-be6c-5e54bda2c0cd


### How to get a random number between two numbers?

```python
from random import random

int(random() * (max + 1 - min)) + min
```

question id: 3efa33f2-6808-4af4-ba6f-85be785769a0


### How exactly does int(random() * (max + 1 - min)) + min give us numbers from 5 to 10?

- random() gives us a float number between 0 and 1
- int(random() * max) gives us numbers from 0 to max-1
- int(random() * (max + 1) gives us numbers from 0 to max
- int(random() * (max + 1 - min)) + min gives a number between min and max


question id: 0c4db707-4835-47b7-a950-bd2c227af50a


### How does random.shuffle() work and what time complexity does it have?

answer

random.shuffle() traverses given list backwards, for every
element in the list Python swaps this element with an element
from a random index. So it takes O(n) as we process all elements and do it just once.

```python
 def shuffle(self, x):
        """Shuffle list x in place, and return None."""

        randbelow = self._randbelow  # randbelow is almost the same as randint
        for i in reversed(range(1, len(x))):
            # pick an element in x[:i+1] with which to exchange x[i]
            j = randbelow(i + 1)
            x[i], x[j] = x[j], x[i]
```

https://github.com/python/cpython/blob/main/Lib/random.py#L373

question id: a3fa1bee-7820-45b2-a3a8-a81f37df5948