### Open postgres command line from docker:
`docker exec -it name_of_your_container psql -U postgres`

question id: 46f48733-d907-4172-a07b-36c03853c1c5

### Create a database:
`CREATE DATABASE database_name;`

question id: 8813ca8e-ffc4-4ef8-be6f-d57095499e01

### Create a user with encrypted password:
`CREATE USER user_name with ENCRYPTED PASSWORD 'your_password_here';`

question id: e1046c71-04cd-4da4-8c5c-9c9e10fd620d

### List users:
`\du`

question id: 358074d2-aa74-4002-bf5c-4fe35eebe9d8


### Grant all privileges for user on database and all the tables, sequences, functions, views in it:
`GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_user_name;`

also (you have to be connected to the right database)
```
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public to your_user_name;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public to your_user_name;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public to your_user_name;
```

https://stackoverflow.com/questions/15520361/permission-denied-for-relation

question id: 8c06baed-54f9-46e9-81a5-feaf4c77efe9


### How to grant some privileges by default for a user/schema?

```
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO username
```

https://blog.dbi-services.com/a-wonderful-postgresql-feature-default-privileges/

question id: d44a798a-d953-401d-ad66-03ede2e4dd9b


### List databases:
`\l`

question id: b0b35a76-04a3-4775-b3a9-ac156508f802

### Choose a database:
`\c your_database_name`

question id: df6642aa-38f2-4c20-9fc2-0f2c35560300

### Show tables:
`\dt`

NB: only get a listing of tables in the current schema (public by default).

question id: a5244381-f546-436e-929b-5ef4b8d40e8c


### How to list table in all schemas? 

answer:

`\dt *.*`

question id: 541754a1-16c1-4881-bdaf-007ecb557102


### How to list tables of a particular schema?

answer:

`\dt your_schema.*`

question id: 18d8b748-0702-477f-afc0-dfdb1240034


### Describe a table:
`\d+ your_table_name`

question id: 2e8f8dac-55e1-466d-bafe-4a15cc4198d7


### Insert a row into a table:
```sql
INSERT INTO ms_users(login, password) VALUES ('some_login', 'some_password');
```

question id: 60dd795c-52fe-4094-9129-08a09cce9cd3


### How to insert several rows at once?

For example you have a table like this:

```sql
CREATE TABLE links (
    id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
);
```

and you want to insert this list of values 
```python
[('https://www.google.com','Google'), ('https://www.yahoo.com','Yahoo'), ('https://www.bing.com','Bing')]
```

How would you do that?

answer

```sql
INSERT INTO 
    links (url, name)
VALUES
    ('https://www.google.com','Google'),
    ('https://www.yahoo.com','Yahoo'),
    ('https://www.bing.com','Bing');
```

question id: b2be6c48-433e-4482-adec-bd861605ce0f


### How to alter a type of column?
```sql
ALTER TABLE ms_tasks ALTER COLUMN client_id TYPE integer USING client_id::integer;
```

USING client_id::integer - means to convert existing data to the new format

https://www.postgresqltutorial.com/postgresql-change-column-type/

question id: f28c2140-5420-450f-a054-605ca2e537e8

### drop database:
`Drop database your_database_name;`

question id: 813e0510-cbd7-4a1b-8d0d-8a23a9324445

### Let a user create databases:
```sql
ALTER USER username CREATEDB;
```

question id: cf3f0ff9-005d-4290-84b6-be8bec68425a

### List schemas:
```shell
\dn
```

question id: 005f69cf-32c2-4c03-ac00-b67f085e0b69


### What's schema?

A schema is a named collection of tables. A schema can also contain views, indexes, sequences, data types, operators, 
and functions. Schemas are analogous to directories at the operating system level, except that schemas cannot be nested.

question id: 62ff0327-ca66-4a2b-b508-bf0e5c5746d3


### Select last N rows
```sql
SELECT * FROM table_name ORDER BY id DESC LIMIT N;
```

question id: 6707371d-566a-42e7-88eb-cb9b894e9530

### Count occurrences
```sql
SELECT col_name, COUNT(col_name) AS num_of_occurrences
FROM table_name
GROUP BY col_name
ORDER BY num_of_occurrences DESC
LIMIT 10;
```

question id: 9e38b08e-6a66-47ec-abd6-07a4be7743b2

### List only unique values from a column
```sql
SELECT DISTINCT column_name FROM table_name;
```

question id: 0b91a8b5-b67f-4bf3-848f-bdfb3a08450d


### What is the difference between DISTINCT and DISTINCT ON in PostgreSQL?

First of all, DISTINCT ON exists only in PostgreSQL, it is not a part of official SQL.

DISTINCT removes duplicate rows. Where there all values in all columns are the same. What columns? Each and every 
column that you denote after SELECT statement. 

DISTINCT ON(column or column list) returns only the first row from a group of similar rows where specified column or column
list is/are the same. But there are some pitfalls:
The order of rows returned from the SELECT statement is unspecified therefore the “first” row of each group of the 
duplicate is also unspecified. You can specify which row should be returned first by specifying it in ORDER BY.
For example, you DISTINCT ON(name), but there are several rows where names are identical, but other fields not. So
which one should be returned? 
The problem is that to specify the order for DISTINCT ON you use the same ORDER BY that you use for the whole query.
Even worse, columns that are in DISTINCT ON should present from the left to right in ORDER BY of the whole query.
So if you want to use DISTINCT ON(name) and want to order duplicate rows by name, but the whole queryset by other 
column, you are screwed :) In this case you have to use subquery to order your rows again. 

https://www.postgresqltutorial.com/postgresql-select-distinct/

question id: 98b48c3d-bc48-4017-86d8-1bad40082ad6


### How to count a number of rows in a table?
```sql
SELECT COUNT(*) FROM table_name;
```

question id: d7601e45-df50-45ba-b49b-f80e613c4d84

### How to figure out what is the number of unique items in a column?
```sql
SELECT COUNT(DISTINCT(column_name)) FROM table_name;
```

question id: 736873f3-30ad-4a42-bb6f-04c37774ba5c

### Select all customers with name Jerry 33 who is also 33 years old
```sql
SELECT * FROM customer 
WHERE name = 'Jerry' AND age >= 33;
```

question id: 74174449-98a1-4e84-ad49-72f728997018


### Count all movies that was not shot in Japan
```sql
SELECT COUNT(*) FROM movie WHERE country != "Japan";
```

question id: ed2ae79c-a733-4f88-b685-8a5ace4d5b88

### Select all customers and order them by first_name in 1) ascending order 2) descending order
```sql
SELECT * FROM customer ORDER BY first_name;

SELECT * FROM customer ORDER BY first_name DESC;
```

question id: ed073086-5bb7-4bd9-a1cf-6ad0bc6d4f7d

### Select companies and order them by name and by sales
```sql
SELECT * FROM company ORDER BY name, sales;
```

Postgres will sort companies first by name, then by sales 
so you'll get something like this

Apple - 100

Apple - 300

Google - 200

Google - 500

Xerox - 100

question id: ca739532-74e1-40e3-b14f-536297261d78

### Select all customers, order them by name starting with Z and by age starting from the youngest one:
```sql
SELECT * FROM customer ORDER BY first_name DESC, age ASC;
```

question id: af4a5e83-6d4a-4cfc-8dd4-715a02f68565

### Select five shortest movie from 'film' table (title, length)
```sql
SELECT title, length FROM film ORDER BY length LIMIT 5; 
```

question id: 78540f21-e630-4ccb-a4aa-7c4183d90e0c

### How many films are there less than 50 minutes in film table? (title, length)
```sql
SELECT COUNT(*) FROM film WHERE length <= 50;
```

question id: a9768d17-c43c-4dd4-abba-5fb3a264dd57

### Are BETWEEN and NOT BETWEEN statements inclusive?

BETWEEN is inclusive (BETWEEN x AND y is the same as x >= your_value <=y)
NOT BETWEEN is exclusive (x < your_value > y)

question id: ac3f74d9-51b9-46d2-a524-de60c4e806d0

### Select all rows from `some_table` by column `year` where year is at least or 1932 and not greater than 2000
```sql
SELECT * FROM some_table WHERE year BETWEEN 1932 AND 2000;
```

question id: 31f8f83c-136f-4afc-9e93-2266244108f5


### Select rows of people born not in 1990, 1991, 1992
```sql
SELECT * FROM people WHERE age NOT BETWEEN 1990 AND 1992;
```

1988

1989

1993

...

question id: 2475d169-92b8-4a91-aa59-7451ad7595f8

### Select all people with ids 1, 23, 98, 34
```sql
SELECT * FROM people WHERE id IN (1, 23, 98, 34);
```

question id: 99c8aa1c-1d54-4fe0-a97b-cff090f5f215

### Select all the people apart from who have names "Max", "Beth", "Rex"
```sql
SELECT * FROM people WHERE first_name NOT IN ('Max', 'Beth', 'Rex');
```

question id: bfb3c6c2-5bfc-4caa-b5bf-2be0f9514e01

### What the difference between LIKE and ILIKE?
ILIKE is case-insensitive 

question id: 60e6f903-9ae8-4c69-9157-23316ce21016

### Count all people whose name starts with "J" and last name starts with "S"
```sql
SELECT COUNT(*) FROM people 
WHERE first_name LIKE 'J%' AND last_name LIKE 'S%';
```

question id: d9cd7ece-2ae4-474f-95b1-282aab1a6f09

### Select people whose first name start with "A" and last name doesn't start with "B", order by last name
```sql
SELECT * FROM people
WHERE first_name LIKE 'A%' AND last_name NOT LIKE 'B%'
ORDER BY last_name;
```

question id: 8cda25e9-5e73-4ece-bb6b-aa5dba02bbc4

### Count all films that have a word Truman somewhere in their title
```sql
SELECT COUNT(*) FROM film WHERE title LIKE '%Truman%';
```

question id: bf0fa324-38a0-4ac7-acc8-c9d776c4cdee

### Get an average length of a movie in a film column
```sql
SELECT ROUND(AVG(length), 2) FROM film;
```

question id: 7ccaace7-10c4-46bf-920e-a14201bb7805

### Get sum of length of all movies
```sql
SELECT SUM(length) FROM film;
```

question id: 979da9df-054e-4196-a41e-22460152ee4c

### Find the maximum payment from payment table
```sql
SELECT MAX(amount) FROM payment;
```

question id: 03c5880d-a58f-4668-a8cb-07a419d3190c

### Find the length of the shortest film
```sql
SELECT MIN(length) FROM film;
```

question id: 467c289b-6d5f-4c92-996a-c04ccbe75c63


### Find the shortest film

```sql
SELECT * FROM film
ORDER BY length
LIMIT 1
```

question id: 9c923df8-da54-4048-b596-c139d3773e6e


### Find min and max length of films in a film table
```sql
SELECT MIN(length), MAX(length) FROM film;
```

question id: a0d8adc2-64c0-46ed-b311-032339fad8c3

### Show 5 customers who has spent in dvdrental the most - from top to bottom by amount which each of them has spent in total. Table: payment. Columns: customer_id, amount.
```sql
SELECT customer_id, SUM(amount) FROM payment
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5;
```
output
```
 customer_id |  sum   
-------------+--------
         148 | 211.55
         526 | 208.58
         178 | 194.61
         137 | 191.62
         144 | 189.60
```

question id: d1a2ba22-bb7e-42ed-b7a6-7b7065b6d7ae

### Show 5 customers with the least number of payments (transaction-wise). Table: payment. Columns: customer_id, payment_id.
```sql
SELECT customer_id, COUNT(payment_id)
FROM payment
GROUP BY customer_id
ORDER BY COUNT(payment_id)
LIMIT 5;
```

output
```bash
 customer_id | count 
-------------+-------
         318 |     7
         281 |    10
         110 |    12
         272 |    13
          61 |    13
```

question id: 8f1582f2-f500-49c7-8a78-374e52326c77


### Figure out how much every customer spends with every staff person.

Table payment:
```
 customer_id | staff_id | amount 
-------------+----------+--------
         341 |        2 |   7.99
         341 |        1 |   1.99
         341 |        1 |   7.99
         341 |        2 |   2.99
         341 |        2 |   7.99
         341 |        1 |   5.99
         342 |        2 |   5.99
         ... |      ....|   ....
```

answer: 

```sql
SELECT customer_id, staff_id, SUM(amount) FROM payment
GROUP BY staff_id, customer_id
ORDER BY customer_id, staff_id;
```

output:

```
customer_id | staff_id |  sum   
-------------+----------+--------
           1 |        1 |  60.85
           1 |        2 |  53.85
           2 |        1 |  55.86
           2 |        2 |  67.88
           3 |        1 |  59.88
           3 |        2 |  70.88
```

