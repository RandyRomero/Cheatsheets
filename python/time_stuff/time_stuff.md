### How to parse string with a time to datetime object?

For example, you have this string '2021-06-07 12:47:30'

answer
```python
import datetime as dt

my_time = '2021-06-07 12:47:30'

date_time = dt.datetime.strptime(my_time, "%Y-%m-%d %H:%M:%S")
print(date_time)  # 2021-06-07 12:47:30
```

format reference:
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

question id: 5e2e5f87-6612-4729-8189-53a20b9d4e07


### How to convert a timestamp to a datetime object?

answer
Python's datetime.datetime has special method for it - .fromtimestamp()

```python
import datetime as dt

timestamp = 1545730073
dt_object = dt.datetime.fromtimestamp(timestamp)

print(dt_object)
```

question id: 3790bfec-6e5e-4a3b-9485-c4e0e62cd1e2


### How to create datetime object from given date and time?

For example, you want to create a datetime object that represents the 1st of September of 2012.
How would you do that? 

answer
```python
from datetime import datetime as dt

dt(2012, 9, 1)  # datetime.datetime(2012, 9, 1, 0, 0) / 2012-09-01 00:00:00
```

question id: d95d684b-4777-443f-8b84-f92a9ac71b98


### How to create datetime object from given date and time?

For example, you want to create a datetime object that represents the 1st of September of 2012, 
quarter after noon (12:15)
How would you do that? 

answer
```python
from datetime import datetime as dt

dt(2012, 9, 1, 12, 15)  # datetime.datetime(2012, 9, 1, 12, 15) / 2012-09-01 12:15:00
```

question id: defd4a97-6a6e-4c21-a59b-5f9bf4157b09


### How to convert datetime object to a timestamp?
answer
```python
from datetime import datetime as dt

# create datetime object
date = dt(2021, 6, 21, 16, 16, 21)  # datetime.datetime(2021, 6, 21, 16, 16, 21) / 2021-06-21 16:16:21
# convert datetime object to timestamp
dt.timestamp(date)  # 1624281383.0
```

question id: 83127052-02f8-42d1-a4e4-85311693bcab


### How to create a datetime object of a date that is exactly 21 days ago?
answer
```python
from datetime import datetime as dt
from datetime import timedelta

# create datetime object
date = dt(2021, 6, 21, 16, 16, 21)  # datetime.datetime(2021, 6, 21, 16, 16, 21) / 2021-06-21 16:16:21

TWENTY_ONE_DAYS_AGO = date - timedelta(days=21)
```

question id: f244d2a9-dd7f-4064-9209-5361810f816e


### How to get current date and time in this format? 2020-10-15T00:00:00.000000+03:00

```python
import datetime

datetime.datetime.now().astimezone().isoformat()  # '2021-06-08T19:28:52.456761+03:00'  
```

https://stackoverflow.com/questions/2150739/iso-time-iso-8601-in-python

question id: 96a3ab8f-8427-4648-a48d-ea4fc812c623



### How to get date of today as a string

```python
from datetime import datetime

datetime.now().strftime("%Y-%m-%d")

# or 

str(datetime.now().date())
```

question id: 8f80a2dd-bcd6-47cc-9ccc-5c93c968bf98

