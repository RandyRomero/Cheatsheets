### What is the difference between json and jsonb field types in PostgreSQL?

They are basically the same thing, except that JSONB stores JSON data in a custom format that is 
optimized for querying. jsonb type also has some additional operators for querying.

If you know beforehand that you will not be performing JSON querying operations (much), 
then use the JSON data type. For all other cases, use JSONB.

question id: 8612cffc-ca11-402a-aee8-9c01654e32af


### What does function `jsonb_build_array` do?

Builds a json array from a bunch of given arguments like this:

```sql
json_build_array(1,2,'3',4,5)

-- result: [1, 2, "3", 4, 5]
```

question id: f90eccac-8bc1-44e3-b0c4-0736e083f16c


### What does `@>` operator mean?

answer:
Does the left JSON value contain the right JSON path/value entries at the top level?

example:
```sql
'{"a":1, "b":2}'::jsonb @> '{"b":2}'::jsonb
```

question id: 7f9e09f0-1d31-449c-ac20-4afd151549bf


### How to get a value from a field by a key?

For example, you have json like this in one of your fields
```json
"{"name": "Alice", "agent": {"bot": true} }"
```
and want to return value of "bot" key. How would you do it?

answer
```sql
SELECT you_field_name -> 'agent' -> 'bot' FROM your_table;
```

http://www.silota.com/docs/recipes/sql-postgres-json-data-types.html

question id: f43b6d7c-b8d4-4080-9d37-fac3d2e532d3


### Select rows where "__old" key of the json field of the following table equals 10

```markdown
+--+-----------+---------------------------------------------------------------+
|id|serviceName|entityDiff                                                     |
+--+-----------+---------------------------------------------------------------+
|2 |hrm        |{"weight":{"__old":9.14173309198454,"__new":9.144745974263094}}|
|3 |hrm        |{"weight":{"__old":10,"__new":9.672658683923487}}              |
|4 |hrm        |{"weight":{"__old":9.67265868392349,"__new":9.672658683923487}}|
|5 |hrm        |{"weight":{"__old":9.67265868392349,"__new":9.672658683923487}}|
|6 |hrm        |{"weight":{"__old":9.67265868392349,"__new":9.70183341512058}} |
+--+-----------+---------------------------------------------------------------+
```

answer:
```sql
SELECT * FROM history_entity
WHERE "entityDiff" -> 'weight' ->> '__old' = '10'
LIMIT 10;
```

or
```sql
SELECT * FROM history_entity
WHERE ("entityDiff" -> 'weight' ->> '__old')::float = 10
LIMIT 10;
```

https://www.postgresqltutorial.com/postgresql-json/
https://stackoverflow.com/questions/20236421/how-to-convert-postgres-json-to-integer

question id: 48bba058-8797-4633-b166-e85398f21172


### What's the difference between these two operators - `->` and `->>`?

`->` returns items as JSON objects
`->>`  items as test

https://www.postgresqltutorial.com/postgresql-json/

question id: 85f18aee-564b-4ef7-a8d0-00919fb737e9
