## Introduction to models

https://docs.djangoproject.com/en/3.1/topics/db/models/

### What's model in Django?

It's a Python class derived from one of Django's special classes which maps to a single database table.
Each attribute of this class represents one column in a database table.

https://docs.djangoproject.com/en/3.1/topics/db/models/#module-django.db.models

question id: 423bda2b-7177-4f52-aa57-d28ae28e3428

### Define a Person model, which has a first_name and last_name

```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```

question id: a4df2ad2-72f3-480d-9089-d7698c8ac19a

### How to define choices in Django?

```python
from django.db import models

class YourChoicesName(models.TextChoices):
    """Master status choices."""

    choice_one = "name1_in_database", "human name"
    choice_two = "name2_in_database", "human name"

class Person(models.Model):

    first_name = models.Charfield(choices=YourChoicesName)
```

It is not only and certainly not the default way, but it will do.

question id: 5621a16c-7caf-424e-9986-5cf60fdb630e

### Define two models with Many-to-one relationship in Django

A Car model has a Manufacturer – that is, a Manufacturer makes multiple cars but each Car only has one Manufacturer.
 
```python
from django.db import models

class Manufacturer(models.Model):
    pass

class Car(models):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
```

https://docs.djangoproject.com/en/3.1/topics/db/models/#many-to-one-relationships

question id: 748a50ad-c9ac-4b5b-b38b-762e5452b422

### In case of Many-to-one relationship, where should be a field with foreign key? 

For example, A Finger has a Person – that is, a Person has multiple fingers but each Finger only has 
one Person. Where should be a field with foreign key - in Person model or in Finger model?

answer

On "many" side of the relationship. In this cas model Finger should have foreign key to Person
```python

class Finger(models.Model):

    person = models.ForeignKey(Person, on_delete=CASCADE)
```

question id: 1d149e02-aba6-4fa4-b189-055cc69ac708


### Define many-to-many relationship in Django

For example, if a Pizza has multiple Topping objects – that is, a Topping can be on multiple pizzas and each Pizza 
has multiple toppings - how would you represent that?

```python
from django.db import models

class Topping(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping, related_name="pizzas")
```

It doesn’t matter which model has the ManyToManyField, but you should only put it in one of the models – not both.

question id: 2bd8ef4f-6219-4cd3-b9ca-db114195574b

### When do you need to specify intermediate table for many-to-many relationship in Django?

When you want to store extra info about the relatioship. For example, date when it is created, reason, etc.
Otherwise you don't need to specify it explicitly and Django will create it for you.

question id: 3205487d-8eba-41bd-b05d-8f632865c2fb


### Create two models with many-to-many relationship in Django

Consider the case of an application tracking the musical groups which musicians belong to. There is a many-to-many 
relationship between a person and the groups of which they are a member, so you could use a ManyToManyField to 
represent this relationship. However, there is a lot of detail about the membership that you might want to collect, 
such as the date at which the person joined the group, that's why you also need to specify intermediate table.

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=128)
```

question id: c1d04ade-45b3-4341-a13c-72f5cc326ad8


### Having the following tables with m2m relationship, create a new person called Paul McCartney, new band
called "The Beatles" and add Paul to the band

```python
from django.db import models

class Person(models.Model):
    name = models.Charfield(max_length=128)
    
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.Charfield(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.Charfield(max_length=128)
```

answer

```python
paul = Person.objects.create(name="Paul McCartney")
beatles = Band.objects.create(name="The Beatles")
m1 = Membership.objects.create(person=paul, 
                               band=beatles, 
                               date_joined=date(1962, 8, 16), 
                               invite_reason="Needed a new singer")
m1.save()
beatles.members.all()  # <QuerySet [<Person: Paul McCartney>]>
paul.band_set.all()  # <QuerySet [<Group: The Beatles>]>
```

question id: e632d3ce-04b2-4461-8366-83695043f450


### Having the following table, find all the bands with a member whose name starts with 'Paul'

```python
from django.db import models

class Person(models.Model):
    name = models.Charfield(max_length=128)
    
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.Charfield(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.Charfield(max_length=128)
```

answer 

```python
bands = Band.object.filter(members__name__startswith="Paul")
bands  # <QuerySet [<Group: The Beatles>]>
```

question id: 5ecf3ff0-3339-4070-a356-fde94fea7a30


### Having the following table, all the members of the Beatles that joined after 1 Jan 1961

```python
from django.db import models

class Person(models.Model):
    name = models.Charfield(max_length=128)
    
    def __str__(self):
        return self.name

class Band(models.Model):
    name = models.Charfield(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')
    
    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.Charfield(max_length=128)
```

answer

```python
Person.objects.filter(band__name="The Beatles", 
                      membership__date_joined__gt=date(1961, 1, 1))  # <QuerySet [<Person: Ringo Starr]>
```

question id: 78db5b6c-f260-4852-bf07-41cb2fe69645

### Why to use meta class in django model?

Model metadata is “anything that’s not a field”, such as ordering options (ordering), database table name (db_table), 
or human-readable singular and plural names etc

full reference: https://docs.djangoproject.com/en/3.1/ref/models/options/

question id: 89cdd2a0-d0dc-49fc-9075-7788826016e8

### How to do something extra on saving django model?

answer: redefine .save() method of the model

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        do_something()
        super().save(*args, **kwargs)  # Call the "real" save() method.
        do_something_else()
```

https://docs.djangoproject.com/en/3.1/topics/db/models/#overriding-predefined-model-methods

question id: 4f32bdd4-5a1f-45e7-8484-381f2d4ef2a1


### How to prevent saving to the database on condition?

Redefine redefine .save() method of the model - return None if condition

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if self.name == "Yoko Ono's blog":
            return # Yoko shall never have her own blog!
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.
```

https://docs.djangoproject.com/en/3.1/topics/db/models/#overriding-predefined-model-methods

question id: 3ca28952-16ec-4b2d-8bd4-f420f204af4f


### Usually for m2m fields and for many-to-one relations Django creates a field to use for the relation from the related 
object back to this one with a name like `your_field_set` automatically.
How to give a proper name to such field? 

Example: 
If a Person can have a lot of Cat, to get all the cats that belong to this person would be something like
```python
person = Person.objects.filter(id=1).first()
person.cat_set.all()  # <QuerySet [<Cat: Kitty>, <Cat: Max>]>
```

How to make it like 
```python
person.cats.all()
```

answer
To provide `related_name` arg to ForeignKey field 

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

class Cat(models.Model):
    name = models.CharField(max_length=128)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='cats')
```

question id: c3b02e08-2257-4bbe-9091-37af2d11f6a7

