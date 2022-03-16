https://ruheni.dev/posts/sql-table-inheritance/


### What are three ways to store models/tables which have common columns as well as its own columns?

For example, you have three instances: text_document, picture and audio. All of them should have the following
columns: 
- id
- created_at
- creator_id
- name
- size
- total_character_num
- total_word_num

text_documents also has the following columns:
- total_character_num
- total_word_num

picture has the following columns:
- resolution
- exif

audio has the following columns:
- bitrate
- genre

What are three ways to orginize these tables in a database?


## Option 1 (Concrete Table Inheritance)
You can just create three separate tables: Text Document, a Picture and an Audio.

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/databases/data modeling/concrete_table_inheritance.png">](concrete_table_inheritance.png)

Pros: 
- it's as simple as that

Cons:
- you have to create a lot of same columns, like name, size, creator with the same types in each table (thougn in ORM only once and than inherit from this model)
- it will be difficult to manage multiple types at once (because each table will have its own columns with different types)


## Option 2 (Single Table Inheritance)
We can put all instances in one table, called, for example, File.
We will add special column "type" to distinguish Text Document from Picture and so on.

For each Instance/Type the table will have some columns related only to this type. For example, only Audio type will have bitrate.

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/databases/data modeling/sti.png">](sti.png)

Example:
| id 	| created_at 	| creator_id 	| name             	| size    	| type          	| total_character_num 	| total_word_num 	| resolution 	| exif       	| bitrate    	| genre          	|
|----	|------------	|------------	|------------------	|---------	|---------------	|---------------------	|----------------	|------------	|------------	|------------	|----------------	|
| 1  	| 2022-01-01 	| 3          	| report.docs      	| 2097152 	| text_document 	| 10 000              	| 750            	| null       	| null       	| null       	| null           	|
| 2  	| 2015-05-05 	| 3          	| IMG1090.jpg      	| 4194304 	| picture       	| null                	| null           	| 4096x3810  	| some byres 	| null       	| null           	|
| 3  	| 2020-12-12 	| 3          	| jingle_bells.mp3 	| 5242880 	| audio         	| null                	| null           	| null       	| null       	| 128 kbit/s 	| cristmas_songs 	|


Pros:
- you don't how to create and store repetitive columns for common attributes
- easy to query multiple instances at once

Cons:
- not suitable for case there are a lot of different types because there will be a lot of nulls in each row
- not suitable for cases where each type has a lot of its own columns - table will be a mess
- data not normalized
- has overhead of cheking type of instance every time we want just to select all instances of one type
- cannot use NOT NULL constraint for a column that relates to only one instance


## Option 3 (Multi-Table inheritance)

Common columns are stored in one separate table. 
Columns that are unique for every instance will be stored in separate tables - one table for one instance.
Rows in a parent table (with common columns) will have 1-to-1 relationships with rows in each of child tables.

[<img src="/home/aleksandr/yad/Studies/Cheatsheets/databases/data modeling/mti.png">](mti.png)

Pros:
- data is normalized
- it is DRY
  
Cons:
- a lot of joins

question id: faa5fd5d-e1ac-432c-a1e5-b15d9a111928