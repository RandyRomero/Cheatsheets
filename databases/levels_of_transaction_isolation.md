Useful links:
https://www.postgresql.org/docs/current/transaction-iso.html

### What are level of transaction isolation in databases?

Levels of isolation are basically rules how a transaction can interact with
data that is modified by another transaction.

Let's take PostgreSQL for example. Every data maniputlation in PostgreSQL happens
in a transaction (in order to support working on a database from multiple connections).
There are different cases when actions in a transaction can interfere with actions in another
transaction. In order to handle this cases and provide data integrity PostgreSQL
provides set of rules called level of transactions.

A brielf example. Can a transaction read not-yet-committed data of another transaction?
If level of isolaction for this transaction is set to Read Committed, that means
that this transaction cannot read not-yet-committed data of other transactions.

question id: 8e45a9c5-dd32-40bb-af0c-3e63ac84c886


### Can you name all levels of transaction isolation?

The SQL standard defines four levels of transaction isolation:
- Read Uncommitted
- Read Committed
- Read Repeatable
- Serializable

Note: PostgreSQL doesn't have Read Uncommitted level. Instead, the default is Read Committed.

question id: e523a7f0-a137-4d18-9329-016e585ef31d


### What is Read uncommitted level of transaction isolation?

It is when a transaction is allowed to read not-yet-committed data of another transaction.

question id: ce7d6663-d3ef-46a6-9910-52b5ea5717b0


### What is Read Committed level of transaction isolation?

It is when a transaction is not allowed to read not-yet-committed data of another transaction.

question id: 916e6427-12b9-4dd8-8b39-981491ce9586


### What is Read Repeatable level of transaction isolation?

The Repeatable Read isolation level means that you one transaction
cannot modify data in rows that are being read by another transaction.
So to avoid situations when your transaction reads data at the begging,
then reads it again after a while and the data have been changed already.
So if the data is committed already by the transaction T2, T1 still won't see
this changes.

https://jennyttt.medium.com/dirty-read-non-repeatable-read-and-phantom-read-bd75dd69d03a

question id: 2effdfe3-ba07-4592-b523-194755cd7974


### What is Serializable level of transaction isolation?

It the most strict level of isolation that exists to avoid
phantom read - when is you perform the same SELECT query 
more than once during one transaction, you get different (number
of) rows.

In this level of isolation transactions run as they would if you 
would run sequentially one by one in order.

https://jennyttt.medium.com/dirty-read-non-repeatable-read-and-phantom-read-bd75dd69d03a
https://shiroyasha.io/transaction-isolation-levels-in-postgresql.html

question id: 9a587e88-d949-401a-bad2-8cbf0228f135


