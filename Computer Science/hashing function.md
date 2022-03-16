## What is a hash function?

Hash function is any function that can be used to map data of arbitrary size to fixed-size values

### What are major properties of a hashing function?

- Irreversibility
    
  A hashing function is a bit like a meat grinder: you put steaks on one end, and get hamburgers on the other - 
  and there is no way to ever get back those steaks starting with the hamburger
  
-  Reproducible
   
   If we hash the same input multiple times, 
   we will always get back the exact same result, bit by bit.
   
- No Collisions

  Another interesting property of Hashing functions is that if we submit multiple values to it, 
  we always get back a unique result per input value.

  There are effectively no situations when two different inputs will produce the same output - 
  a unique input produces a unique output.
  
- Unpredictability
  Given a known output, it's not possible to guess the input using a successive incremental approximation method.
  If we change even a single character in the input (actually even a single bit), on average 50% of the output bits 
  will change!
  
 question id: df4fb701-649d-4579-804b-ed28cdc7fa08


### What does 'irreversibility' mean for hashing function?

A hashing function is a bit like a meat grinder: you put steaks on one end, and get hamburgers on the other - 
and there is no way to ever get back those steaks starting with the hamburger
 
question id: 8d2bb0c7-d148-404a-b5db-c43d4c6ac9b5


### What does 'Reproducible' mean for hashing function?

If we hash the same input multiple times, 
we will always get back the exact same result, bit by bit.
   
question id: e8d9a284-b15c-485d-97b1-2595f5309647


### What does 'No Collisions' mean for hashing function?

Another interesting property of Hashing functions is that if we submit multiple values to it, 
we always get back a unique result per input value.

There are effectively no situations when two different inputs will produce the same output - 
a unique input produces a unique output.
   
question id: b486297c-edc4-4f8d-b161-32056c61b1f7


### What does 'Unpredictability' mean for hashing function?

Given a known output, it's not possible to guess the input using a successive incremental approximation method.
If we change even a single character in the input (actually even a single bit), on average 50% of the output bits 
will change!
   
question id: fde4de6a-cdde-4c42-ab59-35bb0f3c559d