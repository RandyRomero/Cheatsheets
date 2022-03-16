### What is the conception of bit flags and what is the use of it?

Bit flags are good for when you want to be able to assign any possible combination
of predefined attributes to some object. And to store it in a concise way. 

A very good example of it is a work with some access rights.

For example you want to give your users three types of rights: read, write, delete.
For different users combination can be different. 

One way of implementing it is using bit flags.

Let's take a look at this Python code:

```python
from enum import IntFlag, auto

# describe all our rights
class Rights(IntFlag):
    read = auto()   # 2**0 = 1   0001
    write = auto()  # 2**1 = 2   0010
    delete = auto()  # 2**2 = 4  0100

    # right + write = 1 + 2 = 3 = 0011
```

Here you have your access right as attributes and each of them gets a corresponding value. Each value is 2 in some power.
So the first value is 2^0, second - 2^1, third - 2^2 and so on. So for the first ten attributes you have the following
corresponding values: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512. 
What's the point?

The point is that you can add these values up and get totally unique sum. So you can store each and every combination
of your attributes as just one number (though it could be pretty big).

Let's take back to our code example. Assuming you want to give your user a right to read, which in our case equals to 1.
That's simple, if object `User` has attribute  `permissions` equal to 1, that means he is only able to read (some 
files, resources etc). 
If we assign 2 to permissions of this user, that would mean that he is only able to write. However, the great news is, 
if you want to give them all three rights, that woulb be still just one number. You have to just sum all of the values
of the rights (1 + 2 + 4 = 7) and that's all. If your `user` have his `permissions` equal to 7, that means that he can
read, write and delete. If 3 - he can read and write.

How does this work? That's kinda simple. Take a look at this pattern:

1  | 0001

2  | 0010

4  | 0100

8  | 1000

there decimal system on the left and binary equivalents on the right.

So when you add 1 and 2, you get 3 decimal or 0011 in binary. When you add 1 + 2 + 4, you get 7 decimal or 0111 in 
binary. The point is that every attribute, every right of access of yours is a flag in a row of flags. 
So by adding or subtracting a particular value, that is tided to your attribute/right access, you just set one specific
flag to be 1 or 0.

question id: c694fbd4-0129-414d-b0d8-257a7fccb9ea


### How to implement working with bit flags in Python?

