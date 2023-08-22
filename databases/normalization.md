### What is normalization?

Normalization is the process of efficiently organizing data in a database in accordance with a series of so-called normal 
forms in order to reduce data redundancy and improve data integrity.

question id: cd06a9f6-e2fc-4812-bd74-1456ad07d935


### How to achieve the 1st Normal Form?

answer
1. Columns contain atomic values (one value per cell)
2. Columns contain values of the same type
3. Columns should have unique names
4. Row order does not matter

question id: 7f64e8ac-01e4-4295-814e-b22b7a4c2c18


### How to achieve the 2nd Normal Form?

1. Table should be in the 1st Normal Form
2. No partial dependencies

The second thing means that all of you field that is not part of a primary key should depend only
on the whole primary key (in case it is composite).

For example you have intermediate m2m table `author_book` that has `author_id` and `book_id`. It
does not make sense to put in it a field like `isbn` because it does not depend on both `author_id` 
and `book_id`. It depends only on `book_id` so it should be in `book` table. In case it is in 
`author_book` table, it will be partial dependencies that infringes second noraml form (2NF)

https://www.youtube.com/watch?v=WSKuxoAN35g

question id: d3c5bbe6-bbdd-40f9-8da8-43afd9c956d8

