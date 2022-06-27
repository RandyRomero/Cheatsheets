### How to install sqlite3 on Linux?

answer:

via wget / make
not from sudo apt-get install sqlite3
it has very old version

question id: 18975ba2-a5d8-4fa1-bdcb-1c1b4e956165


### How to open a file with a database?

answer:

```
sqlite3 path/to/db
```

question id: 8644978f-00c0-4cd3-a392-18dbf4f625eb


### How to list tables of a database?

answer:
```
.tables
```

Note: no semicolon at the end

question id: f9745762-760e-46fc-a045-91d07e128c70


### How to describe a table?

answer:
```
.schema table_name
```

Note: no semicolon at the end


question id: 93215a7a-2cff-4ec4-b15d-c01c38a43d55


### How to check the type of a value?

```
SELECT typeof(col_name) FROM table_name
```

question id: 36485b4e-2cfc-44b9-94f6-f4ff5d45614c