question id: f3772302-8b28-443e-892c-368a35d5163a


### Convert timestamp to a date
question:
Table payment.
```
        payment_date        
----------------------------
 2007-02-15 22:25:46.996577
 2007-02-16 17:23:14.996577
 2007-02-16 22:41:45.996577
 2007-02-19 19:39:56.996577
 2007-02-20 17:31:48.996577
 2007-02-21 12:33:49.996577
```

answer
```sql
SELECT DATE(payment_date) FROM payment;
```

```
date    
------------
 2007-02-15
 2007-02-16
 2007-02-16
 2007-02-19
 2007-02-20
 2007-02-21
 2007-02-17
```

question id: 384142a2-4569-4e72-9fb7-4d85dda7da3f


### Show total sum of earning by each day having this table:
Table: payment
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

answer
```sql
SELECT DATE(payment_date), SUM(amount) FROM payment
GROUP BY DATE(payment_date)
ORDER BY DATE(payment_date)
LIMIT 100;
```

output:
```
 date    |   sum   
------------+---------
 2007-02-14 |  116.73
 2007-02-15 | 1188.92
 2007-02-16 | 1154.18
 2007-02-17 | 1188.17
 2007-02-18 | 1275.98
 2007-02-19 | 1290.90
```

question id: 6eb055d8-328f-43d7-b8ee-68c91d472dc6

### Who gets the bonus?
We have two staff members, with Staff IDs 1 and 2. We want to give a bonus to the staff member that handled 
the most payments. (MOst in terms of number of payments processed, not total dollar amount).
How many payments did each staff member handle and who gets the bonus?

Table: payment;

```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

answer
```sql
SELECT staff_id, COUNT(payment_id) FROM payment
GROUP BY staff_id
ORDER BY COUNT(payment_id) DESC;
```

output
```
 staff_id | count 
----------+-------
        2 |  7304
        1 |  7292
```

question id: 2c78d675-f45c-4767-bc54-2f9f2d128834

### Show average rental rate per movie rating having the following table
Table: film
```
       title       | rental_rate | rating 
-------------------+-------------+--------
 Chamber Italian   |        4.99 | NC-17
 Grosse Wonderful  |        4.99 | R
 Airport Pollock   |        4.99 | R
 Bright Encounters |        4.99 | PG-13
```

answer 

```sql
SELECT rating, ROUND(AVG(rental_rate), 2) average_rental_rate FROM film
GROUP BY rating
ORDER BY AVG(rental_rate);
```

output
```
 rating | average_rental_rate 
--------+-------
 G      |  2.89
 R      |  2.94
 NC-17  |  2.97
 PG-13  |  3.03
 PG     |  3.05

```

question id: 64dc258b-5a50-4f6c-9740-77ff612225dd

### Who has spent the most?
Show five customers who spent the most money in dvdrental with the total amount of their spendings and total number of their transactions
Table: payment;

```
+----------+-----------+--------+---------+------+--------------------------+
|payment_id|customer_id|staff_id|rental_id|amount|payment_date              |
+----------+-----------+--------+---------+------+--------------------------+
|17518     |343        |1       |3407     |0.99  |2007-02-21 14:42:28.996577|
|17519     |344        |1       |1341     |3.99  |2007-02-15 10:54:44.996577|
|17520     |344        |2       |1475     |4.99  |2007-02-15 19:36:27.996577|
|17521     |344        |1       |1731     |0.99  |2007-02-16 14:00:38.996577|
|17522     |345        |2       |1210     |0.99  |2007-02-15 01:26:17.996577|
|17523     |345        |1       |1457     |4.99  |2007-02-15 18:34:15.996577|
|17524     |345        |2       |1550     |0.99  |2007-02-16 00:27:01.996577|
|17525     |345        |2       |2766     |4.99  |2007-02-19 16:13:41.996577|
|17526     |346        |1       |1994     |5.99  |2007-02-17 09:35:32.996577|
|17527     |346        |2       |3372     |2.99  |2007-02-21 12:02:45.996577|
+----------+-----------+--------+---------+------+--------------------------+
```

answer

```sql
SELECT customer_id, SUM(amount) AS total_amount, COUNT(*) total_num_transactions FROM payment
GROUP BY customer_id
ORDER BY total_amount DESC
LIMIT 5;
```

output

```
+-----------+------------+----------------------+
|customer_id|total_amount|total_num_transactions|
+-----------+------------+----------------------+
|148        |211.55      |45                    |
|526        |208.58      |42                    |
|178        |194.61      |39                    |
|137        |191.62      |38                    |
|144        |189.6       |40                    |
+-----------+------------+----------------------+
```

question id: 0bdf57f7-704e-4091-b166-3a12276f7f87


### How many there are bookings started in August of 2008?

table cd.bookings, column starttime

```markdown
+------+-----+-----+--------------------------+-----+
|bookid|facid|memid|starttime                 |slots|
+------+-----+-----+--------------------------+-----+
|0     |3    |1    |2012-07-03 11:00:00.000000|2    |
|1     |4    |1    |2012-07-03 08:00:00.000000|2    |
|2     |6    |0    |2012-07-03 18:00:00.000000|2    |
|3     |7    |1    |2012-07-03 19:00:00.000000|2    |
|4     |8    |1    |2012-07-03 10:00:00.000000|1    |
|5     |8    |1    |2012-07-03 15:00:00.000000|1    |
|6     |0    |2    |2012-07-04 09:00:00.000000|3    |
|7     |0    |2    |2012-07-04 15:00:00.000000|3    |
|8     |4    |3    |2012-07-04 13:30:00.000000|2    |
|9     |4    |0    |2012-07-04 15:00:00.000000|2    |
+------+-----+-----+--------------------------+-----+
```

```sql
SELECT COUNT(*) FROM cd.bookings
WHERE starttime >= '2012-08-01' AND starttime < '2012-09-01';
```

there should be 1472 items


question id: 42286ce3-948f-4621-9cd4-99031ed55f58


### Who spent the most in a specific month?
Show five customers who spent the most money in dvdrental during April of 2007 with the total amount of their spendings and total number of their transactions
Table: payment;

```
 customer_id | amount |        payment_date        
-------------+--------+----------------------------
         341 |   7.99 | 2007-02-15 22:25:46.996577
         341 |   1.99 | 2007-02-16 17:23:14.996577
         341 |   7.99 | 2007-02-16 22:41:45.996577
         341 |   2.99 | 2007-02-19 19:39:56.996577
         341 |   7.99 | 2007-02-20 17:31:48.996577
```

answer 

```sql
SELECT customer_id, SUM(amount), COUNT(*) FROM payment
WHERE DATE(payment_date) >= '2007-04-01' AND DATE(payment_date) < '2007-05-01'
GROUP BY customer_id
ORDER BY SUM(amount) DESC
LIMIT 5;
```

output

```
 customer_id |  sum   | count 
-------------+--------+-------
         148 | 100.78 |    22
         522 |  97.81 |    19
         470 |  96.83 |    17
         137 |  96.81 |    19
         144 |  93.82 |    18
```

question id: 02c7bdcf-17cb-458c-8b4d-55307746b373

### Count how many customers associated with each store

Show only stores with more than 300 unique customers.
Resulting table has to have store_id and correspondent number of accociated customers.

Table: customer

```
 store_id | customer_id | first_name | last_name |                email                
----------+-------------+------------+-----------+-------------------------------------
        1 |         524 | Jared      | Ely       | jared.ely@sakilacustomer.org
        1 |           1 | Mary       | Smith     | mary.smith@sakilacustomer.org
        1 |           2 | Patricia   | Johnson   | patricia.johnson@sakilacustomer.org
        1 |           3 | Linda      | Williams  | linda.williams@sakilacustomer.org
        2 |           4 | Barbara    | Jones     | barbara.jones@sakilacustomer.org
```


answer
```sql
SELECT store_id, count(customer_id) FROM customer
GROUP BY store_id
HAVING COUNT(*) > 300;
```

output

```
 store_id | count 
----------+-------
        1 |   326
```

question id: dd4049de-40e5-4ad1-b71c-024a16705cf6

### Select customers with more than 40 transactions
Table: payment;
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

answer
```sql
SELECT customer_id, COUNT(*) FROM payment
GROUP BY customer_id
HAVING COUNT(*) > 40
ORDER BY COUNT(*) DESC;
```

output

```
 customer_id | count 
-------------+-------
         148 |    45
         526 |    42
```

question id: 76b25b3f-b5cf-4a51-9da9-428a40f04d35

### What are customers ids of customers who have spent more than $100 in payment transactions with our staff id memnber 2?
Table: payment

```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

answer
```sql
SELECT customer_id, SUM(amount) FROM payment
WHERE staff_id = 2
GROUP BY customer_id
HAVING SUM(amount) > 100
ORDER BY SUM(amount) DESC;
```

output

```
 customer_id |  sum   
-------------+--------
         187 | 110.81
         148 | 110.78
         211 | 108.77
         522 | 102.80
         526 | 101.78
```

question id: 105014d7-8107-4536-af61-e139f2dc1ba6 

### What are emails of customers who live in California district?
Tables: customer, address;

customer table
```
 customer_id | address_id | first_name | last_name 
-------------+------------+------------+-----------
         524 |        530 | Jared      | Ely
           1 |          5 | Mary       | Smith
           2 |          6 | Patricia   | Johnson
           3 |          7 | Linda      | Williams
           4 |          8 | Barbara    | Jones

```

address table 
```
 address_id |              address               |    district    | postal_code 
------------+------------------------------------+----------------+-------------
          6 | 1121 Loja Avenue                   | California     | 17886
         11 | 900 Santiago de Compostela Parkway | Central Serbia | 93896
         18 | 770 Bydgoszcz Avenue               | California     | 16266
         28 | 96 Tafuna Way                      | Crdoba         | 99865
         42 | 269 Cam Ranh Parkway               | Chisinau       | 34689
```

answer

Here we need just a simple INNER JOIN and a WHERE clause
```sql
SELECT email, district FROM customer
INNER JOIN address ON customer.address_id = address.address_id
WHERE district = 'California';
```

output
```
                email                 |  district  
--------------------------------------+------------
 patricia.johnson@sakilacustomer.org  | California
 betty.white@sakilacustomer.org       | California
 alice.stewart@sakilacustomer.org     | California
 rosa.reynolds@sakilacustomer.org     | California
 renee.lane@sakilacustomer.org        | California
 kristin.johnston@sakilacustomer.org  | California
 cassandra.walters@sakilacustomer.org | California
 jacob.lance@sakilacustomer.org       | California
 rene.mcalister@sakilacustomer.org    | California
```

question id: 1c4b4549-014f-41dc-a854-e9a593fbe71c


### Get all the film titles with Nick Wahlberg in it
Tables: film, actor, film_actor;

table film
```
       title       | film_id | release_year | length 
-------------------+---------+--------------+--------
 Chamber Italian   |     133 |         2006 |    117
 Grosse Wonderful  |     384 |         2006 |     49
 Airport Pollock   |       8 |         2006 |     54
 Bright Encounters |      98 |         2006 |     73
 Academy Dinosaur  |       1 |         2006 |     86
```

table actor
```
 actor_id | first_name |  last_name   |      last_update       
----------+------------+--------------+------------------------
        1 | Penelope   | Guiness      | 2013-05-26 14:47:57.62
        2 | Nick       | Wahlberg     | 2013-05-26 14:47:57.62
        3 | Ed         | Chase        | 2013-05-26 14:47:57.62
        4 | Jennifer   | Davis        | 2013-05-26 14:47:57.62
        5 | Johnny     | Lollobrigida | 2013-05-26 14:47:57.62
```

table film_actor
```
actor_id | film_id |     last_update     
----------+---------+---------------------
        1 |       1 | 2006-02-15 10:05:03
        1 |      23 | 2006-02-15 10:05:03
        1 |      25 | 2006-02-15 10:05:03
        1 |     106 | 2006-02-15 10:05:03
        1 |     140 | 2006-02-15 10:05:03
```

answer
We actually join here two tables via the third one because they have m2m connection

```sql
SELECT film.film_id, title, first_name, last_name
 FROM film
     INNER JOIN film_actor fa ON film.film_id = fa.film_id
     INNER JOIN actor ON actor.actor_id = fa.actor_id
 WHERE actor.first_name = 'Nick'
   AND actor.last_name = 'Wahlberg';
```

output

```
 film_id |       title       | first_name | last_name 
---------+-------------------+------------+-----------
       3 | Adaptation Holes  | Nick       | Wahlberg
      31 | Apache Divine     | Nick       | Wahlberg
      47 | Baby Hall         | Nick       | Wahlberg
     105 | Bull Shawshank    | Nick       | Wahlberg
     132 | Chainsaw Uptown   | Nick       | Wahlberg
     145 | Chisum Behavior   | Nick       | Wahlberg
     226 | Destiny Saturday  | Nick       | Wahlberg
     249 | Dracula Crystal   | Nick       | Wahlberg
```

