Useful links:
https://www.postgresql.org/docs/current/transaction-iso.html

### What are levels of transaction isolation in databases?

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

First of all, a repeatable read transaction cannot modify or lock rows changed by other transactions after the repeatable read transaction began.
So, if two or more transaction will try to update the same data at the same time, as soon as one transation has committed an update, the other one will fail.


Also, all commands within a transaction in this mode will see the data in the database as it was when the transaction has started.


The Repeatable Read level of isolation solves a phenomena that is called 'nonrepeatable read'.
Non-repeatable read is when, for example, two transactions first select, than update a certain row or bunch of rows like this:

Transaction 1: selects row id 1
Transaction 2: selects row id 1
--at this point both transaction read exactly the same values from the rows--
Transaction 1: updates row id 1
--at this point the data in row id 1 has changed, but Transaction 2 doesn't know it--
Transaction 2: updates row id 1

So we can end up with inconsistent state because Transaction 2 updates the row based on what its state was 
before Transaction 1 has changed it.
It's the same situation where we can use SELECT FOR UPDATE.


A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read).

The difference between Repeatable Read and SELECT FOR UPDATE that in the first case your transaction sees that data as it was before the transaction,
but cannot change this data if it was changed by another transaction concurrently.
With SELECT FOR UPDATE a transaction cannot even see rows that another transaction works with.

https://www.postgresql.org/docs/current/transaction-iso.html

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


