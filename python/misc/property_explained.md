https://www.programiz.com/python-programming/property


### What is `property`?

It is a built-in function that creates and returns a property object. The syntax of this function is:

```python
property(fget=None, fset=None, fdel=None, doc=None)
```
where,

- fget is function to get value of the attribute
- fset is function to set value of the attribute
- fdel is function to delete the attribute
- doc is a string (like a comment)

These function arguments are optional.

Usually `property` is used to make pythonic getter and setter for a class attribute.

question id: 3acf1cc8-382d-4f9e-84ee-c6ea00fd4ce8



### What problems does `property` solve?

The same as getters and setters, for example dynamic construction of returning value with getter or validation of 
input value in setter. 
Also you don't have to change any dependent code when you move from using a usual
class attribute to a method via property interface

question id: 67b48c82-6fdd-4a48-91eb-4a83306f6d05


### What are `self.temperature` and `self._temperature` in this code example?

```python
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value
```

answer

`self.temperature` a property object which provides an interface to this private variable `self._temperature`
where the actual value of temperature is stored

question id: 2ac46180-b42c-49bf-8dd1-b31abbf04a06


### Write an `Employee` class who has `wage` attribute

There should be validation that the wage cannot be lower than $15

answer

```python
class Employee:
    """Some employee."""

    def __init__(self, wage=15):
        self._wage: int  # private variable
        self.wage: int = wage  # interface to interact with self._wage

    @property
    def wage(self):
        return self._wage

    @wage.setter
    def wage(self, value):
        print('setting wage...')
        if value < 15:
            raise ValueError("The lowest wage is $15")
        self._wage = value

emp = Employee()

print(emp.wage)
emp.wage = 13
print(emp.wage)
```

question id: 3643da23-a801-4c21-85a9-25f8313eec16


### Write a `Employee` class who has `wage` attribute

`self.wage` should be comprised of `self.hours` and `self.hour_price`

answer

```python
class Employee:
    """Some employee."""

    def __init__(self, hour_price=0, hours=0):
        self.hour_price: float = hour_price
        self.hours: float = hours

    @property
    def wage(self):
        return self.hour_price * self.hours


emp = Employee(hour_price=15, hours=140)

print(emp.wage)
emp.wage = 13  # should fail
print(emp.wage)
```

question id: e272c964-1771-42fb-a0eb-adee6f10c50d