There are should be 25 movies in total

question id: 6da6eb22-59c6-4e6e-843d-4d1d0e5845f1

### What movies do we have in database that we do not have in inventory? 

Table film
```
 film_id |       title       | release_year | length | rental_rate 
---------+-------------------+--------------+--------+-------------
     133 | Chamber Italian   |         2006 |    117 |        4.99
     384 | Grosse Wonderful  |         2006 |     49 |        4.99
       8 | Airport Pollock   |         2006 |     54 |        4.99
      98 | Bright Encounters |         2006 |     73 |        4.99
       1 | Academy Dinosaur  |         2006 |     86 |        0.99

```

table inventory

```
 inventory_id | film_id | store_id |     last_update     
--------------+---------+----------+---------------------
            1 |       1 |        1 | 2006-02-15 10:09:17
            2 |       1 |        1 | 2006-02-15 10:09:17
            3 |       1 |        1 | 2006-02-15 10:09:17
            4 |       1 |        1 | 2006-02-15 10:09:17
            5 |       1 |        2 | 2006-02-15 10:09:17

```

answer

We are gonna use `LEFT OUTER JOIN` with `WHERE` clause to find which items form the left table do not present
 in the right table

```sql
SELECT film.film_id, title, inventory_id
FROM film
         LEFT OUTER JOIN inventory ON film.film_id = inventory.film_id
WHERE inventory.film_id IS NULL;
```

output 

```
 film_id |         title          | inventory_id 
---------+------------------------+--------------
      14 | Alice Fantasia         |             
      33 | Apollo Teen            |             
      36 | Argonauts Town         |             
      38 | Ark Ridgemont          |             
      41 | Arsenic Independence   |             
      87 | Boondock Ballroom      |             
     108 | Butch Panther          |             
     128 | Catch Amistad          |             
```

question id: 96f94ba7-c70a-468e-98a6-9e474cda4934

### Get timezone that Postgres is using

```sql
SHOW TIMEZONE;
```

question id: 7f8a1238-7b21-4119-aa26-d16961e57972

### Get current timestamp with timezone

```sql
SELECT NOW();
```

question id: 2abcb5fe-3dee-45f9-9ad6-0d6fcd9e4596

### Get current time and date in human readable format

```sql
SHOW TIMEOFDAY();
```

output: 
Wed Jan 27 10:00:27.984837 2021 UTC

question id: f9bc61f6-037a-4a00-bf4b-903299238b80

### Get current date

```sql
SELECT CURRENT_DATE;
```

output

2021-01-27

question id: 17eb0b70-f7aa-4511-a850-a9c88d46e0d1

### Get current time

```sql
SELECT CURRENT_TIME;
```

output

10:07:08.406317+00

question id: 29000548-fafc-4359-94fb-23e762c9f7db

### Make a new column with just a year component from a timestamp  

```sql
SELECT EXTRACT(YEAR FROM col_name) AS new_col_name FROM table_name;
```

Could be not only year, but a bunch of different things:

```
microseconds
milliseconds
second
minute
hour
day
week
month
quarter
year
decade
century
millennium
```

question id: 49a20169-7334-4970-9b85-d1cddae56eeb

### How to get how many time has gone since some timestamp in a table

table customer

```
 customer_id | first_name | last_name |       last_update       
-------------+------------+-----------+-------------------------
         524 | Jared      | Ely       | 2013-05-26 14:49:45.738
           1 | Mary       | Smith     | 2013-05-26 14:49:45.738
           2 | Patricia   | Johnson   | 2013-05-26 14:49:45.738
           3 | Linda      | Williams  | 2013-05-26 14:49:45.738
           4 | Barbara    | Jones     | 2013-05-26 14:49:45.738

```

Expected output:
```
 customer_id |      since_last_update      
-------------+-----------------------------
         524 | 7 years 8 mons 09:10:14.262
           1 | 7 years 8 mons 09:10:14.262
           2 | 7 years 8 mons 09:10:14.262
           3 | 7 years 8 mons 09:10:14.262
           4 | 7 years 8 mons 09:10:14.262
```

answer


```sql
SELECT customer_id, AGE(last_update) AS since_last_update FROM customer LIMIT 5;
```


question id: 1cfde4ee-9481-46c6-a7ba-4681ae6ff683

### How to get timestamp in any format you want?

```sql
SELECT T0_CHAR(col_name, 'dd-MM-YYY') FROM table_name;
```

format in quotes are described here

https://www.postgresql.org/docs/12/functions-formatting.html

question id: 442d3644-397f-4cb7-be91-0bd7684efcae


### Get a column of months when payments occurred 

table payment
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

expected result

```
 month_of_payment 
------------------
 MARCH    
 MAY      
 FEBRUARY 
 APRIL   
```

answer

```sql
SELECT DISTINCT(TO_CHAR(payment_date, 'MONTH')) AS month_of_payment 
FROM payment;
```

question id: eff67116-408d-45b4-b41b-c4c5dca06853


### What is an order of argument for to_char()? 

answer:
Use to_char(expression/field_name, format)

For example:
```sql
SELECT DISTINCT(TO_CHAR(payment_date, 'MONTH')) AS month_of_payment 
FROM payment;
```

```
 month_of_payment 
------------------
 MARCH    
 MAY      
 FEBRUARY 
 APRIL   
```

https://www.postgresqltutorial.com/postgresql-to_char/

question id: 55e0179e-7dcf-4a6a-a06f-8e7ea5bc57ad



### How many are there payments made on Monday?

table payment
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

answer

We can extract day of a week for every timestamp and count by that

```sql
SELECT COUNT(*) FROM payment;
WHERE EXTRACT(DOW FROM payment_date) = 1;
```

output
```
 count 
-------
  2948
```

question id: 779e2972-0bed-4b06-9c1a-3b07b8c9462e

### Make a new column by calculating deposit value for a movie to be 10% of it's replacement cost

table film
```
 film_id |       title       | release_year | replacement_cost 
---------+-------------------+--------------+------------------
     133 | Chamber Italian   |         2006 |            14.99
     384 | Grosse Wonderful  |         2006 |            19.99
       8 | Airport Pollock   |         2006 |            15.99
      98 | Bright Encounters |         2006 |            12.99
       1 | Academy Dinosaur  |         2006 |            20.99

```

answer

```sql
SELECT film_id, title, release_year, replacement_cost, 0.1 * replacement_cost AS DEPOSIT 
FROM film;
```

output
```
 film_id |       title       | release_year | replacement_cost | deposit 
---------+-------------------+--------------+------------------+---------
     133 | Chamber Italian   |         2006 |            14.99 |   1.499
     384 | Grosse Wonderful  |         2006 |            19.99 |   1.999
       8 | Airport Pollock   |         2006 |            15.99 |   1.599
      98 | Bright Encounters |         2006 |            12.99 |   1.299
       1 | Academy Dinosaur  |         2006 |            20.99 |   2.099
```

question id: 828212bd-959b-44cf-818c-dfe1ab347d42


### Calculate how many characters in a string/text

```sql
SELECT LENGTH(col_name) FROM table_name;
```

question id: 8e3fe030-7e82-4e94-a74d-3d9802327792

### Concatenate first_name and last_name of a customer to create a column called full_name

table customer

```
 customer_id | first_name | last_name |                email                |       last_update       
-------------+------------+-----------+-------------------------------------+-------------------------
         524 | Jared      | Ely       | jared.ely@sakilacustomer.org        | 2013-05-26 14:49:45.738
           1 | Mary       | Smith     | mary.smith@sakilacustomer.org       | 2013-05-26 14:49:45.738
           2 | Patricia   | Johnson   | patricia.johnson@sakilacustomer.org | 2013-05-26 14:49:45.738
           3 | Linda      | Williams  | linda.williams@sakilacustomer.org   | 2013-05-26 14:49:45.738
           4 | Barbara    | Jones     | barbara.jones@sakilacustomer.org    | 2013-05-26 14:49:45.738

```

answer 

```sql
SELECT first_name || ' ' || last_name AS full_name FROM customer;
```

output

```
    full_name     
------------------
 Jared Ely
 Mary Smith
 Patricia Johnson
 Linda Williams
 Barbara Jones
```

question id: e47df7fd-1928-4aa3-8d21-521f3493160c

### Figure out that a length of a string/text is greater than N without evaluating the whole length of 
a string/text and why to do so

answer 
Because evaluating length for very long string is costly and time-consuming (we are token about megabytes of text)

```sql
LENGTH(LEFT(col_name, N + 1)) > N
```

question in: a0d686d1-e090-4d41-8394-4dff793eeb22


### Return N characters from the left side of the string

```sql
LEFT(col_name, N)
```

where N is number of characters to return, similar to `'python'[:3]`

question id: 3172556a-86b9-49e1-b87e-57d9434cf316

### How to create email for customers by their first_name and last_name

table customer
```
 customer_id | first_name | last_name |       last_update       
-------------+------------+-----------+-------------------------
         524 | Jared      | Ely       | 2013-05-26 14:49:45.738
           1 | Mary       | Smith     | 2013-05-26 14:49:45.738
           2 | Patricia   | Johnson   | 2013-05-26 14:49:45.738
           3 | Linda      | Williams  | 2013-05-26 14:49:45.738
           4 | Barbara    | Jones     | 2013-05-26 14:49:45.738
```

expected result for Mary Smith is msmith@gmail.com

answer 
```sql
SELECT LOWER(LEFT(first_name, 1) || last_name) || '@gmail.com' AS email
FROM customer LIMIT 5;
```

output
```
 email        
---------------------
 jely@gmail.com
 msmith@gmail.com
 pjohnson@gmail.com
 lwilliams@gmail.com
 bjones@gmail.com
```

question id: bc1ffbb1-9fd3-42ac-b069-c9602a4a426a


### Get movies which rental_rate is more than average and calculate for every of such movies how much 
is its rental_rate is greater than average rental_rate

table film
```
       title       | rental_rate 
-------------------+-------------
 Chamber Italian   |        4.99
 Grosse Wonderful  |        4.99
 Airport Pollock   |        4.99
 Bright Encounters |        4.99
 Academy Dinosaur  |        0.99
```

output
```
       title       | rental_rate | above_average_rate 
-------------------+-------------+--------------------
 Chamber Italian   |        4.99 |               2.01
 Grosse Wonderful  |        4.99 |               2.01
 Airport Pollock   |        4.99 |               2.01
 Bright Encounters |        4.99 |               2.01
 Ace Goldfinger    |        4.99 |               2.01
 Adaptation Holes  |        2.99 |               0.01
 Affair Prejudice  |        2.99 |               0.01
 African Egg       |        2.99 |               0.01
 Agent Truman      |        2.99 |               0.01
 Airplane Sierra   |        4.99 |               2.01
```

answer

We need to use subquery 

```sql
SELECT title, rental_rate, ROUND(rental_rate - (SELECT AVG(rental_rate) FROM film), 2) AS above_average_rate
FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film)
LIMIT 10;
```

question id: 27e0ee35-1ae5-4ede-be8f-b370e0f3b95e

### Select rows where an array is not empty

table users where `additional_phones` is an array
```
+----+-----------------+
|id  |additional_phones|
+----+-----------------+
|344 |                 |
|3700|                 |
|9527|                 |
|918 |                 |
|8988|                 |
|813 |                 |
|380 |                 |
|379 |                 |
|378 |                 |
|377 |                 |
+----+-----------------+
```

answer

Check whether array is empty or not with `array_length()` where the first one is column name and the 
second one is dimension of an array

```sql
SELECT id, additional_phones
FROM users
WHERE array_length(additional_phones, 1) > 0;
```

output
```
+-----+-----------------+
|id   |additional_phones|
+-----+-----------------+
|10117|{+79117325005}   |
|410  |{79994694191}    |
|442  |{+79185112633}   |
|9495 |{79998785661}    |
|595  |{+79263446612}   |
+-----+-----------------+
```

question id: cbf628ba-b26b-4b5b-ad36-702b8cb7371b

### Pattern matching in array

We have a table like this:
```
+-----+---------------------------+
|id   |additional_phones          |
+-----+---------------------------+
|11111|{+79261123541,+79686478689}|
|9473 |{+79117846046,+79661033725}|
|5401 |{+79689550818,+79258716136}|
|8745 |{+79913538989,+79630120607}|
|5925 |{+79876159717,+79656441444}|
+-----+---------------------------+
```

We need to find all the phone numbers that start with 7 instead of +7

answer

