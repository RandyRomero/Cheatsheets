### How to read and print out content of a *.csv file?

answer

```python
import csv

with open("your_csv_file.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row) # first one will be header, the others will be with actual rows
```

https://realpython.com/python-csv/

question id: 971aa8e4-dd12-4fc4-83c1-293340ccae1f


### How to write to csv file?

```python
import csv

with open('your.csv', mode='w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(['John Smith', 'Accounting', 'November'])
    csv_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

If quoting is set to csv.QUOTE_MINIMAL, 
then .writerow() will quote fields only if they contain the delimiter or the quotechar. This is the default case.

question id: 29a99a5d-aa6f-44bc-93cb-ba5ab5724628