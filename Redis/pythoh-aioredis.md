### How to get all keys? 

```python
your_redis_connection.keys(pattern, *, encoding=<object object>)

# like 

app.redis.keys("*", encoding="utf-8")

# or 

app.redis.keys("amo*")

# or

app.redis.keys("*token*")
```

question id: 926aa236-6520-4c37-9e21-169b29420d3c