We need to use `unnest()` function to unpack values of array. It expands an array to multiple rows. 
The non-array columns get repeated for each row. For example:

```sql
select
  first_name,
  last_name,
  unnest(phone_numbers)
from contacts;
```
output
```
 first_name | last_name |    unnest    
------------+-----------+--------------
 John       | Doe       | 999-876-5432
 John       | Doe       | 999-123-4567
 Bob        | Parr      | 555-INC-RDBL
```

So the flow is too unnest array of additional_phones to a separate table with a subquery
and use WHERE clause and LIKE to find numbers that match our pattern

```sql
SELECT id, additional_phone
FROM (SELECT id, unnest(additional_phones) AS additional_phone FROM users) as iap
WHERE additional_phone LIKE '7%'
ORDER BY id DESC
LIMIT 5;
```

output 

```
+-----+----------------+
|id   |additional_phone|
+-----+----------------+
|13648|79057557746     |
|13639|79037302136     |
|13635|79013648038     |
|13634|79772818241     |
|13631|79850726292     |
+-----+----------------+
```

question id: feb2a116-b63d-46a7-9ae5-d1bd0f1e8275

# Get a list of all film titles (and film ids) that were returned during 2005-05-29

table rental
```
 rental_id |     rental_date     | inventory_id | customer_id |     return_date     | staff_id |     last_update     
-----------+---------------------+--------------+-------------+---------------------+----------+---------------------
         2 | 2005-05-24 22:54:33 |         1525 |         459 | 2005-05-28 19:40:33 |        1 | 2006-02-16 02:30:53
         3 | 2005-05-24 23:03:39 |         1711 |         408 | 2005-06-01 22:12:39 |        1 | 2006-02-16 02:30:53
         4 | 2005-05-24 23:04:41 |         2452 |         333 | 2005-06-03 01:43:41 |        2 | 2006-02-16 02:30:53
         5 | 2005-05-24 23:05:21 |         2079 |         222 | 2005-06-02 04:33:21 |        1 | 2006-02-16 02:30:53
         6 | 2005-05-24 23:08:07 |         2792 |         549 | 2005-05-27 01:32:07 |        1 | 2006-02-16 02:30:53
(5 rows)
```

table inventory
```
 inventory_id | film_id | store_id |     last_update     
--------------+---------+----------+---------------------
            1 |       1 |        1 | 2006-02-15 10:09:17
            2 |       1 |        1 | 2006-02-15 10:09:17
            3 |       1 |        1 | 2006-02-15 10:09:17
            4 |       1 |        1 | 2006-02-15 10:09:17
            5 |       1 |        2 | 2006-02-15 10:09:17
```

table film

```
 film_id |       title       
---------+-------------------
     133 | Chamber Italian
     384 | Grosse Wonderful
       8 | Airport Pollock
      98 | Bright Encounters
       1 | Academy Dinosaur

```

expected output
```
+-------+--------------------+
|film_id|title               |
+-------+--------------------+
|15     |Alien Center        |
|19     |Amadeus Holy        |
|45     |Attraction Newton   |
|50     |Baked Cleopatra     |
|52     |Ballroom Mockingbird|
|54     |Banger Pinocchio    |
|68     |Betrayed Rear       |
|73     |Bingo Talented      |
|83     |Blues Instinct      |
|89     |Borrowers Bedazzled |
+-------+--------------------+
```
There are should be 83 items.

And there are two ways how to accomplish it.


answer

The way with subquery. Count returned films in a subquery. Select titles of films if film_id in subquery.

```sql
SELECT film.film_id, title FROM film
WHERE film_id in (SELECT inventory.film_id FROM rental INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30')
ORDER BY film_id LIMIT 10;
```

The way with two joins.
```sql
SELECT inventory.film_id, title
FROM rental
         INNER JOIN inventory ON rental.inventory_id = inventory.inventory_id
         INNER JOIN film ON inventory.film_id = film.film_id
WHERE return_date => '2005-05-29' < '2005-05-30'
ORDER BY film_id
```

question id: 3cc54e0f-e496-4706-89d7-781e22cebf24


### Find customers who paid more than $11 in one transaction (using EXISTS)

table rental
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577

```

table customer
```
 customer_id | first_name | last_name 
-------------+------------+-----------
         524 | Jared      | Ely
           1 | Mary       | Smith
           2 | Patricia   | Johnson
           3 | Linda      | Williams
           4 | Barbara    | Jones
```


expected output
```
 customer_id | first_name | last_name 
-------------+------------+----------
         362 | Nicholas   | Barfield 
         204 | Rosemary   | Schmidt  
         116 | Victoria   | Gibson   
         195 | Vanessa    | Sims     
         237 | Tanya      | Gilbert  
```



Using exists
```sql
SELECT customer_id, first_name, last_name
FROM customer AS c
WHERE EXISTS(SELECT * FROM payment AS p WHERE c.customer_id = p.customer_id AND p.amount > 11);
```

You can also use INNER JOIN

Using join
```sql
SELECT payment.customer_id, first_name, last_name, amount
FROM payment
         INNER JOIN customer on payment.customer_id = customer.customer_id
WHERE amount > 11;
```

question id: 6543d141-0caf-45da-bcb5-8203131af4d7


### Tell us about `EXISTS` operator

- boolean operator that tests for existence of rows in a subquery.

- accepts an argument which is a subquery.

- if the subquery returns at least one row, the result of EXISTS is true.

- the result of EXISTS operator depends on whether any row returned by the subquery, and not on the row contents. 
Therefore, columns that appear on the SELECT clause of the subquery are not important.

https://www.postgresqltutorial.com/postgresql-exists/

question id: 41579815-02bc-4841-bc07-1ff6b5fbc64d


### What does this query mean?

```sql
SELECT customer_id, first_name, last_name
FROM customer
WHERE EXISTS(SELECT * FROM payment WHERE customer.customer_id = payment.customer_id AND payment.amount > 11);
```

Answer: 
The following statement returns customers who have paid at least one rental with an amount greater than 11

We have two tables, customer and payment, connected via customer_id. 
for each customer in the customer table, the subquery checks the payment table to find if that customer made at least
one payment (p.customer_id = c.customer_id) and the amount is greater than 11 ( amount > 11)

https://www.postgresqltutorial.com/postgresql-exists/

question id: ea3f2890-33ba-4f91-89bd-f936a19af0e2


### Find all pairs of movies with the same length

table film
```
 film_id |       title       | length 
---------+-------------------+--------
     133 | Chamber Italian   |    117
     384 | Grosse Wonderful  |     49
       8 | Airport Pollock   |     54
      98 | Bright Encounters |     73
       1 | Academy Dinosaur  |     86
```

expected output something like
```
 title1      |       title2        
------------------+---------------------
 Academy Dinosaur | Annie Identity
 Academy Dinosaur | Gandhi Kwai
 Academy Dinosaur | Midnight Westward
 Academy Dinosaur | Yentl Idaho
 Ace Goldfinger   | Heaven Freedom
 Ace Goldfinger   | Rush Goodfellas
 Ace Goldfinger   | Midsummer Groundhog
```

answer

Use self-join

```

SELECT f1.title, f2.title, f1.length
FROM film AS f1
         JOIN film AS f2 ON f1.film_id != f2.film_id AND f1.length = f2.length
ORDER BY f1.title
LIMIT 20;
```

question id: 08510dce-934c-4353-83d9-18c9291eeea5

### Restore database to postgres in docker

```bash
docker exec -i container_name pg_restore --verbose --clean --no-acl --no-owner -h localhost -U user_name -d database_name < /home/aleksandr/Downloads/file_with_database.tar
```

### How can you produce a list of facilities that charge a fee to members, and that fee is less than 1/50th of the monthly maintenance cost? Return the facid, facility name, member cost, and monthly maintenance of the facilities in question.

table cd.facilities

```
 facid |      name       | membercost | guestcost | initialoutlay | monthlymaintenance 
-------+-----------------+------------+-----------+---------------+--------------------
     0 | Tennis Court 1  |          5 |        25 |         10000 |                200
     1 | Tennis Court 2  |          5 |        25 |          8000 |                200
     2 | Badminton Court |          0 |      15.5 |          4000 |                 50
     3 | Table Tennis    |          0 |         5 |           320 |                 10
     4 | Massage Room 1  |         35 |        80 |          4000 |               3000
     5 | Massage Room 2  |         35 |        80 |          4000 |               3000
     6 | Squash Court    |        3.5 |      17.5 |          5000 |                 80
     7 | Snooker Table   |          0 |         5 |           450 |                 15
     8 | Pool Table      |          0 |         5 |           400 |                 15
```

answer

```sql
SELECT name, membercost, monthlymaintenance
FROM cd.facilities
WHERE membercost > 0 AND membercost < monthlymaintenance / 50;
```

output 

```
+---------------+----------+------------------+
|name           |membercost|monthlymaintenance|
+---------------+----------+------------------+
|Massage Room 1 |35        |3000              |
|Massage Room 2 |35        |3000              |
+---------------+----------+------------------+
```

question id: 9a6c3126-d8a2-496c-95da-759b66c2dbc0

### How can you produce a list of all facilities with the word 'Tennis' in their name?

table cd.facilities, column name

```sql
SELECT * FROM cd.facilities WHERE name LIKE '%Tennis%';
```

question id: 29a04bcf-6938-4d65-90b7-9348f0d0e271

### How can you retrieve the details of facilities with ID 1 and 5? Try to do it without using the OR operator.

table cd.facilities, column 

```sql
SELECT * FROM cd.facilities WHERE facid IN (1, 5);
```

question id: e0f07cb2-447f-4194-b1a8-1dde0f6fa2c0

### How can you produce a list of members who joined after the start of September 2012? 

table cd.members

```
+-----+--------+---------+--------------------------+
|memid|surname |firstname|joindate                  |
+-----+--------+---------+--------------------------+
|0    |GUEST   |GUEST    |2012-07-01 00:00:00.000000|
|1    |Smith   |Darren   |2012-07-02 12:02:05.000000|
|2    |Smith   |Tracy    |2012-07-02 12:08:23.000000|
|3    |Rownam  |Tim      |2012-07-03 09:32:15.000000|
|4    |Joplette|Janice   |2012-07-03 10:25:05.000000|
+-----+--------+---------+--------------------------+
```

answer
```sql
SELECT memid, surname, firstname, joindate
FROM cd.members
WHERE joindate >= '2012-09-01'
LIMIT 11;
```

output
```
+-----+-----------------+---------+--------------------------+
|memid|surname          |firstname|joindate                  |
+-----+-----------------+---------+--------------------------+
|24   |Sarwin           |Ramnaresh|2012-09-01 08:44:42.000000|
|26   |Jones            |Douglas  |2012-09-02 18:43:05.000000|
|27   |Rumney           |Henrietta|2012-09-05 08:42:35.000000|
|28   |Farrell          |David    |2012-09-15 08:22:05.000000|
|29   |Worthington-Smyth|Henry    |2012-09-17 12:27:15.000000|
+-----+-----------------+---------+--------------------------+

```

question id: 1d961b42-23a7-4c18-b6d5-0e3b5ab726cc

### How can you produce an ordered list of the first 10 surnames in the members table? 

The list must not contain duplicates.

table cd.members

```
+-----+--------+---------+--------------------------+
|memid|surname |firstname|joindate                  |
+-----+--------+---------+--------------------------+
|0    |GUEST   |GUEST    |2012-07-01 00:00:00.000000|
|1    |Smith   |Darren   |2012-07-02 12:02:05.000000|
|2    |Smith   |Tracy    |2012-07-02 12:08:23.000000|
|3    |Rownam  |Tim      |2012-07-03 09:32:15.000000|
|4    |Joplette|Janice   |2012-07-03 10:25:05.000000|
+-----+--------+---------+--------------------------+
```

answer

```sql
SELECT DISTINCT(surname) FROM cd.members 
ORDER BY surname LIMIT 10;
```

output:

```
+-------+
|surname|
+-------+
|Bader  |
|Baker  |
|Boothe |
|Butters|
|Coplin |
|Crumpet|
|Dare   |
|Farrell|
|Genting|
|GUEST  |
+-------+
```

question id: 5977bfcf-a317-47b1-b398-5f2a8d9f96e4


### You'd like to get the signup date of your last member. How can you retrieve this information?

table cd.members

```
+-----+--------+---------+--------------------------+
|memid|surname |firstname|joindate                  |
+-----+--------+---------+--------------------------+
|0    |GUEST   |GUEST    |2012-07-01 00:00:00.000000|
|1    |Smith   |Darren   |2012-07-02 12:02:05.000000|
|2    |Smith   |Tracy    |2012-07-02 12:08:23.000000|
|3    |Rownam  |Tim      |2012-07-03 09:32:15.000000|
|4    |Joplette|Janice   |2012-07-03 10:25:05.000000|
+-----+--------+---------+--------------------------+
```

answer

```sql
SELECT MAX(joindate) FROM cd.members;
```

question id: 9f3fdede-3c71-4d85-8e1e-0335cccc9d6b

### Produce a list of the total number of slots booked per facility in the month of September 2012. 

Produce an output table consisting of facility id and slots, sorted by the number of slots.
Expected Result is 9 rows.

table cd.bookings

```
+------+-----+-----+--------------------------+-----+
|bookid|facid|memid|starttime                 |slots|
+------+-----+-----+--------------------------+-----+
|0     |3    |1    |2012-07-03 11:00:00.000000|2    |
|1     |4    |1    |2012-07-03 08:00:00.000000|2    |
|2     |6    |0    |2012-07-03 18:00:00.000000|2    |
|3     |7    |1    |2012-07-03 19:00:00.000000|2    |
|4     |8    |1    |2012-07-03 10:00:00.000000|1    |
+------+-----+-----+--------------------------+-----+
```

answer

We need to `GROUP BY` facid which is facility id and `SUM()` by bookings

```sql
SELECT facid, SUM(slots) AS total_slots
FROM cd.bookings
WHERE starttime >= '2012-09-01'
  AND starttime <= '2012-10-01'
