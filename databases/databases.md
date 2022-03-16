### What's a database?

A database is a collection of information that is organized so 
that it can be easily accessed, managed and updated.

question id: f1704161-1b87-4dec-a93f-8051332e69b6

### What's SQL?

SQL - Structured Query Language - is the programming language that is used to
communicate with a database

question id: acd60e56-34b5-467d-bba2-615acc71a050

### What's JOIN?
An SQL join clause combines columns from one or more tables in a relational database. 
JOIN combines columns from one (self-join) or more tables by using values common to each and 
creates a set that can be saved as a table or used as it is.

question id: 0256627e-b582-49b5-b0d6-b34fcbbc00cb

### Что такое JOIN?
Оператор языка SQL 

Операция соединения, которая предназначена для создания выборки данных из двух таблиц и включения этих данных 
в один результирующий набор. Особенности:

- в схему таблицы-результата входят столбцы обеих исходных таблиц (таблиц-операндов), то есть схема результата 
является «сцеплением» схем операндов;
- каждая строка таблицы-результата является «сцеплением» строки из одной таблицы-операнда со строкой второй 
таблицы-операнда.

question id: 856f6921-9619-476f-8af1-1acfbec4578f

### How many are there types of JOINs and what are they?

ANSI-standard SQL specifies five types of JOIN: 
- INNER
- LEFT OUTER 
- RIGHT OUTER 
- FULL OUTER 
- CROSS

question id: 26195e3d-3f8c-4966-bf31-b5dc421f91c8

https://stackoverflow.com/questions/17946221/sql-join-and-different-types-of-joins

### What's INNER JOIN?

INNER JOIN let's us connect two or more tables by a matching column so that in the resulting column we get
only rows that matches by id or whatever in both tables. If there is some id that present only in one table - they are
thrown away.

syntax:
```sql
SELECT * FROM tableA
INNER JOIN tableB
ON tableA.name = tableB.name
```


two tables
```
id name       id  name
-- ----       --  ----
1  Pirate     1   Rutabaga
2  Monkey     2   Pirate
3  Ninja      3   Darth Vader
4  Spaghetti  4   Ninja
```

output

```
id name       id  name
-- ----       --  ----
1  Pirate     2   Pirate
3  Ninja      4   Ninja
```

question id: 17136448-0554-49fa-b37e-c539a83f2d19

### What's FULL OUTER JOIN and how to use it?

FULL OUTER JOIN produces the set of all records in Table A and Table B, with matching records from both sides where available. 
If there is no match, the missing side will contain null.

two tables
```
id name      | id  name
-- ----      | --  ----
1  Pirate    | 1   Rutabaga
2  Monkey    | 2   Pirate
3  Ninja     | 3   Darth Vader
4  Spaghetti | 4   Ninja
```

the syntax
```sql
SELECT * FROM tableA
FULL OUTER JOIN tableB
ON tableA.name = tableB.name
```

the output
```
id name      id  name
-- ----       --  ----
1  Pirate     2   Pirate
2  Monkey     null  null
3  Ninja      4 Ninja
4  Spaghetti  null null
null null     1   Rutabaga
null null     3   Darth Vader
```

question id: c30d6767-89df-41c4-b2b0-c4b777fe723a

### FULL OUTER JOIN with WHERE or how two find what rows don't have matches in two or more tables

syntax
```sql
SELECT * FROM tableB
FULL OUTER JOIN tableA
ON tableA.col_match == tableB.col_match
WHERE tableA.id IS null OR tableB.id IS null
```

It's an opposite of INNER JOIN

question id: 69ca3758-ad05-4a6a-b7a1-f504c07c0969

### What's LEFT OUTER JOIN and how to use it?

LEFT OUTER JOIN produces a complete set of records from Table A, with the matching records (where available) in Table B. 
If there is no match, the right side will contain null. So the resulting table will have common for both tables rows 
and unique rows from Table A. Unique values from Table B will be thrown away.  

syntax
```sql
SELECT * FROM TableA
LEFT OUTER JOIN TableB
ON TableA.name = TableB.name
```

two tables
```
table A      | table B
id name      | id  name
-- ----      | --  ----
1  Pirate    | 1   Rutabaga
2  Monkey    | 2   Pirate
3  Ninja     | 3   Darth Vader
4  Spaghetti | 4   Ninja
```

the output
```
id  name       id    name
--  ----       --    ----
1   Pirate     2     Pirate
2   Monkey     null  null
3   Ninja      4     Ninja
4   Spaghetti  null  null
```

question id: 43ccdb11-94f7-4c4f-98f3-11189fde0e77


