### How many there are styles of inheritance in Django and what are they?

- Abstract base classes (you just don't want to redefine the same fields in Python class, so you inherit one to avoid it)
- Multi-table (or concrete) inheritance (each subclass has its own table)
- Proxy models - you want a separate model for the same table, but with changed ordering or something

https://docs.djangoproject.com/en/3.1/topics/db/models/#model-inheritance

question id: 3ff1bbdd-7747-47c8-9948-839ab2c0d220


### How to put some common information into a number of other models without repeating yourself? For example some
common fields for different model/tables

answer:

Create a class with common info, that inherits from models.Model. Make new classes that inherit from this one. But in 
order to avoid autocreation of the table for a common class add to its meta info flag `abstract = True`. 

Like this 

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```
 
question id: 93ceb20b-1789-48d1-bfe9-6e31954ed8a2

### What does mean `abstract = True` in Meta class of the Django model?

That the class is only to be inherited from, it does not create its own table.

Example: 

```python
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
```

question id: 89cf9ae1-7445-4857-9b1c-95c12ec488e4


### What's abstract base classes inheritance in Django for?

It's like usual inheritance in Python for example, but in Django it allows you not to declare same fields to 
different-but-similar models. Like in this example:

```python
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

Under the hood you get as many table as you have child classes.

question id: 65942051-f208-4f2b-aa32-242b461b88e7


### What are some downsides of abstract base classes inheritance in Django?

in short:
- many common fields in diffetent table
- cannot query all child models at once by parent model without raw sql
- cannot use constraints on common fields (e.g. you have `name` column in N tables, but you cannot specify that it
should be unique among all the tables)

Even that you don't declare common fields to different models, which is good, you still have several tables with
where a lot of columns are the same. Sometimes there are more common columns than different.

You can't query them by their parent class. In django you can query them only separately. If you have some connections,
let's say `member_id` in both tables of yours, you can join these tables, but with raw SQL only. For example you
have base class Product, and child classes Apple and Orange. In Django with abstract base classes inheritance you
cannot query all your products at once using Product. You either make a raw sql if you have some product_id in both 
tables, or query them from Django ORM separately, like Apple.objects.all() and Orange.objects.all().

So abstract base classes inheritance is mostly useful for creating mixins to add some common fields to other tables.

question id: 3f404352-e2df-4b15-9ce8-b169c555291d


### What's Multi-Table Inheritance (MTI) in Django?

Multi-table inheritance is where the superclass, as well as each subclass, map to their own database tables.
The shared fields are stored on the superclass table and the type-specific fields are stored on their respective 
tables. Each subclass table then has an extra column that contains the id of the corresponding row in the parent 
class table.

For example:
```python
from django.db import models

class Product(models.Model):
  part_number = models.CharField(max_length=25)
  price = models.CharField(max_length=25)

class Label(Product):
  dimensions = models.CharField(max_length=25)

class FaceMask(Product):
  COLOR_CHOICES = [
      ('Blue', 'Blue'),
      ('White', 'White')
  ]
  color = models.CharField(max_length=25, choices=COLOR_CHOICES)
```

Under the hood you get a table of your parent class with common fields. Also as many tables as you have child models, 
each one contains a column with pointers to id of parent table <table1_name_ptr_id> (one-to-one field).

https://dev.to/zachtylr21/model-inheritance-in-django-m0j

question id: 264d8a8e-a2f6-4972-a75d-3e1d17af6d65

### Advantages and downsides of MTI

Advantages:
- data is normalized
- proven-by-time solution
- you can share constraints for common columns (like `name` can be unique among all the children tables)
Downsides:
- a lot of JOINs
- difficult to deal with all children at once (you cannot select all of them at once in Django ORM, you need raw SQL
or special side packages like InheritanceManager)

question id: 24b2bdeb-1ec5-478e-bcec-0637e309c9e7


### What is Single Table Inheritance?

It's when you superclass as well as its subclasses share one table for each of them. So there can be several models
but only one table for all of them. All information are stored in the same table, and not common fields get null.

question id: baacf141-74d3-4bbe-97a7-21c924a1eed2


### When it is a good idea to use STI?

When you have only one different column for your child models or as few as possible. Like you have superclass of Product
and subclasses with different type of products. You can use STI since the only non-common field here would be type of 
a product (and when you really want different types of product appear as different table in Django)

question id: a4188c56-56ea-401a-b17b-403864c5e2fd

### How to implement STI in Django?

Using proxy models. 

```python
class LabelManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(product_type='Label')

class Label(Product):
  objects = LabelManager()

  class Meta:
    proxy = True

class FaceMaskManager(models.Manager):
  def get_queryset(self):
    return super().get_queryset().filter(product_type='Face Mask')

class FaceMask(Product):
  objects = FaceMaskManager()

  class Meta:
    proxy = True
```

https://docs.djangoproject.com/en/3.1/topics/db/models/#proxy-models
https://www.benlopatin.com/using-django-proxy-models/
https://dev.to/zachtylr21/model-inheritance-in-django-m0j

question: 12f77b27-8d02-4c41-a165-570618dcbdbe

### Pluses and minuses of Single Table Inheritance

advantages:
- easy to fetch all the data in one fell swoop, hence to sort or whatever
downsides
- data is not normalized
- a lot of nullable columns
- high coupling

question id: efe49687-87cc-4e09-a274-58bdd29431d0

### What proxy models are and what are they for?

A proxy model is a subclass of a database-table defining model. Typically creating a subclass of a model results in a 
new database table with a reference back to the original model’s table - multi-table inheritance. A proxy model doesn’t 
get its own database table. Sometimes, however, you only want to change the Python behavior of a model – perhaps
 to change the default manager, or add a new method.

This is what proxy model inheritance is for: creating a proxy for the original model. You can create, delete and 
update instances of the proxy model and all the data will be saved as if you were using the original (non-proxied) model. 
The difference is that you can change things like the default model ordering or the default manager in the proxy, 
without having to alter the original.

https://docs.djangoproject.com/en/3.1/topics/db/models/#proxy-models
https://www.benlopatin.com/using-django-proxy-models/
https://dev.to/zachtylr21/model-inheritance-in-django-m0j

question id: 8adc6aad-6954-44d1-8ad6-51863e4e70ac


### When do we need multiple inheritance in Django?

Usually for mixins

question id: b8d2e57a-a02a-43e7-a868-14aa69d552f9