GROUP BY facid
ORDER BY SUM(slots) DESC;
```
 
output
```
+-----+-----------+
|facid|total_slots|
+-----+-----------+
|4    |648        |
|0    |591        |
|1    |588        |
|2    |570        |
|6    |540        |
|8    |471        |
|7    |426        |
|3    |422        |
|5    |122        |
+-----+-----------+
```

question id: d44df7a4-0615-4a1b-85a4-130618ed1fc6

### Produce a list of facilities with more than 1000 slots booked. 

Produce an output table consisting of facility id and total slots, sorted by facility id.

table cd.bookings

```
+------+-----+-----+--------------------------+-----+
|bookid|facid|memid|starttime                 |slots|
+------+-----+-----+--------------------------+-----+
|0     |3    |1    |2012-07-03 11:00:00.000000|2    |
|1     |4    |1    |2012-07-03 08:00:00.000000|2    |
|2     |6    |0    |2012-07-03 18:00:00.000000|2    |
|3     |7    |1    |2012-07-03 19:00:00.000000|2    |
|4     |8    |1    |2012-07-03 10:00:00.000000|1    |
+------+-----+-----+--------------------------+-----+
```

answer

We need to `GROUP BY` facid which is facility id and `SUM()` by bookings. To apply a clause to sum of slots we 
need to use HAVING (as always with aggregation functions). 

```sql
SELECT facid, SUM(slots) AS total_slots FROM cd.bookings
GROUP BY facid
HAVING SUM(slots) >= 1000
ORDER BY facid;
```

output
```
+-----+-----------+
|facid|total_slots|
+-----+-----------+
|0    |1320       |
|1    |1278       |
|2    |1209       |
|4    |1404       |
|6    |1104       |
+-----+-----------+
```

question id: b560107d-d929-4bc9-bb5b-9db74fe6c8e9


### How can you produce a list of the start times for bookings for tennis courts, for the date '2012-09-21'? Return a list of start time and facility name pairings, ordered by the time.

Expected Result is 12 rows

table cd.bookings
```
 bookid | facid | memid |      starttime      | slots 
--------+-------+-------+---------------------+-------
      0 |     3 |     1 | 2012-07-03 11:00:00 |     2
      1 |     4 |     1 | 2012-07-03 08:00:00 |     2
      2 |     6 |     0 | 2012-07-03 18:00:00 |     2
      3 |     7 |     1 | 2012-07-03 19:00:00 |     2
      4 |     8 |     1 | 2012-07-03 10:00:00 |     1
```

table cd.facilities

```
 facid |      name       | membercost | guestcost | initialoutlay | monthlymaintenance 
-------+-----------------+------------+-----------+---------------+--------------------
     0 | Tennis Court 1  |          5 |        25 |         10000 |                200
     1 | Tennis Court 2  |          5 |        25 |          8000 |                200
     2 | Badminton Court |          0 |      15.5 |          4000 |                 50
     3 | Table Tennis    |          0 |         5 |           320 |                 10
     4 | Massage Room 1  |         35 |        80 |          4000 |               3000
```

expected result 

```
+--------------------------+--------------+
|start                     |name          |
+--------------------------+--------------+
|2012-09-21 08:00:00.000000|Tennis Court 1|
|2012-09-21 08:00:00.000000|Tennis Court 2|
|2012-09-21 09:30:00.000000|Tennis Court 1|
|2012-09-21 10:00:00.000000|Tennis Court 2|
|2012-09-21 11:30:00.000000|Tennis Court 2|
|2012-09-21 12:00:00.000000|Tennis Court 1|
|2012-09-21 13:30:00.000000|Tennis Court 1|
|2012-09-21 14:00:00.000000|Tennis Court 2|
|2012-09-21 15:30:00.000000|Tennis Court 1|
|2012-09-21 16:00:00.000000|Tennis Court 2|
+--------------------------+--------------+
```

answer

We just need an `INNER JOIN` and some `WHERE` conditions

```sql
SELECT starttime as start, name
FROM cd.bookings b
         INNER JOIN cd.facilities f ON b.facid = f.facid
WHERE starttime >= '2012-09-21'
  AND starttime < '2012-09-22'
  AND name LIKE '%Tennis Court%'
ORDER BY starttime;
```

question id: 3b99145b-5fef-4dea-8062-a922d39f3178


### How can you produce a list of the start times for bookings by members named 'David Farrell'?

Expected result is 34 rows of timestamps

table cd.bookings

```
 bookid | facid | memid |      starttime      | slots 
--------+-------+-------+---------------------+-------
      0 |     3 |     1 | 2012-07-03 11:00:00 |     2
      1 |     4 |     1 | 2012-07-03 08:00:00 |     2
      2 |     6 |     0 | 2012-07-03 18:00:00 |     2
      3 |     7 |     1 | 2012-07-03 19:00:00 |     2
      4 |     8 |     1 | 2012-07-03 10:00:00 |     1
```

table cd.members

```
 memid | surname  | firstname |           address            
-------+----------+-----------+------------------------------
     0 | GUEST    | GUEST     | GUEST
     1 | Smith    | Darren    | 8 Bloomsbury Close, Boston
     2 | Smith    | Tracy     | 8 Bloomsbury Close, New York
     3 | Rownam   | Tim       | 23 Highway Way, Boston
     4 | Joplette | Janice    | 20 Crossing Road, New York
```

Expected 34 rows

answer

Just use `INNER JOIN`

```sql
SELECT starttime, firstname, surname
FROM cd.bookings b
         INNER JOIN cd.members m ON b.memid = m.memid
WHERE surname = 'Farrell'
  AND firstname = 'David';
```

question id: 4d428190-715d-4cba-9d0c-76cfed3e141d


### How to update one value in some table?

```sql
UPDATE users
SET first_name = 'Mark'
WHERE id = 21
```

question id: 4de0c6b6-4f67-4d5f-aae2-b6e7452f0ab4


### How to update several columns at once in some table?

```sql
UPDATE users
SET first_name = 'Mark', last_name='Markovich'
WHERE id = 21
```

question id: 065795a7-3226-48fb-8906-16f19e48cc9d


### Change district in a customer address for customer Mary Smith

table customer

```
+-----------+----------+---------+----------+-----------------------------------+
|customer_id|first_name|last_name|address_id|email                              |
+-----------+----------+---------+----------+-----------------------------------+
|524        |Jared     |Ely      |530       |jared.ely@sakilacustomer.org       |
|1          |Mary      |Smith    |5         |mary.smith@sakilacustomer.org      |
|2          |Patricia  |Johnson  |6         |patricia.johnson@sakilacustomer.org|
|3          |Linda     |Williams |7         |linda.williams@sakilacustomer.org  |
|4          |Barbara   |Jones    |8         |barbara.jones@sakilacustomer.org   |
+-----------+----------+---------+-------
```

table address 

```
+----------+--------------------+----------+-----------+------------+
|address_id|address             |district  |postal_code|phone       |
+----------+--------------------+----------+-----------+------------+
|1         |47 MySakila Drive   |Alberta   |           |            |
|2         |28 MySQL Boulevard  |QLD       |           |            |
|3         |23 Workhaven Lane   |Alberta   |           |14033335568 |
|4         |1411 Lillydale Drive|QLD       |           |6172235589  |
|6         |1121 Loja Avenue    |California|17886      |838635286649|
+----------+--------------------+----------+-----------+------------+
```

answer

You need to join table, but you cannot do this in postgres via usual join syntax. You
need to join your table via 'WHERE' clause and then add your conditions

```sql
UPDATE address -- table that you want to update eventually 
SET district = 'Moscow'
FROM customer  -- column to use in WHERE clause
WHERE customer.address_id = address.address_id  -- join a table
  AND customer.first_name = 'Mary'  -- add your conditions
  AND customer.last_name = 'Smith';
```

or just for example in pik.pro

```sql
UPDATE user_profiles up
SET avatar_hashid = NULL
FROM users u
WHERE u.id = up.user_id AND u.id = 14320 ;  -- note that user_profiles use separate columns for ids from user table
```

question id: 33c4ab10-91af-4ad9-b4f9-a72d3d91f00f


### How to set current date as a default value for an existing field with type DATE?

```sql
ALTER TABLE table_name
ALTER COLUMN col_name SET DEFAULT CURRENT_DATE;
```

question id: e6e340b4-2a1e-4a84-85e8-a048684eed17

### Create a simple table

Create a table named account with the following columns: username, password, email, created_at, last_login

```sql
CREATE TABLE account(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);
```

question id: 286cf52c-f529-4b8b-9f9b-ff36a05cbaa3

### Create an m2m relation between two following tables with column hire_date

table account

```sql
CREATE TABLE account(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);
````

table job

```sql
CREATE TABLE job(
    id SERIAL PRIMARY KEY,
    job_name VARCHAR(200) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL
)
```

answer
```sql
CREATE TABLE account_job(
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES account(id) ON DELETE CASCADE,
    job_id INTEGER REFERENCES job(id) ON DELETE CASCADE,
    hire_date TIMESTAMP NOT NULL,
    CONSTRAINT account_job_unique UNIQUE(user_id,job_id)
);
```

question id: d0d0678a-7a6c-4a5b-9db4-277bc4ad3123

### How to insert values from another table on some condition?

```sql
INSERT INTO table_name(column1, column2)
SELECT column1, column2
FROM another_table
WHERE some_condition; 
```

question id: cdb6bd0e-ae28-4553-80cf-8c89bbc52246


### Add values to the table

table account

```sql
CREATE TABLE account(
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(250) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);
````

values: name - Jose, password - passoword, email - jose@mail.com

answer

```sql
INSERT INTO account(username, password, email, created_at)
VALUES('Jose', 'passoword', 'jose@mail.com', CURRENT_TIMESTAMP)
```

question id: 4ff568cf-687f-4ea2-bc6f-a709fb15ec30

### Add values to table

table job

```sql
CREATE TABLE job(
    id SERIAL PRIMARY KEY,
    job_name VARCHAR(200) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
);
```

values - 'Astronaut'

answer

```sql
INSERT INTO job(job_name, created_at)
VALUES ('Astronaut', CURRENT_TIMESTAMP);
```

question id: 8c237a2f-565b-4883-a260-75b867fa69aa

### How to return some columns of the updated rows?

General syntax: 

```sql
UPDATE table_name
SET column_name = 'your_value'
WHERE your_condition
RETURNING column_name, column_name2, column_name3
```

question id: 4c55c9fa-e953-4a73-a4df-959eb1c1440a


### For customers with ids 23, 34, 45 set last login timestamp to current one

table customer

```
 customer_id | first_name | last_name |       last_update       
-------------+------------+-----------+-------------------------
         524 | Jared      | Ely       | 2013-05-26 14:49:45.738
           1 | Mary       | Smith     | 2013-05-26 14:49:45.738
           2 | Patricia   | Johnson   | 2013-05-26 14:49:45.738
           3 | Linda      | Williams  | 2013-05-26 14:49:45.738
           4 | Barbara    | Jones     | 2013-05-26 14:49:45.738
