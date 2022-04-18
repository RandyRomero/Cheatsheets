relational vs non-relational

### What are differences between relational and non-relational databases?

Relation databases are based upon tables and foreign keys.
Tables contain rows of our data and foreign keys allow us to create relations between tables.
Relational dbs are good for well-structured data, because they have a lot of tools to make
sure our data is consistent and complies with defined structure.

Non-relation databases in general are more suitable for data that is not very well structured, for example
a JSON with a tons of arbitrary keys.

Also, NoSQL databases are much better at horizontal scaling and at handling a lot of connections at the same time,
which is good for applications with high-load.

Btw, in some relation databases, there is an ability to store unstructured data. 
For example, there is JSONB type in Postgres, where you can store json.
And not only store, but query as well. So you can have best of two worlds.

question id: 89fbb3f8-de39-4649-8ff0-29026842e5c6



structure:
table | table or document (json) or graph

storage:
typically on one machine | typically distributed

scale:
nosql databases are much easier to scale

access:
sql | rest api or vendor specific language



Main two things that relation databases are based upon is tables and foreign keys.
Tables contain rows of our data and foreign keys allow us to create relations between tables.


In NoSQL databases information can be stored as a document (like in MongoDB) or as a graph (there are other types.)
NoSQL database do not care that much about relations.

NoSQL databases are better for storing unstructured data whereas relation databases win where you 
have information with clear and firm structure and you want to keep this structure.

In relational database writing data is slower because you have to make sure that data is consistent and complies with the structure of your database, but
reading is much faster because everything is structured.

Writing to a NoSQL database is generally faster than in relation database because there are not so many strict rules and check and data is mostly
unstructured. However, to get data in structured way from NoSQL database is slower.

NoSQL databases are good for fast writing in them since we are writing unstructured data and don't spend time on checks and validations as in relational databases. Also, NoSQL dbs are better at scaling and they work better with tons of connections, whereas relation databases do not scale that well and not good at handling a considerable number of connections.

