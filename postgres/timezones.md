### How to check which timezone is set in your postgres database?

```sql
SHOW timezone;
```

question id: bd160427-4661-4bae-ad3d-88f5104e4f0b

### What the difference between timestamp and timestamptz in PostgreSQL?

These 2 PostgreSQL data types store date and time in a single field, the difference is that “timestamptz” converts 
the value to UTC and “timestamp” doesn’t.

Example:
```shell
SET TIME ZONE 'UTC';

SELECT
'2000-01-01 00:00:00 +05:00'::timestamp as "Timestamp without time zone",
'2000-01-01 00:00:00 +05:00'::timestamptz as "Timestamp with time zone";

+---------------------------+------------------------+
|Timestamp without time zone|Timestamp with time zone|
+---------------------------+------------------------+
| 2000-01-01 00:00:00       |1999-12-31 19:00:00+00  |
```

The “timestamp” data type ignores the offset (‘+05:00’) from the original value.
The “timestamptz” data type takes into account the offset (‘+05:00’) from the original value.

https://medium.com/building-the-system/how-to-store-dates-and-times-in-postgresql-269bda8d6403

question id: fde7a328-aaa2-43db-a3fc-fe5fe4742d2

### What is the flow of working with timestamptz in PostgreSQL?

Let's imagine we want to build some a char for users from all over the world. Each of them should see messages with
time and date of their creation in their time zone. 
To do this:
- we make sure that our timezone setting in PostgreSQL is set to UTC and that we save time and date of 
every message as `timestamptz`. 
- our chat-client sends to PostgreSQL time aware timestamps with local time when user 
created the message. 
- database, storing in timestamptz field, converts this value to UTC +0 timestamp. That means that 
2000-01-01 00:00:00 +05:00 would be stored as 1999-12-31 19:00:00+00. 
- when our chat-client gets time and dates of messages from database, it performs backwards convertion from UTC +0 to 
whatever timezone user has. That means back from 1999-12-31 19:00:00+00 to 2000-01-01 00:00:00 +05:00

https://medium.com/building-the-system/how-to-store-dates-and-times-in-postgresql-269bda8d6403

question id: c486ae89-4f5b-44da-b445-1b680a751411