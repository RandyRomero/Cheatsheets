### Example of one to one relationship

```python
from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return "%s the place" % self.name

class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)
```

### How to create a new Restaurant entity?

Having Place and Restaurant models with one-to-one relationship like here:
https://docs.djangoproject.com/en/3.1/topics/db/examples/one_to_one/

answer:
First you have to have or create a Place. You cannot create a new Restaurant without connecting it
to some Place

so having our Place:
```python
nice_place = Place.objects.filter(id=1).first()
if not nice_place:
    return None

rest = Restaurant.objects.create(place=nice_place, serves_hot_dogs=True, serves_pizza=False)
```

question id: 156175b4-2ded-4402-a0bb-b5df55f4c977