```

answer

```sql
UPDATE customer
SET last_update = CURRENT_TIMESTAMP
WHERE customer_id IN (23, 34, 45)
RETURNING customer_id, first_name, last_name, last_update
```

question id: 31643964-c006-4aef-9256-1d5273b4d647

### You have three tables

table account

```bash
+--+--------+---------+-------------+--------------------------+----------+
|id|username|password |email        |created_at                |last_login|
+--+--------+---------+-------------+--------------------------+----------+
|1 |Jose    |passoword|jose@mail.com|2021-02-05 15:34:00.258575|NULL      |
+--+--------+---------+-------------+--------------------------+----------+
```

table job

```bash
+--+---------+--------------------------+
|id|job_name |created_at                |
+--+---------+--------------------------+
|1 |Astronaut|2021-02-05 15:51:11.537055|
|2 |President|2021-02-05 15:54:35.475186|
+--+---------+--------------------------+
```


table account_job

```bash
+-------+------+--------------------------+
|user_id|job_id|hire_date                 |
+-------+------+--------------------------+
|1      |1     |2021-02-05 16:03:00.539500|
+-------+------+--------------------------+
```

You need to set column `job.hire_date` to be equal to `account.created_at` 

answer

You need UPDATE Join

```sql
UPDATE account_job
SET hire_date = account.created_at
FROM account
WHERE account.id = account_job.user_id
RETURNING user_id, job_id, hire_date
```

question id: a63a6ee6-57fa-4c2d-8f6b-9ed1ab20f9c2

### How to remove a row from a table?

General syntax

```sql
DELETE FROM table_name
WHERE row_id = 1
```

question id: 882cceee-0dfd-41e7-8828-915b735bbf6a


### Remove rows from tableA where `name` field in tableB starts with 'S'

```sql
DELETE FROM tableA
USING tableB
WHERE tableB.id = tableA.id AND tableB.name LIKE 'S%'
```

https://www.postgresqltutorial.com/postgresql-delete-join/
https://stackoverflow.com/questions/11753904/postgresql-delete-with-inner-join

question id: c5abb295-2097-4a4a-a2b6-d157e3225b68


### Remove all the rows from the table

```sql
DELETE FROM table;
```

question id: b4925b44-b79d-48ab-97e6-60d6531b476e

### Return some columns from rows that were deleted

```sql
DELETE FROM table
WHERE column_name = 'whatever'
RETURNING column_name
```

question id: a8d9a6de-f75b-412b-8fe6-c80aa130233d

### Add a column to a table

```sql
ALTER TABLE table_name
ADD COLUMN column_name column_type constraint;
```

question id: 2aa92ac7-67c6-426a-97b3-324ff70c443c

### Remove a column from a table

```sql
ALTER TABLE table_name
DROP COLUMN column_name;
```

question id: 2ca85e7a-f090-4f49-a4f0-d221a87dded1

### Set default value for a column

```sql
ALTER TABLE table_name
ALTER COLUMN column_name 
SET DEFAULT value
```

question id: f1cd1890-a612-406d-a654-f34ea38ba57d


### Remove default value for a column

```sql
ALTER TABLE table_name
ALTER COLUMN column_name 
DROP DEFAULT;
```

question id: 93d90fcf-3b0e-4ec9-bbff-6e8573e9e283

### Set a column in an existing table to be not null

```sql
ALTER TABLE table_name
ALTER COLUMN column_name
SET NOT NULL;
```

question id: 53d62cb5-3f2f-4188-b80b-03aeb62c1793

### How to rename a table?

```sql
ALTER TABLE table_name
RENAME TO new_table_name;
```

question id: c0f2b2ac-302b-4963-af92-caf9640c95c4

### How to rename a column?

```sql
ALTER TABLE table_name
RENAME COLUMN col_name TO another_col_name;
```

question id: 5c5299e5-1de9-498f-b637-0ea400ee1da8


### Set a constraint (e.g. NOT NULL) to an existing column

```sql
ALTER TABLE table_name
ALTER COLUMN column_name SET NOT NULL;
```

question id: 68843f62-546f-4102-8428-50a53e91212d

### Delete a constraint (e.g. NOT NULL) from an existing column

```sql
ALTER TABLE table_name
ALTER COLUMN column_name DROP NOT NULL;
```

question id: 1601c700-6083-423a-af7c-69b2008c2263

### Remove several columns from a table

```sql
ALTER TABLE table_name
DROP COLUMN col_name1,
DROP COLUMN col_name2;
```

question id: 9929e661-4fe8-4068-84ec-3b81a3642555

### Remove a column from only if there is one

```sql
ALTER TABLE table_name
DROP COLUMN IF EXISTS col_name;
```

question id: 3620db47-a0c3-49ab-bf14-7e4663532c3d


### Make a new table called 'employees'

It should have id, first and last name, birthdate column where value should be at least within 20th century, hire_date 
that should be at least bigger than birthdate, and salary which have to be more than zero

answer 

```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE CHECK(birthdate > '1900-01-01'),
    hire_date DATE CHECK(hire_date > birthdate),
    salary INTEGER CHECK (salary > 0)
);
```

question id: 9dbffe04-b987-4940-87bb-4e6eb1ac7cdb

### What's CHECK for?

For creating custom constraints like

```sql
CREATE TABLE employees(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE CHECK(birthdate > '1900-01-01')
    hire_date DATE CHECK(hire_date > birthdate)
    salary INTEGER (salary > 0)
);
```

question id: 117880df-e157-49db-984e-596604851af2

### How to add a CHECK constraint to an existing column?

```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name CHECK(some codintion on whatever field you like)
```

question id: 354b9aa5-4df7-40e9-9b7b-fa064de098f0


### Set new class system for customers

You have a customer table

```
+-----------+----------+--------------------------+
|customer_id|first_name|last_update               |
+-----------+----------+--------------------------+
|1          |Mary      |2013-05-26 14:49:45.738000|
|2          |Patricia  |2013-05-26 14:49:45.738000|
|3          |Linda     |2013-05-26 14:49:45.738000|
|4          |Barbara   |2013-05-26 14:49:45.738000|
|5          |Elizabeth |2013-05-26 14:49:45.738000|
+-----------+----------+--------------------------+
```

You need to create a new column and fill it with a class of a customer.
(You don't change the table, new column only appears in your select outcome)
First 100 customers should get 'Premium' class.
Customers with id from 101 to 200 should be 'Plus'.
The rest should get a 'Normal' customer_class;

Like this

```
+-----------+----------+---------+--------------+
|customer_id|first_name|last_name|customer_class|
+-----------+----------+---------+--------------+
|1          |Mary      |Smith    |Premium       |
|2          |Patricia  |Johnson  |Premium       |
|3          |Linda     |Williams |Premium       |
+-----------+----------+---------+--------------+
```

Answer:

You need to use CASE statement

```sql
SELECT customer_id, first_name, last_name,
CASE
    WHEN (customer_id <= 100) THEN 'Premium'
    WHEN (customer_id BETWEEN 101 AND 200) THEN 'Plus'
ELSE 'Normal'
END AS customer_class
FROM customer
ORDER BY customer_id;
```

question id: 4d74178d-4b7e-4167-b6f0-e25aaf6e2c35


### A raffle

You have a customer table

```
+-----------+----------+--------------------------+
|customer_id|first_name|last_update               |
+-----------+----------+--------------------------+
|1          |Mary      |2013-05-26 14:49:45.738000|
|2          |Patricia  |2013-05-26 14:49:45.738000|
|3          |Linda     |2013-05-26 14:49:45.738000|
|4          |Barbara   |2013-05-26 14:49:45.738000|
|5          |Elizabeth |2013-05-26 14:49:45.738000|
+-----------+----------+--------------------------+
```

You gonna make a hardcoded raffle. You need a new column 'raffle_result'
where the second customer is Winner, the fifth is Second place, and the rest of them 
is Normal

Expected result:

```
+-----------+----------+---------+--------------+
|customer_id|first_name|last_name|raffle_results|
+-----------+----------+---------+--------------+
|1          |Mary      |Smith    |Normal        |
|2          |Patricia  |Johnson  |Winner        |
|3          |Linda     |Williams |Normal        |
|4          |Barbara   |Jones    |Normal        |
|5          |Elizabeth |Brown    |Second place  |
+-----------+----------+---------+--------------+
```

answer

```sql
SELECT customer_id,
       first_name,
       last_name,
       CASE customer_id
           WHEN 2 THEN 'Winner'
           WHEN 5 THEN 'Second place'
           ELSE 'Normal'
           END AS raffle_results
FROM customer
ORDER BY customer_id;
```

question id: f9b695ab-aee5-4358-84f2-88fecba33db4

### What's COALESCE? 

The COALESCE function accepts an unlimited number of arguments.
It return the first argument that is not null. If all arguments
are null, the COALESCE funtion will return null

Basically like in Python `x or y or ... or None`

For example
```sql
SELECT
	COALESCE (NULL, 2 , 1)
```

will return 2

question id: 27a39f3c-4892-49b2-a070-e767b2aeaa6f


### What is COALESCE for?

The COALESCE function becomes useful when querying a table that 
contains null values and substituting it with another value.

question id: 4c4a72a8-1ec1-401c-bc4b-23f20d2f3b9d


### Discount

You have a table like this

```
| Item | Price | Discount |
|------|-------|----------|
| A    | 100   | 20       |
| B    | 300   | null     |
| C    | 200   | 10       |
```

You need to come up with a column of final prices, what would you do?

```sql
SELECT item, price, discount, (price - COALESCE(discount, 0)) AS final FROM table_name;
```

question id: e08f050d-99ba-4b85-815a-7437fde4e191


### Convert data types

You have a table `customer` like this: 

```
+-----------+----------+---------+--------------------------+
|customer_id|first_name|last_name|last_update               |
+-----------+----------+---------+--------------------------+
|524        |Jared     |Ely      |2013-05-26 14:49:45.738000|
|1          |Mary      |Smith    |2013-05-26 14:49:45.738000|
|2          |Patricia  |Johnson  |2013-05-26 14:49:45.738000|
|3          |Linda     |Williams |2013-05-26 14:49:45.738000|
|4          |Barbara   |Jones    |2013-05-26 14:49:45.738000|
+-----------+----------+---------+--------------------------+
```

You need to convert last update column to be without information of hours, minutes etc

Expected output

```
+-----------+----------+---------+-----------+
|customer_id|first_name|last_name|last_update|
+-----------+----------+---------+-----------+
|524        |Jared     |Ely      |2013-05-26 |
|1          |Mary      |Smith    |2013-05-26 |
|2          |Patricia  |Johnson  |2013-05-26 |
|3          |Linda     |Williams |2013-05-26 |
|4          |Barbara   |Jones    |2013-05-26 |
+-----------+----------+---------+-----------+
```

answer

You need to use CAST operator

```sql
SELECT customer_id, first_name, last_name, last_update::DATE FROM customer LIMIT 5;
```

question id: 2f8056f8-9d0e-4512-b91e-a17c73771cc7


### How does NULLIF work? Where can it be used? 

The NULLIF function returns a null value if arg1 equals to arg2, otherwise it returns arg1.

It can be used, for example, to prevent division by zero. 

More about it: https://www.postgresqltutorial.com/postgresql-nullif/

question id: dfc59ccd-4c20-4aca-b833-f269d186357b

 
### What's a view?

A view is named query that is defined based on one or more tables which are known as base tables. When you create a 
view, you basically create a query and assign it a name, therefore a view is useful for wrapping a commonly used 
complex query. 

https://www.postgresqltutorial.com/postgresql-views/

View does not store data physically, it stores only your query.

question id: 62cc9bd5-692f-4d4d-9926-d46c91b02360

### What's a materialized view? 

A materialized view caches the result of a complex expensive query and then allow you to refresh this result periodically.

The materialized views are useful in many cases that require fast data access therefore they are often used in data
warehouses or business intelligent applications.

https://www.postgresqltutorial.com/postgresql-materialized-views/

question id: 774ef474-a410-4de7-a050-8f490dd3fdf8


### What happens when you DELETE some rows from a table in PostgreSQL?

They don't get deleted. These rows are marked to be available to reuse. Every row
in PostgreSQL has column xmin for transaction id when it was inserted and xmax for
transaction id during which the rows was kinda deleted. So deleted rows are still
in the database. You cannot see them in transactions which id is bigger than id of 
transaction in their xmax. That's how MVCC works (multiversion concurrency control).
The only way to get rid of these rows totally is to wait for AUTOVACUUM or run VACUUM manually.
But first you have to close all transactions with id less then id from xmax of the deleted rows.

In other words. Everything in PostgreSQL is happening in one or another transaction. Each row
get marked with a transaction id during which it was inserted, and with transaction id within
which the row was deleted. 

For example you want to select some rows. Transaction id for your session is 5. You cannot see
rows that was inserted with transaction 6 (xmin 6). You cannot see rows that have xmax less than
5 either.  

https://lerner.co.il/2015/09/17/in-postgresql-as-in-life-dont-wait-too-long-to-commit/

question id: f94ddba4-cf05-4d41-b34e-d73da12ea2be


### What happens with rows when you updated them? 

They are not getting changed at all. Instead, PostgreSQL inserts new rows and marks old ones
as available to be reused. That's why if we update all the rows, the size of our table doubles.

Every row in PostgreSQL has column xmin for transaction id during which it was inserted and xmax for
transaction id during which the rows was kinda deleted. So deleted rows are still
in the database. You cannot see them in transactions which id is bigger than id of 
transaction in their xmax. That's how MVCC works (multiversion concurrency control).
The only way to get rid of these rows totally is to wait for AUTOVACUUM or run VACUUM manually.
But first you have to close all transactions with id less then id from xmax of the deleted rows.

In other words. Everything in PostgreSQL is happening in one or another transaction. Each row
get marked with a transaction id during which it was inserted, and with transaction id within
which the row was deleted. 

For example you want to select some rows. Transaction id for your session is 5. You cannot see
rows that was inserted with transaction 6 (xmin 6). You cannot see rows that have xmax less than
5 either.  

https://lerner.co.il/2015/09/17/in-postgresql-as-in-life-dont-wait-too-long-to-commit/

question id: 2a78fcc3-237a-4bad-857f-92bcb825bcf1


### Why a table in a db will double its size if you update all the rows in it?

When you update rows in PostgreSQL (or in any other db with with MVCC), you don't actually change any 
existing rows. Instead, PostgreSQL inserts new rows and marks old ones
as available to be reused. That's why if we update all the rows, the size of our table doubles.

Every row in PostgreSQL has column xmin for transaction id during which it was inserted and xmax for
transaction id during which the rows was kinda deleted. So deleted rows are still
in the database. You cannot see them in transactions which id is bigger than id of 
transaction in their xmax. That's how MVCC works (multiversion concurrency control).
The only way to get rid of these rows totally is to wait for AUTOVACUUM or run VACUUM manually.
But first you have to close all transactions with id less then id from xmax of the deleted rows.

In other words. Everything in PostgreSQL is happening in one or another transaction. Each row
get marked with a transaction id during which it was inserted, and with transaction id within
which the row was deleted. 

For example you want to select some rows. Transaction id for your session is 5. You cannot see
rows that was inserted with transaction 6 (xmin 6). You cannot see rows that have xmax less than
5 either.  

https://lerner.co.il/2015/09/17/in-postgresql-as-in-life-dont-wait-too-long-to-commit/

question id: fd2fe6c6-6cc1-4cad-9777-11c780de9ade


### What will happen with the size of a table if you update all the rows in it?

It will double. 

When you update rows in PostgreSQL (or in any other db with with MVCC), you don't actually change any 
existing rows. Instead, PostgreSQL inserts new rows and marks old ones
as available to be reused. That's why if we update all the rows, the size of our table doubles.

Every row in PostgreSQL has column xmin for transaction id during which it was inserted and xmax for
transaction id during which the rows was kinda deleted. So deleted rows are still
in the database. You cannot see them in transactions which id is bigger than id of 
transaction in their xmax. That's how MVCC works (multiversion concurrency control).
The only way to get rid of these rows totally is to wait for AUTOVACUUM or run VACUUM manually.
But first you have to close all transactions with id less then id from xmax of the deleted rows.

In other words. Everything in PostgreSQL is happening in one or another transaction. Each row
get marked with a transaction id during which it was inserted, and with transaction id within
which the row was deleted. 

For example you want to select some rows. Transaction id for your session is 5. You cannot see
rows that was inserted with transaction 6 (xmin 6). You cannot see rows that have xmax less than
5 either.  

https://lerner.co.il/2015/09/17/in-postgresql-as-in-life-dont-wait-too-long-to-commit/

question id: c5546c05-cb4b-4a3c-8d85-fcc3ad488764


### What customer has the highest customer ID number whose name starts with an 'E' and has an address ID lower than 500?
Table: customer;

```
 customer_id | first_name | last_name | address_id 
