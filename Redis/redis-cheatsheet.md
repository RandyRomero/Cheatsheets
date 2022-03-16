### How to get all keys? 

```shell
KEYS *
```

question id: d7a9693a-5b05-440d-a7fb-1d72ca4be146


### How to select all the keys that start with "amo"?

```shell
KEYS amo*
```

question id: df2dfeb6-26cd-4575-933e-f89bc0bc0caf


### How to select all keys that contain "token"? 

```shell
KEYS *token*
```

question id: 7b8bef2f-7cab-42a5-8e8a-f9f2dde3f6d6


### How to set a key value pair such as "Pink":"Panter" for example

answer

```markdown
SET Pink Panther
```

question id: 2d078b03-b6b6-4109-92b6-f8743c47c0bd


### How to check if a key does exist in Redis?

```markdown
EXISTS your_key
```

return either 0 or 1

question id: fea50c19-ee29-4248-9786-300dd8c6bd2c


### How to set multiple key-value pairs within a hash?

HMSET hash key value key value key value

For example:
HMSET movies mask 1994 fear_and_loathing 1998 men_in_black 1997

question id: 2908be90-807c-4274-8f11-09544d4776b4


### How to set a value only if the key does not exists?

SET my_key my_value nx

Example:
127.0.0.1:6379> set my_key my_val nx
OK
127.0.0.1:6379> get my_key
"my_val"
127.0.0.1:6379> set my_key your_val nx
(nil)
127.0.0.1:6379> get my_key
"my_val"

question id: e9c151b7-a929-4e0c-832b-7f9aefea1abe


### How to set a value only if the key does exist?

SET your_key some_val xx

127.0.0.1:6379> set your_key some_val xx
(nil)
127.0.0.1:6379> get your_key
(nil)
127.0.0.1:6379> set your_key some_val
OK
127.0.0.1:6379> get your_key
"some_val"
127.0.0.1:6379> set your_key new_val xx
OK
127.0.0.1:6379> get your_key
"new_val"

question id: a7531c97-4ee2-44c5-855b-ddec82c68881


### How to set a new value to the key while getting the old one?

GETSET

127.0.0.1:6379> getset your_key Petya
(nil)
127.0.0.1:6379> getset your_key Vasya
"Petya"
127.0.0.1:6379> getset your_key Kolya
"Vasya"
127.0.0.1:6379> getset your_key Arnold
"Kolya"

question id: 49203f09-6baf-4ac2-af3e-0b4cc503df5


### How to set, get, increment and decrement a counter? 

127.0.0.1:6379> SET counter 100
OK
127.0.0.1:6379>GET counter
"100"
127.0.0.1:6379> INCR counter
(integer) 101
127.0.0.1:6379> GET counter
"101"
127.0.0.1:6379> DECR counter 
(integer) 100
127.0.0.1:6379> 

question id: 0a2a48ad-e40d-41c8-9728-ad5d6564126f