### How to find which stocks does not belong to any watchlist?

For example, you have a table with stocks (id, ticker, company_description etc), a table with For example, you have:
- a table with stocks (id, ticker, company_description etc)
- a table with watchlists (id, name, created_at) 
- m2m table stock_watchlist (stock_id, watchlist_id). 

How to find all stocks that does not belong to any watchlist?

answer 
You need to use LEFT JOIN with WHERE CLAUSE like this:
```sql
SELECT s.ticker FROM stock s
LEFT JOIN stock_watchlist sp ON s.id  = sw.stock_id
WHERE sw.stock_id IS NULL
```

With LEFT JOIN and WHERE clause you can find all items unique for left table

question id: c663ccd4-0dd0-4d49-b2f8-a3093e1de1e6


### What is the use of LEFT JOIN?

With LEFT JOIN and WHERE clause you can find all items unique for left table

For example, you have a table with stocks (id, ticker, company_description etc), a table with For example, you have:
- a table with stocks (id, ticker, company_description etc)
- a table with watchlists (id, name, created_at) 
- m2m table stock_watchlist (stock_id, watchlist_id). 

How to find all stocks that does not belong to any watchlist?

answer 
You need to use LEFT JOIN with WHERE CLAUSE like this:
```sql
SELECT s.ticker FROM stock s
LEFT JOIN stock_watchlist sp ON s.id  = sw.stock_id
WHERE sw.stock_id IS NULL
```

question id: b0aa8023-d069-4c09-ab5f-d4802a73d61f


### What is RIGHT OUTER JOIN?

The same as LEFT OUTER JOIN, but for right handed table

```sql
SELECT * FROM TableA
RIGHT OUTER JOIN TableB
ON TableA.name = TableB.name
```

question id: 1c876eb2-7f60-48ef-86e9-cca61388244f


### What's UNION for?

Basically it stacks result of two or more SELECT statement on each other  and removes the duplicates.

```sql
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

If you do not wish to remove duplicates, try using the UNION ALL operator instead.

question id: a8f1a37b-b7dd-4fb9-9f7e-a225bf30572e

### What's CROSS JOIN? 

The CROSS JOIN is used to generate a paired combination of each row of the first table with each row of the second 
table. This join type is also known as cartesian join.

question id: ebc6c2fc-4d48-4048-a55b-928d0fd7a8e1


### What's primary key? 

A primary key is a column or group of columns used to identify a row uniquely in a table.

If the Primary Key is defined using more that one column, it is known as a Composite Key (or Composite Primary Key). Therefore, a Composite Key in a table does not mean that there are more than one Primary Keys in the table. Instead, a Composite Key uses more than one columns to define a (Single) Primary Key.

question id: e9eecc03-c350-4336-950d-a5d60b7b1273


### What's foreign key?

A Foreign Key is a column or a combination of columns whose values match a Primary Key in a different table. A foreign 
key is a key used to link two tables together.
 

The table that contains the foreign key is called referencing table or child table. 
The table to which the foreign key references is called referenced table or parent table.

A table can have multiple foreign keys depending on its relationship with other tables.


question id: afd09dca-98e2-40af-a92b-a9052a73154e

### What are constraints?

Constraints are the rules enforced on data columns on table.
There are used to prevent invalid data from being entered into the database.
This ensures the accuracy and reliability of the data in the database.
Two main categories are column constraints and table constraints.

question id: 24126465-4bad-42cc-a98b-132b40bd78d6

### What are the most common column constraints?

- NOT NULL
- UNIQUE 
- PRIMARY key
- FOREIGN key
- CHECK (for some custom conditions)
- EXCLUSION (too long to explain here)

question id: 3f8558f2-9150-4145-8cf6-8cdd43cf9cba

### What are the most common table constraints? 

- CHECK - to check a condition when inserting or updating data
- REFERENCES - to constrain the value stored in the column that must exist in a column in another table
- UNIQUE (column_list) - forces the values stored in the columns listed inside the parentheses to be unique
- PRIMARY KEY(column_list) - allows you to define the primary key that consists of multiple columns

question id: bf5908f8-f7f8-4d85-9d10-4b2e4207f1be

### General syntax for defining a field as a foreign key on creating a table

```sql
CREATE TABLE your_table_name(
    id SERIAL PRIMARY KEY,
    your_fk_field_name INT REFERENCES other_table_name(other_table_pk_name) ON DELETE CASCADE;
)
```

question id: 39e3127e-eab8-43a8-9ea4-844fec20577c


### How to define a foreign key constraint on creating a new table?

Given these tables below, how to specify that contacts.customer_id is a foreign key referencing customers.customer_id?
```sql
CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);

