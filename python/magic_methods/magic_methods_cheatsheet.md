### What is the difference between __str__ and __repr__?

They are both methods to get a concise string representation of object.

answer

str is called first by default and it should be very human readable. 
When there is no str, Python interpreter falls back to using repr, 
which is unambiguous representation of an object.
 It is considered as a good practice to make this representation to 
 be able to recreate your object, but it isn't always attainable.

Example: 
```python
import datetime
today = datetime.date.today()

str(today)
'2017-02-02'

repr(today)
'datetime.date(2017, 2, 2)'
```

question id: f10d5449-dd12-437c-91c9-82390f723625