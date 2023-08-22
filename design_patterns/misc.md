### What can you do if your service has more read operations than write operations and these read operations use a lot of joins?

In order to gain performance, you can use a different table for the reads. It could be Postgres Materialized View, it could be
a manually made denormalized table updated on write operations to original tables, it could be even data in Redis also updated
on write operations to the original table.

https://www.cosmicpython.com/book/chapter_12_cqrs.html

question id: a0031911-e101-4045-9cf9-3e7e3cb1a60cs