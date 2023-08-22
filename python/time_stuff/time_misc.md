Useful links:
https://www.youtube.com/watch?v=TFa38ONq5PY
https://blog.ganssle.io/articles/2018/03/pytz-fastest-footgun.html
https://pypi.org/project/backports.zoneinfo/

### What does UTC stand for?

answer:

Universal Time Coordinated or Coordinated Universal Time

question id: b738b2b6-24ef-42d0-9424-f00d62e5b363


### How is GMT different from UTC?

answer:

GMT is an actual time zone, whereas UTC is a time standard that is 
used to keep time synchronized across the world.

GMT (Greenwich Mean Time) corresponds to UTC+0 time zone which is 0h

question id: 910ec6d2-3fc0-4e9f-bcac-31467ee26970


### How to get Unix timestamp?

answer:

```python
import time

print(time.time())  # 1671003247.1892054
```

question id: d5d3a6bd-0e17-4acc-971d-0076a8ec6026



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


### How to convert datetime object to a timestamp?
answer
```python
import datetime as dt

# create datetime object
date = dt(2021, 6, 21, 16, 16, 21)  # datetime.datetime(2021, 6, 21, 16, 16, 21) / 2021-06-21 16:16:21
# convert datetime object to timestamp
dt.datetime.timestamp(date)  # 1624281383.0
```

question id: 83127052-02f8-42d1-a4e4-85311693bcab



### How to create datetime object from given date?

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
import datetime as dt

dt.datetime(2012, 9, 1, 12, 15)  # datetime.datetime(2012, 9, 1, 12, 15) / 2012-09-01 12:15:00
```

question id: defd4a97-6a6e-4c21-a59b-5f9bf4157b09


### How to get local current time and date (naive) as a datetime object?

answer:

```python
import datetime as dt

dt.datetime.now()  # datetime.datetime(2022, 12, 14, 12, 0, 26, 988909)
```

question id: 32b0e1e4-0d19-4739-8af7-683f894bb8ac


### How to get current date and time as a string in this format? 2022-12-15T10:36:57.599483

answer

```python
import datetime

datetime.datetime.now().isoformat()  # '2022-12-15T10:36:57.599483'  
```

question id: 669476fa-3b28-4a34-9b66-65b3ef5c05c7



### How to get datetime object from ISO 8601 string (like this "2022-12-14T11:40:37")?

answer:

```python
import datetime as dt

dt.datetime.fromisoformat("2022-12-14T11:40:37") # datetime.datetime(2022, 12, 14, 11, 40, 37)
```

question id: 2efbd147-c158-4c21-ac70-2e02b7f1350a



### How to get naive current time and date as a datetime object, but in UTC+00?

answer

```python
import datetime as dt

dt.datetime.utcnow()  # datetime.datetime(2022, 9, 13, 7, 4, 51, 567978)
```

question id: a353370e-08b7-4dc7-a3cd-8866860847ca


### Print 'foo' if last_updated happened less than 3 minutes ago

```python
import datetime as dt
from random import randint

last_updated = dt.datetime.now() - dt.timedelta(seconds=randint(0, 360))

# your code here
```

answer:
```python
import datetime as dt
from random import randint

last_updated = dt.datetime.now() - dt.timedelta(seconds=randint(0, 360))


print(last_updated)
if last_updated > dt.datetime.now() - dt.timedelta(seconds=180):
    print("foo")
```

question id: 7c9ba475-03e8-432e-afa0-f9434f211969


### How to create a tz-aware datetime object with current date and time in UTC+00?

```python
import datetime as dt
from zoneinfo import ZoneInfo

print(dt.datetime.now(ZoneInfo("UTC"))) # datetime.datetime(2023, 8, 14, 15, 14, 3, 168666, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
```

question id: 8977c8e0-da6a-445f-94e8-95f1ce0146f2


### How to create a tz-aware datetime object with current date and time in a specified time zone?

Let's say, you want to get a current date and time in Las-Vegas

answer:
First, google "What is time zone in las vegas according to zoneinfo"

```python
import datetime as dt
from zoneinfo import ZoneInfo

print(dt.datetime.now(ZoneInfo("America/Los_Angeles")))
```

question id: d812a530-729c-400f-99ae-6dabf6c584c9



### How to convert a timezone-aware datetime to another timezone?


Let's say you have created a timezone-aware object like this:
```python
import datetime as dt
from zoneinfo import ZoneInfo  # backport.zoneinfo in > Python 3.8

tz = ZoneInfo("Asia/Yerevan")

yerevan = dt.datetime.now(tz)

print(yerevan) # 2022-12-16 15:05:24.376970+04:00
```

Given this is time in Yerevan, what's the time in New York then?

answer:

```python
import datetime as dt
from zoneinfo import ZoneInfo

tz = ZoneInfo("Asia/Yerevan")

yerevan = dt.datetime.now(tz)

new_york = yerevan.astimezone(ZoneInfo("America/New_York"))

print(yerevan)  # 2022-12-16 15:56:55.898154+04:00
print(new_york)  # 2022-12-16 06:56:55.898154-05:00
```

question id: aa16c57a-e179-4add-b571-6f4f67e2a3b5


### How to make a naive datetime object to be timezone-aware?

Let's say you already have a naive datetime object like:

```python
import datetime as dt

yerevan_naive = dt.datetime.now()

print(yerevan_naive)  # 2022-12-16 16:13:32.841679
```

How to add a timezone?

answer:

```python
import datetime as dt
from zoneinfo import ZoneInfo

yerevan_naive = dt.datetime.now()

print(yerevan_naive)  # 2022-12-16 16:13:32.841679

yerevan_aware = yerevan_naive.replace(tzinfo=ZoneInfo("Asia/Yerevan"))

print(yerevan_aware)  # 2022-12-16 16:13:32.841679+04:00
```

question id: 300bb509-9033-460e-ab66-ed4cd6c5b16b


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



### How to get date of today as a string

```python
from datetime import datetime

datetime.now().strftime("%Y-%m-%d")

# or 

str(datetime.now().date())
```

question id: 8f80a2dd-bcd6-47cc-9ccc-5c93c968bf98



### How to get a time interval so as to be able to add or subract it from a datetime object?

answer:

```python
import datetime as dt

dt.timedelta(seconds=100)
```

From doc:
```python
from datetime import timedelta
delta = timedelta(
        days=50,
        seconds=27,
        microseconds=10,
        milliseconds=29000,
        minutes=5,
        hours=8,
        weeks=2
    )
# Only days, seconds, and microseconds remain
# delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)
```

question id: d4bd8cbf-a695-49c8-8631-a106f17c0c74