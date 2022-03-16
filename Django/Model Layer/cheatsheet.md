### Create and save a row within Task table with id = id and status=status

```python
task = Task(id=some_id, status=status)
task.save()
```
To create and save an object in a single step, use the `create()` method:

```python
task = Task.objects.create(id=some_id, status=status)
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#creating-objects

question id: eb76dd57-7bff-4a12-be32-a0b1a977594c


### What the difference between `SomeModelName()` vs `SomeModelName.objects.create()` in Django?

The first one doesn't save a new object to the database immediately, you still have to call '.save()'
on it. The second one saves immediately.

question id: 27ca6160-1a0d-423f-a0df-8b8bbf3f0975


### Get row from Task table by id
```python
task = Task.objects.filter(id=1).first()
if not task:
    return
```

It is better to user `filter().first()` than `get()` because former returns None if nothing is found and the latter 
raises an exception

question id: e37968e1-a307-462e-877a-3c867a741b38


### Delete several rows by a list of IDs:
```python
Task.objects.filter(id__in=[1, 3, 4]).delete()
```

question id: 97c87d41-9510-4a86-8dce-4e74e93dd674

### Create a related object, for example a new Entry for a Blog
```python
b = Blog.objects.filter(id=1).first()
if not b:
    return
b.entry_set.create(some_arg=some_arg)
```
No need to call `e.save()` at this point -- it's already been saved.
 
question id 100fecd4-89e7-4012-9545-a29c68db1e66


## Related manager

A “related manager” is a manager used in a one-to-many or many-to-many related context. This happens in two cases:

- The “other side” of a ForeignKey relation. That is:
```python
from django.db import models

class Reporter(models.Model):
    # pass

class Article(models.Model):
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

```
    
    In the above example, the methods below will be available on the manager ```reporter.article_set```.

- Both sides of a ManyToManyField relation:
```python
class Topping(models.Model):
  # pass

class Pizza(models.Model):
  toppings = models.ManyToManyField(Topping)
```
  In this example, the methods below will be available both on `topping.pizza_set` and on `pizza.toppings`.
  


### How to associate an article to Reporter object?

Let's take these model as an example:
```python
    from django.db import models
    
    class Reporter(models.Model):
        # pass
    
    class Article(models.Model):
        reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
```

Answer:
```python
reporter = Reporter.objects.filter(id=1).first()
if not reporter:
    return
article = Article.objects.filter(id=1).first()
if not article:
    return
reporter.article_set.add(article)
```

question id: 6c7fae5d-b039-4d62-9cea-891e090f1a39

### How to create an article object and associate it with Reporter at the same time? 

Let's take these models as an example:
```python
    from django.db import models
    
    class Reporter(models.Model):
        # pass
    
    class Article(models.Model):
        reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
```

Answer:

```python
reporter = Reporter.objects.filter(id=1).first()
if not reporter:
    return
reporter.article_set.create(title="whatever")
```

Note: No need to call e.save() at this point -- it's already been saved.

question id: 4666b3c4-5487-45cc-881c-c5ddce602a51

### How to remove all articles from related Reporter object?
Let's take these model as an example:
```python
    from django.db import models
    
    class Reporter(models.Model):
        # pass
    
    class Article(models.Model):
        reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
```

Answer:

```python
reporter = Reporter.objects.filter(id=1).first()
if not reporter:
    return
reporter.article_set.clear()
```

question id: d7a13242-b281-45ef-b484-046a451ad637


### How to replace a set of articles related to a Reporter object?
```python
    from django.db import models
    
    class Reporter(models.Model):
        # pass
    
    class Article(models.Model):
        reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
    
```

Answer:
```python
reporter = Reporter.objects.filter(id=1).first()
if not reporter:
    return