-- and

CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
);
```

answer:

```sql
CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT REFERENCES customers(customer_id) ON DELETE CASCADE,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
);
```

question id: 7c18b805-479a-4512-98e5-b1105f673e2b


### General syntax for defining a foreign key for an existing table

```sql
ALTER TABLE child_table
ADD CONSTRAINT constraint_name
FOREIGN KEY (fk_columns)
REFERENCES parent_table(parent_key_columns)
ON DELETE CASCADE;
```

question id: 9087211c-9978-47a8-8000-f46dbc5e8478


### How to define foreign key for existing table?

Given these tables below, how to specify that contacts.customer_id is a foreign key referencing customers.customer_id?
```sql
CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);

-- and

CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
);
```

answer:

```sql
ALTER TABLE contacts
ADD CONSTRAINT fk_contacts_id_customers_id
FOREIGN KEY (contact_id)
REFERENCES customers(customers_id)
ON DELETE CASCADE;
```

question id: a9c21d6d-c0b6-4886-8e16-efc8b6edc02d


### What are ON DELETE actions in PostgreSQL and which one is the default one?

SET NULL
SET DEFAULT
RESTRICT
NO ACTION
CASCADE

The default is NO ACTION

question id: ffc9cdcb-71b1-4947-8afc-0c4a42a4994f

### What is the behavior of ON DELETE NO ACTION constraint?

When you attempt to remove a row from a parent table which (the row) is referenced in the child table, you'll get
an error that the row you are trying to remove is still referenced from your child table.

question id: e000777b-8114-4ce1-9db1-e1193ebf67e8


### What is the behavior of ON DELETE RESTRICT constraint?

RESTRICT prevents deletion of a referenced row. The essential difference between RESTRICT and NO ACTION is that 
NO ACTION allows the check to be deferred until later in the transaction, whereas RESTRICT does not.)

question id: 


### What is the behavior of ON DELETE SET NULL constraint?

The SET NULL automatically sets NULL to the foreign key columns in the referencing rows of the child table when the 
referenced rows in the parent table are deleted.

Note: you will get an error if your have NOT NULL constraint on your foreign key field.

question id: 447781fa-7704-40d7-805f-28c9588d61d3


### What is the behavior of ON DELETE CASCADE constraint?

The ON DELETE CASCADE automatically deletes all the referencing rows in the child table when the referenced rows in the
parent table are deleted. In practice, the ON DELETE CASCADE is the most commonly used option.

question id: d7dba2b9-049a-4a68-a3dc-ff5eaa501b19

### Give an example where do we need ON DELETE SET DEFAULT action?

For example with have a table with users and a table with themes. One user can choose only one theme, but themes can
have a lot of users. What would happen if a theme is removed? With ON DELETE CASCADE all users, who were referencing on
this theme, would be remove too! But is we set ON DELETE SET DEFAULT, after removing a theme its users we be referencing
to some default theme.

question id: 9c6cd21d-2697-45c4-8af5-da57d8a89435

 
### Name some appropriate type for a primary key based on id

SERIAL or BIGSERIAL 

Because it's basically autoincrementing integer

question id: 33da1283-7f45-484b-b741-3e764f1f0f69


### Whe one-to-one relationship is most useful? 

When one objects extends somehow another one.

question id: 16f661b1-b23e-4b12-b480-bb24960e460f


### What's pooling?

Establishing a connection to a database server is an expensive operation. Connection pools are a common technique 
allowing to avoid paying that cost. A pool keeps the connections open and leases them out when necessary.

question id: 01468ceb-4c32-4d1b-b649-c4fd7960a1f2


### What's atomicity? 

Atomicity means that in a transaction either all steps are completed or no step is completed

question id: c929bd84-bbcb-46fc-8108-ecc4467b5056


### What's sharding(шардирование)?

Sharding is a database architecture pattern related to horizontal partitioning — the practice of separating one 
table’s rows into multiple different tables, known as partitions. Each partition has the same schema and columns, 
but also entirely different rows. Likewise, the data held in each is unique and independent of the data held in other 
partitions.

Sharding involves breaking up one’s data into two or smaller chunks, called logical shards. The logical shards 
are then distributed across separate database nodes, referred to as physical shards, which can hold multiple logical 
shards. Despite this, the data held within all the shards collectively represent an entire logical dataset.

https://www.digitalocean.com/community/tutorials/understanding-database-sharding

question id: 1a7872c5-36e5-4b85-9e87-6a2366e785d3
