### How to write python dictionary to json file?

Python dict: whatever = {"hey": "hi", "animals": ["cats", "dogs"], "age": 3.5}

answer
```python
import json

whatever = {"hey": "hi", "animals": ["cats", "dogs"], "age": 3.5}

with open('json_example.json', 'w', encoding='utf8') as file:
    json.dump(whatever, fp=file, sort_keys=True, ensure_ascii=False, indent=2)
```

question id: 58e0a2de-b15a-4c46-8ce3-1967481746d0


### How to read json from string

Your json: 
my_json = b'{"age": 3.5, "animals": ["cats", "dogs"], "hey": "hi"}'
answer

Use serializer
or

```python
import json

my_json = b'{"age": 3.5, "animals": ["cats", "dogs"], "hey": "hi"}'

print(json.loads(my_json))
```
question id: baa779dc-5895-400e-b625-bed64111bd58


### How to read json from file?

answer
```python
import json

with open("json_example.json", "r") as json_file:
    print(json.load(json_file))
```

question id: c94dbd3e-4f9e-4bfd-a286-460ffbb085ba