-------------+------------+-----------+------------
         524 | Jared      | Ely       |        530
           1 | Mary       | Smith     |          5
           2 | Patricia   | Johnson   |          6
           3 | Linda      | Williams  |          7
           4 | Barbara    | Jones     |          8
```

asnwer

```sql
SELECT first_name, last_name FROM customer
WHERE first_name LIKE 'E%' AND address_id < 500
ORDER BY customer_id DESC LIMIT 1;
```

output 

```
 first_name | last_name 
------------+-----------
 Eddie      | Tomlin
```

question id: 57098b92-1138-47ba-a9c8-365564196429


### How to add UNIQUE constraint to an existing column(s)?

```sql
ALTER TABLE table_name
ADD UNIQUE(col1, col2)
```

https://stackoverflow.com/questions/1194438/can-i-add-a-unique-constraint-to-a-postgresql-table-after-its-already-created

question id: 9e69ca7e-3b49-45f4-8ef6-23d85d97e6ad


### How to add UNIQUE constraint for an existing m2m table that there could be only one unique pair of foreign keys?

```sql
ALTER TABLE table_name
ADD CONSTRAINT constrait_name UNIQUE(a_id, b_id)
```

question id: ba9447e2-aadc-45af-a0a7-a4693621dfbd


### How to group by timestamp but buy month? 

For example, you want to get sum of all payments of every month from table `payment`. How would you do so?

table payment
```
 payment_id | customer_id | staff_id | rental_id | amount |        payment_date        
------------+-------------+----------+-----------+--------+----------------------------
      17503 |         341 |        2 |      1520 |   7.99 | 2007-02-15 22:25:46.996577
      17504 |         341 |        1 |      1778 |   1.99 | 2007-02-16 17:23:14.996577
      17505 |         341 |        1 |      1849 |   7.99 | 2007-02-16 22:41:45.996577
      17506 |         341 |        2 |      2829 |   2.99 | 2007-02-19 19:39:56.996577
      17507 |         341 |        2 |      3130 |   7.99 | 2007-02-20 17:31:48.996577
```

expected output
```
+--------------------------+--------+
|date_trunc                |sum     |
+--------------------------+--------+
|2007-03-01 00:00:00.000000|23886.56|
|2007-04-01 00:00:00.000000|28559.46|
|2007-05-01 00:00:00.000000|514.18  |
|2007-02-01 00:00:00.000000|8351.84 |
+--------------------------+--------+
```

answer

Use DATE_TRUNC
```sql
SELECT DATE_TRUNC('month', payment_date) as payment_month, SUM(amount) FROM payment
GROUP BY payment_month
```

question id: ac885b93-ddcb-4c2f-9f1b-0fb42260c117


### What is an order of arguments for date_trunc()? 

answer
```sql
date_trunc(precision, source)
```
For example:
```sql
SELECT date_trunc('year', TIMESTAMP '2001-02-16 20:38:40');
-- Result: 2001-01-01 00:00:00
```

question id: e0de0b74-a0e7-46c9-963d-480e5050188a


### How to insert specific date to a timestamp field with timezone?

```sql
INSERT INTO your_table(your_tmp_field)
VALUES(to_timestamp("2021-03-31 17:55:00", 'YYYY-MM-DD HH24:MI:SS') AT TIME ZONE 'UTC')
```

https://www.postgresqltutorial.com/postgresql-to_timestamp/
https://stackoverflow.com/questions/18913236/how-to-convert-string-to-timestamp-without-time-zone

question id: 314de4d2-6f7a-42fd-abe7-a36094539b0e


### How is self-referencing many-to-one relationship implemented in Django?


For example you have a table `users` with columns id and first_name like this
```sql
SELECT id, first_name FROM users ORDER BY id;
```

```shell
 id | first_name 
----+------------
  1 | first
  2 | Petr
  3 | Ivan
  4 | first
  5 | Артём
  6 | Артём
  7 | Whatever
  8 | Jay
(8 rows)
```

And you want implement that some users can be mentors to other users. 
For example, Petr is a mentor for first and Ivan, hence Ivan and first are mentees of Petr.
In django you add to User model field `mentor` with related name `mentees`. Now in Django you
can query user by these two fields. But what actually happened to your tables and how Djago
queries by mentor and mentees fields?
How does Django filters by mentor? How does it filter by mentees?

answer
Django adds just one foreign key to `users` table - field called `mentor_id` that is foreign key 
to `users.id`. 
Now to find users by mentor you use `WHERE mentor_id = 1`. As simple as that.

With filtering by mentees it's a bit more complicated. You don't have any `mentee` or `mentees` field,
only your `mentor_id` field.

Instead of it, to filter by mentees, for example, how is user that is mentor for first and Ivan, 
Django joins table users to itself, matching users.id with T2.mentor_id
so we get only rows where on the left side our mentors and on the right side corresponding mentees
Like this:

```sql
SELECT users.id, users.first_name, users.mentor_id, T2.id, T2.first_name, T2.mentor_id FROM users 
    INNER JOIN users T2 ON users.id = T2.mentor_id 
ORDER BY users.id ASC;
```

That means that for every user with mentor_id on the right side we get user with user.id on the left side
```shell
 id | first_name | mentor_id | id | first_name | mentor_id 
----+------------+-----------+----+------------+-----------
  2 | Petr       |           |  1 | first      |         2
  2 | Petr       |           |  3 | Ivan       |         2
(2 rows)
```

Once again. On the left side is users. On the right - T2. 
If you have user first with mentor_id 2, for him you get user with users.id 2.
Now all you need is to find users by their mentees is `WHERE T2.id = 2`. So T2.id is column of ids
of your mentees. 

So, in short, you don't have mentee or mentees column. Instead of it you join users table to itself
matching users.id and T2.mentor_id. Then T2.id is your mentee id.

question id: 02199faf-fad9-42e5-abf1-08b79dc73791 
 
 
### What is UPSERT?

In relational databases, the term upsert is referred to as merge. The idea is that when you insert a new row into the
 table, PostgreSQL will update the row if it already exists, otherwise, it will insert the new row. That is why we 
 call the action is upsert (the combination of update or insert).
 
https://www.postgresqltutorial.com/postgresql-upsert/

question id: c00e7085-6a07-4dae-ac9a-de03a8d9aa4e
 

### Select all rows from some table that were created today

Assuming that your postgres server has time zone set to UTC and you work from Moscow

table has `createdAt` field of type timestamptz 

answer

```sql
SELECT * FROM table
WHERE createAt >= CURRENT_DATE::timestamp AT TIME ZONE 'Europe/Moscow';
```

If you specify only CURRENT_DATE, you will get rows starting from 3 a.m in Moscow, not midnight

https://stackoverflow.com/questions/65784464/how-to-get-all-data-post-midnight-of-different-timezone

question id: 161de53f-ff6e-40da-9e26-1ac2403622b0


### How to select all rows that was created in the last 9 days?

Having column created_at of timestamptz type

answer
```sql
SELECT * FROM some_table
WHERE created_at > CURRENT_DATE - INTERVAL '9 day'
```

question id: 600b0db9-d205-4b23-8324-397e86160d48


### What's the order of executing an sql query?

FROM + JOIN  -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT

question id: af2b86c5-fa4f-4937-b35f-0b83b01d8f1b
 

### What's is Lateral?

The LATERAL is a keyword that:
- let your subquery to refer to columns of FROM items that appear before it in the FROM list
- apply the part after the LATERAL to each row before the LATERAL 

Anytime you hear the words “for each”, you are probably looking for a lateral join. 

As an example of where a lateral join is useful, let’s say we have a table people with an id column and an age column, 
and a table pets with columns id, owner_id and age. For the query, let’s say for each person over 30, we want to 
obtain the id of the oldest pet owned by that person. Anytime you hear the words “for each”, you are probably looking 
for a lateral join. This specific example can be done with the following query

```sql
SELECT people_sub.id, pets_sub.id
FROM (SELECT id FROM people WHERE age > 30) people_sub,
     LATERAL (SELECT pets.id
              FROM pets
              WHERE pets.owner_id = people_sub.id
              ORDER BY pets.age DESC
              LIMIT 1) pets_sub;
```

https://malisper.me/postgres-lateral-joins/

and maybe better example https://materialize.com/lateral-joins-and-demand-driven-queries/

question id: 83583dcf-c37d-4085-b6ff-16f21bd0382a


### Find the oldest pet for each person over 30 who obtain this pet
suspended as not being clear enough

Let’s say we have a table people with an id column and an age column, 
and a table pets with columns id, owner_id and age. For the query, let’s say for each person over 30, we want to 
obtain the id of the oldest pet owned by that person. The output should contain a person id and a pet id 

id, name, age
1 

answer
```sql
SELECT people_sub.id, pets_sub.id
FROM (SELECT id FROM people WHERE age > 30) people_sub,
     LATERAL (SELECT pets.id
              FROM pets
              WHERE pets.owner_id = people_sub.id
              ORDER BY pets.age DESC
              LIMIT 1) pets_sub;
