

### How to make a file with a list of random phone numbers from +79000000000 to +799999999999

Describe possible solution

The problem is that in order to shuffle a list of numbers we have to have this list all in memory at once.
What can we do?


0. define suitable numbers of chunks. Like, if we divide this list of numbers by 10, 1/10 of a list
is definitely going to fit into memory. Also, the fewer chunks the better (faster).
1. open/create as many new files as we have chunks all at once
2. generate one number at a time successively, from first to the last, write it one-by-one to the file-buffer, but every time to a random one

Let's say we have to make a random list of 9 numbers from 1 to 9 in chunks of 3 numbers.
If we write them to the chunks successively, then shuffle each of them, then merge them, we will
end up with something like this:

`[3, 1, 2][5, 4, 6][ 9, 7, 8]`

I hope you see the picture - the list is not shuffled enough. That's why we need to write every number not to a 
successive file, but to a random file, so any number can end up in any chunk.

3. write all the files to disk
4. open final file, in a loop open each file-chunk with numbers, shuffle lines, write them to final-file buffer
5. write the final file to the disk

Example:
https://github.com/RandyRomero/work_with_phone_numbers/blob/main/generate_random_phone_numbers.py

question id: b515f7d3-a636-43cc-80ed-d834fc878618