new_list = [art1, art2, art3]
reporter.article_set.set(new_list)
```

This method accepts a clear argument to control how to perform the operation. If False (the default), 
the elements missing from the new set are removed using remove() and only the new ones are added (and django removes only
objects that are not in the list of new objects). If clear=True, django removes every old object and only than adds new ones.

Note that add(), create(), remove(), clear(), and set() all apply database changes immediately for all types of 
related fields. In other words, there is no need to call save() on either end of the relationship.


https://github.com/django/django/blob/0b655a4bf81f640d3e664f398e635943d4fb7812/django/db/models/fields/related_descriptors.py#L731

question id: 277d27c5-738d-4c60-a45a-b2a6e5eb6a39


### How to change last name of a reporter? 

```python
reporter = Reporter.objects.fitler(id=1).first()
# your code here
```

answer

```python
# having
reporter = Reporter.objects.fitler(id=1).first()

# one of options is:
reporter.last_name = "Smith"
reporter.save()
# but it will send to the database all fields, which is a bit taxing, and if you update just one field, 
# does not make sense

# the other options is to save specific fields like this
reporter.save(update_fields=['last_name'])

# and another options is to update necessary fields right away like
Reporter.objects.filter(id=1).update(last_name="Smith")
# It doesn't even load the whole reporter object in memory, although there is a drawback to: 
# does not call any save() methods on your models (maybe you have your custom ones - it won't be called too), nor does 
# it emit the pre_save or post_save signals (which are a consequence of calling Model.save()
```

https://docs.djangoproject.com/en/3.1/ref/models/instances/#updating-attributes-based-on-existing-fields
https://docs.djangoproject.com/en/3.1/ref/models/querysets/#update

question id: da3e1642-b978-41e9-885b-8b4f057df34f


### How to get list of ids of reportes with the last name Smith?

```python
smiths_ids = list(Reporter.objects.filter(last_name="Smith").values_list('id', flat='True'))
[1, 3, 34, ...]
```

https://stackoverflow.com/questions/37140426/does-django-queryset-values-list-return-a-list-object

question id: 1e697b74-5941-4b3a-9ecf-45995e8a7a11


# How to check that there is a reporter with id 999 in the database?

```python
Reporter.objects.filter(id=999).exists()
```

https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.exists

question id: b3a01773-a1aa-4805-b344-aeb95d258eab


### How does `__in` lookup filter work?

It basically means get all the objects where id of this object is in list that you pass to __in
For example
```python
User.objects.filter(mentor__id__in=[1,2,3])
```
will return you all the users who have mentee with id 1 OR 2 OR 3.

it translates to 
```sql
SELECT users WHERE mentor_id IN (1, 2, 3)
```

It works the same even if your field not mentor, but mentorS for example.

question id: 65db38ad-717d-4d78-bdca-8557c7ad80c4


### How is this django code translated into SQL?

```python
User.objects.filter(mentor__id__in=[1,2,3])
```

answer
```sql
SELECT users WHERE mentor_id IN (1, 2, 3)
```

question id: c6ca9fef-437e-4ef1-a761-93ef93b52785


### Explain what means this Django code
```python
User.objects.filter(mentor__id__in=[1,2,3])
```

answer
Give me all users whose field mentor_id equal to one of the items in the list. Like

```python
from django.db import models

User.objects.filter(models.Q(mentor__id=1) | models.Q(mentor__id=2) | models.Q(mentor__id=3))
```

question id: 7d264d92-551d-4aea-a452-6ee2d653fe6b


### What's `only()` method of a queryset for?

It allows you to select only specific fields like
```sql
SELECT first_name FROM users
```

But in Django:
```python
users = User.objects.all().only("first_name")
```

https://docs.djangoproject.com/en/3.1/ref/models/querysets/#only
 
question id: 190f2fbd-8371-48b2-b969-68ea6f7eea40



### How to load only one field from the database?

Something like
```sql
SELECT first_name FROM users
```
but in Django

answer:
```python
users = User.objects.all().only("first_name")
```

https://docs.djangoproject.com/en/3.1/ref/models/querysets/#only
 
question id: 190f2fbd-8371-48b2-b969-68ea6f7eea40