```

https://malisper.me/postgres-lateral-joins/

question id: 53a26a82-1f24-41c4-bff5-f6642c23a2a3


### Select three top cities by population for each state

You have a table with data like these:
```sql
CREATE TABLE cities (
    name text NOT NULL,
    state text NOT NULL,
    pop int NOT NULL
);

INSERT INTO cities VALUES
    ('Los_Angeles', 'CA', 3979576),
    ('Phoenix', 'AZ', 1680992),
    ('Houston', 'TX', 2320268),
    ('San_Diego', 'CA', 1423851),
    ('San_Francisco', 'CA', 881549),
    ('New_York', 'NY', 8336817),
    ('Dallas', 'TX', 1343573),
    ('San_Antonio', 'TX', 1547253),
    ('San_Jose', 'CA', 1021795),
    ('Chicago', 'IL', 2695598),
    ('Austin', 'TX', 978908);
```

And the output should look like:
```
+-----+-----------+-------+
|state|name       |pop    |
+-----+-----------+-------+
|AZ   |Phoenix    |1680992|
|CA   |Los_Angeles|3979576|
|CA   |San_Diego  |1423851|
|CA   |San_Jose   |1021795|
|IL   |Chicago    |2695598|
|NY   |New_York   |8336817|
|TX   |Houston    |2320268|
|TX   |San_Antonio|1547253|
|TX   |Dallas     |1343573|
+-----+-----------+-------+
```

answer
Use lateral join

```sql
SELECT state, name, pop
FROM
    -- for each distinct state we know about ...
    (SELECT DISTINCT state FROM cities) states,
    -- ... extract the top 3 cities by population.
    LATERAL (
        SELECT name, pop
        FROM cities
        WHERE state = states.state
        ORDER BY pop
                DESC
        LIMIT 3
        ) top_cities
ORDER BY state, pop DESC
```

https://materialize.com/lateral-joins-and-demand-driven-queries/

question id: 4a321156-9dc5-47bd-9571-1880e38f9acd



### Find all info about all films that feature both actors Ed Chase and Spencer Depp

table film
```
       title       | film_id | release_year | length 
-------------------+---------+--------------+--------
 Chamber Italian   |     133 |         2006 |    117
 Grosse Wonderful  |     384 |         2006 |     49
 Airport Pollock   |       8 |         2006 |     54
 Bright Encounters |      98 |         2006 |     73
 Academy Dinosaur  |       1 |         2006 |     86
```

table actor
```
 actor_id | first_name |  last_name   |      last_update       
----------+------------+--------------+------------------------
        1 | Penelope   | Guiness      | 2013-05-26 14:47:57.62
        2 | Nick       | Wahlberg     | 2013-05-26 14:47:57.62
        3 | Ed         | Chase        | 2013-05-26 14:47:57.62
        4 | Jennifer   | Davis        | 2013-05-26 14:47:57.62
        5 | Johnny     | Lollobrigida | 2013-05-26 14:47:57.62
```

table film_actor
```
actor_id | film_id |     last_update     
----------+---------+---------------------
        1 |       1 | 2006-02-15 10:05:03
        1 |      23 | 2006-02-15 10:05:03
        1 |      25 | 2006-02-15 10:05:03
        1 |     106 | 2006-02-15 10:05:03
        1 |     140 | 2006-02-15 10:05:03
```

Expected output: there have to be two movies with ids 967 and 17

answer

1. In order to find films where both the actors are featured you have to denote them both in WHERE clause with OR
which will give you all the movies where at least one of them is featured. Some film_id can be encountered more than once,
which will mean that there are both of our actors. To find such movies we group by film_id having count(*) > 1. 

2. We join actor table to be able to query actors by their first and last name;

3. To select actual info about film from film tables, we use the former sql in WHERE film_id IN clause

```sql
SELECT *
FROM film
WHERE film_id IN (SELECT fa.film_id
                  FROM film_actor fa
                           INNER JOIN actor a ON a.actor_id = fa.actor_id
                  WHERE (first_name = 'Ed' AND last_name = 'Chase')
                     OR (first_name = 'Spencer' AND last_name = 'Depp')
                  GROUP BY fa.film_id
                  HAVING COUNT(*) > 1)

```

question id: f589b478-3b80-4126-8575-f42951aebe0c


### Find actors who both starred in the same movie

For example you have an actor_film table with columns film_id and actor_id. You need to find all the film_id's 
where actor_id's is 2 and 5. Like if you want to find films where both of this actors are starred, not where only one
or another. How would your query look?

answer
since WHERE actor_id = 2 AND actor_id = 5 doesn't make sense as one cell can have only one value (either 2 or 5 or
whatever), we have to find some other way to find what we want. 
So we will select  WHERE actor_id = 2 OR actor_id = 5 which will return all film ids where either of actors are starred.
But we need only movies with both these actors. In this result there are definitely some duplicate film ids, one for
actor_id = 2 and some for actor_id = 5. So, we just group by film_id having count more than one row - that's how
we will find the movies we need

```sql
SELECT film_id FROM actor_film
WHERE actor_id = 2 OR actor_id = 5
GROUP BY film_id
HAVING COUNT(*) > 1;
```

There is also another way
```sql
SELECT film_id FROM film_actor
WHERE actor_id = 2
INTERSECT
SELECT film_id FROM film_actor
WHERE actor_id = 5;
```

question id: ec8a8991-8334-427a-8878-b72b84943e73


### Find all movies that are among 30 the most positively rated and among the most expensive in replacement

table film
```
+-----------------+----------------+-----------+
|title            |replacement_cost|user_rating|
+-----------------+----------------+-----------+
|Uprising Uptown  |16.99           |4          |
|Chamber Italian  |14.99           |2          |
|Grosse Wonderful |19.99           |2          |
|Airport Pollock  |15.99           |2          |
|Bright Encounters|12.99           |2          |
|Academy Dinosaur |20.99           |2          |
|Ace Goldfinger   |12.99           |2          |
|Adaptation Holes |18.99           |4          |
|Affair Prejudice |26.99           |5          |
|African Egg      |22.99           |4          |
+-----------------+----------------+-----------+
```

expected output
```
+------------------+----------------+-----------+
|title             |replacement_cost|user_rating|
+------------------+----------------+-----------+
|Clockwork Paradise|29.99           |5          |
+------------------+----------------+-----------+
```

answer
Use intersection

```sql
SELECT title, replacement_cost, user_rating FROM (SELECT title, replacement_cost, user_rating FROM film ORDER BY user_rating DESC LIMIT 30) high_rated
INTERSECT
SELECT title, replacement_cost, user_rating FROM (SELECT title, replacement_cost, user_rating FROM film ORDER BY replacement_cost DESC LIMIT 30) costly
```

Maybe (and I really hope so there is a better way to do it)

question id: e41e97be-8182-412c-8c0e-437bd813af46


### What if you want to alter type of field, but it is referenced in foreign key constraint?

A foreign key usually duplicates a column in another table. What if you want to change a type of
this column? You can't, because these two columns (that one which is Foreign key and that one the
foreign key points to) would have different types. How to fix that?

answer
Drop foreign key constraint, change type of column in both tables.
Brief example: 

```sql
ALTER TABLE child DROP CONSTRAINT constraint_name ;
ALTER TABLE child ALTER COLUMN fk_col TYPE new_type;
ALTER TABLE parent ALTER COLUMN pk_col TYPE new_type;
ALTER TABLE child ADD CONSTRAINT constraint_name 
    FOREIGN KEY fk_col REFERENCES parent(pk_col);
```

https://stackoverflow.com/questions/28050549/changing-type-of-primary-key-when-you-have-foreign-key-constraint

question id: 4d16be6a-bdf0-4ced-a748-c75c53072859


### Sum on condition

You have a table with some transactions, like buying and selling stocks.
There are columns like id, ticker, payment, operation type (sell or buy) and quantity. 
Something like this:
```markdown
+----+--------------+--------+------------+--------+
|id  |operation_type|payment |ticker      |quantity|
+----+--------------+--------+------------+--------+
|5863|Buy           |-3747.86|USD000UTSTOM|51      |
|5867|Sell          |3673.25 |USD000UTSTOM|50      |
|5869|Buy           |-31.02  |STAG        |1       |
|5871|Buy           |-38.75  |GLW         |1       |
|5875|Buy           |-974.45 |USD000UTSTOM|13      |
|5879|Buy           |-3288.12|USD000UTSTOM|44      |
|5880|Buy           |0.00    |NRG         |1       |
|5882|Buy           |-41.96  |NRG         |1       |
|5884|Sell          |20.04   |AKNX        |1       |
|5886|Buy           |-41.50  |DRE         |1       |
+----+--------------+--------+------------+--------+
```
You bought and sold some stocks of AAPL. How would you calculate the eventual quantity of AAPL stocks that you have?
Result should look like this:
```sql
+------+----------------+
|ticker|number_of_stocks|
+------+----------------+
|AAPL  |1               |
+------+----------------+
```

answer
You need to sum up all quantity values where the ticker is APPL. Where operation_type is 'Sell' - quantity should be 
negative, where operation_type is 'Buy' - positive. If any other operation_type - 0. To implement this you need to use 
conditions inside SUM() function.
For example:
```sql
SELECT ticker,
       SUM(CASE
               WHEN (operation_type = 'Sell') THEN -quantity
               WHEN (operation_type = 'Buy') THEN quantity
               ELSE 0 END) AS number_of_stocks
FROM operation
WHERE ticker = 'APPL'
GROUP BY ticker
```
question id: 2a75d1d3-968e-4d17-bba3-5d4678ea35b8


### SELECT FOR UPDATE


### Why do we need select for update if we already have transactions?

Transactions do not always save us from race condition. Here is a simple example:

You have a banking app. Your user has 100 dollars on his account. 
There came two request for purchasing, one for 50 dollars, the second is for 70 dollars.
Process A: selects balance of the users, its 100 dollar, then he can afford 50 dollar purchase
Process B: selects of the users, its 100 dollar, then he can afford 70 dollar purchase
Process A: updates user balance. Now its 70.
Process B: tries to update user balance and can't, because there is not enough money already.

So what went wrong?
At first glance there is nothing bad that one process can select rows while other process also selects them.
However, in reality, the process that comes the second can make wrong decision because of that. In this
particular case, we need the process B not to select rows from the moment process A started selecting then
and until this process updated them and commited. Even if we wrap selecting and updating in one transaction, it
won't help because transaction doesn't lock rows from being selected. But `select ... for update` does.

https://ru.stackoverflow.com/questions/1064951/%D0%97%D0%B0%D1%87%D0%B5%D0%BC-%D0%BD%D1%83%D0%B6%D0%B5%D0%BD-select-for-update

http://shiroyasha.io/selecting-for-share-and-update-in-postgresql.html

question id: b772bcac-c375-4d78-a0d3-d2cfa1137c4a


### When does select for update lock and unlock rows?

Locks are taken during (usually at or near the beginning of) a command's execution. 
Locks (except advisory locks) are released only when a transaction commits or rolls back. 
There is no FOR UNLOCK, nor is there an UNLOCK command to reverse the effects of the table-level LOCK command.

That means, if you want to select ... for update something, you have to explicitly start a transcaction, 
select ... for update something, do what you want with these rows, than commit or rollback the transaction,
then the rows will be unlocked. If you just select ... for update something in auto-commit mode, you will
lock nothing.


https://stackoverflow.com/questions/15736640/when-does-select-for-update-lock-and-unlock

question id: a6467165-973e-4e1e-a55e-b878f6073f48


### How to drop a table? How to drop multiple tables at once?

answer
```sql
DROP TABLE table_name;

DROP TABLE tab1, tab2, tab3;
```

question id: c49b35d1-926a-4d45-bd7c-9b6718d08ef9


### How to define a new table from the results of a query? Why would we need it? 

answer:

```SQL
CREATE TABLE some_table_name AS SELECT * FROM
```

From documentation:
"CREATE TABLE AS creates a table and fills it with data computed by a SELECT command. 
The table columns have the names and data types associated with the output columns of the 
SELECT (except that you can override the column names by giving an explicit list of new column names)."
https://www.postgresql.org/docs/13/sql-createtableas.html


Why would one need it?
If you implementing a soft-delete in an existing application via moving deleted rows to another schema, that mirrors the original schema,
CREATE TABLE AS SELECT FROM will copy a table and data for you to your 'deleted' schema.

NB: I almost sure constraints and stuff like that won't get into copied table (but we don't need them for soft-delete).

question id: 03ada958-829c-4e40-be0d-233e1c0468b8

