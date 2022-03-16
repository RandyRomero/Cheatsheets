### How to sort a huge file with random phone numbers that doesn't fit into memory?

You are given a text file that looks like this:
`+79149238383
+79215392047
+79235940482
`

...and so on. There are all numbers between +79000000000 and +79999999999 in random order. The file 
is around 16 gigs. You need to sort it with Python. How to do it without exceeding your RAM of 16 gigs? 
What would be your steps?

answer

first:
- read the file line by line
- add lines to a list
- when the list has enough lines - sort it
- save this chunk to a file
- repeat for the rest of lines in the file

then:
- open resulting file buffer
- open all the chunks
- pass all the chunks to heapq.merge function
- pass the result of merge function directly to resulting_file.write()

Merge function is lazy, so you won't load all the files to the memory at once
Don't forget: chunks must be sorted so to merge thems

https://github.com/RandyRomero/work_with_phone_numbers/blob/main/sort_random_phone_numbers.py

question id: f2a695e0-f4f5-49a0-ae4b-7c4d4fda7643

