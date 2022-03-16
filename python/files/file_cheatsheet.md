### How to read a text file line by line?

answer:

```python
with open("phone_numbers_shuffled.txt") as infile:
    for line in infile:
        do_something(line)
```

question id: c0a06a76-628d-4e8c-8c97-b6262ce28fe9


### Will reading a text file line by line load the whole file into memory?

```python
with open("phone_numbers_shuffled.txt") as infile:
    for line in infile:
        print(line)
```

answer:

It only reads one line at a time. When the next line is read, 
the previous one will be garbage collected unless you have stored a reference to it somewhere else

https://stackoverflow.com/questions/6475328/how-can-i-read-large-text-files-in-python-line-by-line-without-loading-it-into

question id: 5f81a982-e454-4a25-a034-f868e442cdd2
