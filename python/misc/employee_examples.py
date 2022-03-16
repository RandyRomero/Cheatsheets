
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