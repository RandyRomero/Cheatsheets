### What is MappingProxyType and how to use it?

It's an interface for a dictionary which only allows read-only access to a dict
However you still can change your original dict and these changes will be reflected in your 
read-only interface to the dict

```python
from types import MappingProxyType

_animals = {"cats": 3, "dogs": 4}

animals = MappingProxyType(_animals)

animals["cats"] = 4  # TypeError: 'mappingproxy' object does not support item assignment 
```

question id: a66f16e7-16ff-4020-b83c-3495ef68aabd


### Create a dict with the same initial values (show two ways)

```python
keys = ("cats", "dogs", "parrots")
```

answer:
```python
keys = ("cats", "dogs", "parrots")

# 1st way
dict.fromkeys(key, 0) # {'a': 0, 'b': 0, 'c': 0}

# 2nd way
{key: 0 for key in keys} # {'a': 0, 'b': 0, 'c': 0}
```

question id: 1e9cedeb-58c4-4bc8-badf-1d161fd04910


### How to get nested value from a dict without getting an error if some keys does not exist?

For example, you have a dict like this:
```python
user = {"profile": {"address": {"city": 'Moscow'}}} 
```
How to get user's city assuming any key may not present in the dict?


answer
```python
user = {"profile": {"address": {"city": 'Moscow'}}}
user_city = user.get("profile", {}).get("address", {}).get("city", "")
user_city  # Moscow
```

question id: 5dee447c-d5b1-4a0a-a48d-096aefda96a6


### How to make a dict which automatically creates an empty list for each new key? 

answer
Use defaultdict

```python
from collections import defaultdict

animals = defaultdict(list)
animals["Mammal"].append('dog')
animals["Reptile"].append('lizard')
animals["Mammal"].append('cat')

print(animals.items())  # dict_items([('Mammal', ['dog', 'cat']), ('Reptile', ['lizard'])])
```

question id: 7265178a-1850-4224-8d48-4af2f319981d


### How to make this possible?

```python
print(animals)  # {}

animals["Mammal"].append('dog')
animals["Reptile"].append('lizard')
animals["Mammal"].append('cat')

print(animals.items())  # dict_items([('Mammal', ['dog', 'cat']), ('Reptile', ['lizard'])])
```

answer
Use defaultdict

```python
from collections import defaultdict

animals = defaultdict(list)
animals["Mammal"].append('dog')
animals["Reptile"].append('lizard')
animals["Mammal"].append('cat')

print(animals.items())  # dict_items([('Mammal', ['dog', 'cat']), ('Reptile', ['lizard'])])
```

question id: ba706679-b984-4f94-bc18-556d8931b161


### How to make a compound key in a dictionary?

You can use a tuple as a key in your dict
Example
```python
{
    ("Randy", 30): 'programmer', 
    ("Asya", 30): 'pr'
}
```

question id: c8752245-bf3d-406c-bb68-cb913c503965


### How to swap keys and values in a Python dictionary?

Given dict: 	
```python
capitals = {"USA": "Washington", "France": "Paris"}
```

answer

```python
dict(zip(capitals.values(), capitals.keys()))  # {'Washington': 'USA', 'Paris': 'France'}
```

question id: 5e903145-fbb4-43e6-a0b9-3cdf932f4e86


### How to get several values from a dictionary by several keys at once?


```python
some_dict = {"Russia": "Moscow", "France": "Paris", "Germany": "Berlin"}
keys = ("Russia", "France")
```
Expected result:  ['Moscow', 'Paris']

answer
```python
[some_dict.get(key) for key in keys]  # ['Moscow', 'Paris']
```

question id: 75a01a55-b582-4596-8aa1-0c298609e8f2


### How to remove a key from dictionary?

Given dict:
my_dict = {'cats': 9, 'dogs': 7}

answer
```python
# either 
my_dict.pop('key', None)

# or

del my_dict[key]
```

question: 4acd7f62-0aa3-4321-b612-61a3761fc1e9


### What can be a key of a Python dictionary?

Any immutable type, any hashable type. So a tuple can be a key, a list cannot. But tuple have to contain only immutable types too. 
Function can be a key and even closure can be a key. 
Class and instance of class can be a key.

question id: 747e5d04-51ff-416f-a366-20d5f10f0644


### Python: Add key-values in a dictionary only if the key does not exist

answer

```python	
your_dict.setdefault(your_key, your_value)
```

```python
spam = {'name': 'Pooka', 'age': 5} 
spam.setdefault('color', 'black') # 'black' - setdefault() retuns value whether it was by setdefalut or existed before
spam # {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white') # 'black' - we tried to set 'color': 'white', but key 'color' alredy existed with value 'black'
spam  # {'color': 'black', 'age': 5, 'name': 'Pooka'}
```

question id: 3d11d762-2301-4a84-be56-994c0cc7a296


### How to sort a dictionary by values?

Given dict:
	
d = {'z': 23, 'g': 4, 'k': 31}

answer
```python
sorted(d.items(), key=lambda x: x[1])
```

question id: cc6c9031-3d37-4047-908e-9237025a4acd



### What is the output?

```python
counts = {"apples": 1, "oranges": 2}
x, y = counts

print(x, y) # ?
```

answer:

apples, oranges

question id: 72fae45f-5beb-4c7c-9183-7c4feb1115c5


### What are the time complexity of this expression?

```python
some_dict = {}  # let's imagine that there is a lot of key value pais

exists = "whatever" in some_dict.keys()
```

answer
On the one hand, dict.keys() returns a view with a bunch of tuples of key-value pairs and a memnbership test in tuple
is linear (interpreter has to check every tuple if there is the key). However, in Python it is not like that. 
When you make membership test in dict.keys(), Python actually doesn't look through tuple, it still looks in underlying
hash map.

Therefore, 
```python
"whatever" in some_dict.keys()

# has the same O(1) time complexity as

"whatever" in some_dict
```

question id: f0a1a6b7-2cf1-48c7-9252-9c9c856cb35d
