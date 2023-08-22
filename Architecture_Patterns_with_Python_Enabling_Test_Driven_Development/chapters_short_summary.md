### 1: Domain Modeling

https://www.cosmicpython.com/book/chapter_01_domain_model.html




### 12: Command-Query Responsibility Segregation (CQRS)

https://www.cosmicpython.com/book/chapter_12_cqrs.html


In CQRS (Command-Query Responsibility Segregation) we follow one simple rule: functions should either modify state or answer questions, but never both. 

For example, POST handle (like /batch) should not return created object. Instead, it should redirect to resource 
endpoint (like /batch/123) or return Location header containing the URI or our new resource


Sometimes it is reasonable to have separate views for read and write operations, especially in the following cases:
- there are a lot of business logic around one type of operations (read or write), but much less around the other type
- number of reads is much greater on average than number of writes or vice versa

If a read opearion requires a lot of joins and you have a lot of read operations, you can create a separate denormalized table, where you will
gather infromation as it is appears or updates in original tables.
In other words, as you write, you write in a bunch of related normalized tables, at the same time updating the denormalized table made entirely for reads.
My suggestin is to use Postgres Maretialized View istead. At the same time, you can even store your separate read table in Redis.


### Appendix E: Validation

Validate as little as possible. Read only the fields you need, and don’t overspecify their contents. 
This will help your system stay robust when other systems change over time.

