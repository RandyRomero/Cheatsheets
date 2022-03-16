### How can you watch logs of every container which name matches some pattern?

answer
```
resource.labels.container_name =~ "^warehouse"
```

~ let's you use regex after = 

question id: c4668848-51e6-42f1-b0b0-4e77f31399f5


### How can you choose logs where your value is in array? 

For example, `jsonPayload.transaction_id` is an array of ids and you need to match a specific one.
Or may be `jsonPayload.transaction_id` is an array of mappings like `[{0: 234324, 1: 2343432, 2: 678676...]`
and you need to find all the logs where there 2343432 in this array. How? 

answer
It's too easy. It's just:

```
jsonPayload.transaction_id = 2343432
```

question id: dcf72348-e2ab-496e-bbf4-7895e06ece5e
