https://docs.djangoproject.com/en/3.2/ref/models/querysets/

### When QuerySets are evaluated?

Internally, a QuerySet can be constructed, filtered, sliced, and generally passed around without 
actually hitting the database. No database activity actually occurs until you do something to 
evaluate the queryset.

You can evaluate a QuerySet in the following ways:
- iteration 
- slicing
- Pickling/Caching
- repr()
- len()
- list()
- bool()

question id: f941a79e-b1b4-4a66-8782-9d4540431f01


### How to order a queryset? 

For example, you have this queryset, how to order it by in descending order by 'pub_date' and 
in ascending order by 'headline'?

```python
Entry.objects.filter(pub_date__year=2005)
```

answer
```python
Entry.objects.filter(pub_date__year=2005).order_by('-pub_date', 'headline')
```

question id: d1d904ea-f538-4265-bfe6-b2627c7980d8


### How to order a QuerySet in random order? 

```python
Entry.objects.order_by('?')
```

question id: abae66b6-b532-43ed-95db-336a9ae45d55


### How to order a QuerySet by a field of related model?

For example, you have Blog model and Entry model as one-to-many. You want to get all entries 
ordered by their blog names. How would you do that?

answer

```python
Entry.objects.order_by("blog__name").all()
```

question id: 85d771af-2670-4181-b676-ebdb7ed2d015


### What would happen if you try to order QuerySet by a field that is a relation to another model like this:

```python
Entry.objects.order_by('blog')
```

You have Blog model and Entry model as one-to-many.

answer:
Django will use the default ordering on the related model, or order by the related model’s 
primary key if there is no Meta.ordering specified.

For example, if the Blog model has no default ordering specified:
```python
Entry.objects.order_by('blog')

# ...is identical to:

Entry.objects.order_by('blog__id')
```

If Blog had ordering = ['name'], then the first queryset would be identical to:

```python
Entry.objects.order_by('blog__name')
```

question id: ef939bf3-3695-41f6-9d19-56f063b96df6


### How to reset any ordering of a QuerySet, even default one?

answer
If you don’t want any ordering to be applied to a query, not even the default ordering, 
call order_by() with no parameters.

question_id: 645600d8-c936-443d-b39f-b3a548001e94


### What does applying of order_by() to a QuerySet means? When there are no arguments passed to 
order_by()

answer
If you don’t want any ordering to be applied to a query, not even the default ordering, 
call order_by() with no parameters.

question id: c78ec713-2fbb-4a81-8ada-5ac434803b99


### What will be the ordering of this QuerySet?

```python
Entry.objects.order_by('headline').order_by('pub_date')
```

answer
The results will be ordered only by pub_date in ascending order, because each order_by() call will 
clear any previous ordering.

question id: 3f2f4524-d23e-4a15-b420-46345c649049


### How to reverse an order of items in a QuerySet?

answer
You can use reverse() method. 

note that reverse() should generally only be called on a QuerySet which has a defined ordering 
(e.g., when querying against a model which defines a default ordering, or when using order_by()).
If no such ordering is defined for a given QuerySet, calling reverse() on it has no real effect 
(the ordering was undefined prior to calling reverse(), and will remain undefined afterward).

question id: 9b8ba281-dc32-4fc2-88b1-1b57a640727d


### How to eliminate duplicates rows from a QuerySet?

answer
Use .distinct() to eliminate duplicate rows from the query results.

question id: 66819337-01ce-444a-be06-a897641a4511


### Is it possible to return rows without duplicates but in one or several spefified fields?

answer
Yes, but only when your db is PostgreSQL. You can pass to .distinct() names of your fields as 
strings. Beware that in this case you also have to use .order_by() and specify the same fields in
the same order.

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#distinct

question id: 14ce8b26-ed1b-4e8f-b753-962e143b5372


### How to return rows as list of dictionaries with specified fields instead of QuerySet?

answer
Use .values()

```python
# This list contains a Blog object.
Blog.objects.filter(name__startswith='Beatles')
<QuerySet [<Blog: Beatles Blog>]>

# This list contains a dictionary.
Blog.objects.filter(name__startswith='Beatles').values()
<QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
```

You can specify one or several fields as argument for .values()
```python
Blog.objects.values()
<QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
Blog.objects.values('id', 'name')
<QuerySet [{'id': 1, 'name': 'Beatles Blog'}]>
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#values

question id: 33cb3e48-f3cf-4b83-abd4-08a70af0cc8c


### What is the difference? 

between
```python
# between
Blog.objects.filter(name__startswith='Beatles')
# and 
Blog.objects.filter(name__startswith='Beatles').values()
```
answer
```python
# This list contains a Blog object.
Blog.objects.filter(name__startswith='Beatles')
<QuerySet [<Blog: Beatles Blog>]>

# This list contains a dictionary.
Blog.objects.filter(name__startswith='Beatles').values()
<QuerySet [{'id': 1, 'name': 'Beatles Blog', 'tagline': 'All the latest Beatles news.'}]>
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#values

question id: 8cce6ef2-204a-4090-adcc-678d829ec972


### How to get a list of all articles' headlines? As a list of strings, not as QuerySet 

answer
```python
headlines = Article.objects.values_list('headline', flat=True).order_by('headline')
print(headlines)  # <QuerySet ["What happened to Bill Clinton?", "10 best stories of this week", "What could have gone wrong?"]>
print(list(headlines))  # ["What happened to Bill Clinton?", "10 best stories of this week", "What could have gone wrong?"]
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#values-list

question id: e4c47512-a1a0-455b-8c95-02b21c8f7cf6


### What are .values_list() method of QuerySet for?

answer
With it you can get your rows as a list of tuples instead of objects. Like this:
```python
Entry.objects.values_list('id', 'headline')
<QuerySet [(1, 'First entry'), ...]>
```

or even just a list of values of one field, like this:
```python
ids = Entry.objects.values_list('id', flat=True).order_by('id')
print(ids)  # <QuerySet [1, 2, 3, ...]>
print(list(ids))  # [1, 2, 3, ...]
```

question id: 89952299-c026-49c6-9a08-2829867171bd


### Does it make sence to use only() with values() or values_list()? 

answer

No. If you speficy some particular fields in values() or values_list(),
django will SELECT only these fields from your table. 

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#values

question id: 2072ba39-5229-41ee-8749-b5c9620ca0ee


### How to merge two or more QuerySets into one discarding duplicate rows?

```pythoh
q1 = MyModel.objects.all()  # 'A','B', 'C','D', 'E'
q2 = MyModel.objects.filter(name__in=('A','B'))
q3 = MyModel.objects.filter(name__in=('C','D'))
```

For example, you want to get rows of q2 and q3. How would you do this? 

answer
Use .union()

```python
q4 = q2.union(q3)
print(q4)
<QuerySet [<MyModel: A>, <MyModel: B>, <MyModel: C>, <MyModel: D>]>
```

You can even pass to .union() several QuerySets. 

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#union
https://technowhisp.com/django-orm-union-intersection-and-difference/

question id: e86915d5-cb01-4ee7-935f-08eb255bafc6


### How to get a QuerySet that contains only rows that present in two (or more) other QuerySets?

```pythoh
q1 = MyModel.objects.all()  # 'A','B', 'C','D', 'E'
q2 = MyModel.objects.filter(name__in=('A','B'))
q3 = MyModel.objects.filter(name__in=('C','D'))
```

For example, you want to get rows that present in q1 and q2. How would you do this?

answer

Use .intersection()

```python
q7 = q1.intersection(q2)
print(q7)
<QuerySet [<MyModel: A>, <MyModel: B>]>
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#intersection
https://technowhisp.com/django-orm-union-intersection-and-difference/

question id: 7e5ab793-b015-4bba-bf16-a3eb3d714adf


### How to get a QuerySet with rows that present in one QuerySet and do not present in another (or others)?

In other words, how to get a QuerySet with unique rows for one QuerySet?

```pythoh
q1 = MyModel.objects.all()  # 'A','B', 'C','D', 'E'
q2 = MyModel.objects.filter(name__in=('A','B'))
q3 = MyModel.objects.filter(name__in=('C','D'))
```
For example, you want to get all the rows that present in q1 and do not present in q2

answer
use .difference()

```python
q10 = q1.difference(q2) #q1 - q2
print(q10)
<QuerySet [<MyModel: C>, <MyModel: D>, <MyModel: E>]>
```

You can even pass to .difference() several QuerySets. 

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#difference
https://technowhisp.com/django-orm-union-intersection-and-difference/

question id: 0f8240da-6e15-4f9e-98af-2d7091a44dc1


### What is .select_related() for?

answer
.select_related() is a method that makes Django QuerySet select not only field of one object as in, 
for example, Reporter.objects.all(), but also select related objects in the same SELECT statement.
So Django under the hood join related tables and returns all in one QuerySet.

Check out the example
Here’s standard lookup:
```python
# Hits the database.
e = Entry.objects.get(id=5)

# Hits the database again to get the related Blog object.
b = e.blog
```
And here’s select_related lookup:
```python
# Hits the database.
e = Entry.objects.select_related('blog').get(id=5)

# Doesn't hit the database, because e.blog has been prepopulated
# in the previous query.
b = e.blog
```

You can refer to any ForeignKey or OneToOneField relation in the list of fields passed to 
.select_related().

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#select-related

question id: 5092d8e8-b99e-4cf2-a6af-b333af927a9c


### How to select related object of related objects?

For example, you have three related objects like this:
```python
from django.db import models

class City(models.Model):
    # ...
    pass

class Person(models.Model):
    # ...
    hometown = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

class Book(models.Model):
    # ...
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
```

And you want to select a Book with id #4, but with the book you want to select book's author info
and specifically his home town. How would you do this in Django?

answer
You can follow foreign keys in a similar way to querying them. So this call 
 will cache the related Person and the related City:
```python
Book.objects.select_related('author__hometown').get(id=4)
```

There is the difference between using .select_related() and not using:

```python
# Hits the database with joins to the author and hometown tables.
b = Book.objects.select_related('author__hometown').get(id=4)
p = b.author         # Doesn't hit the database.
c = p.hometown       # Doesn't hit the database.

# Without select_related()...
b = Book.objects.get(id=4)  # Hits the database.
p = b.author         # Hits the database.
c = p.hometown       # Hits the database.
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#select-related

question id: d96cb0ee-7b72-4edf-802a-68d3bddfb8d5


### What is .prefetch_related() for?

answer
.prefetch_related() methods makes Django select related many-to-many and many-to-one objects. It 
does a separate database call for every related object and 'join' the result in Python (instead
of using databases joins).

For example, suppose you have these models:
```python
from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            ", ".join(topping.name for topping in self.toppings.all()),
        )
```

and run:
```python
>>> Pizza.objects.all()
["Hawaiian (ham, pineapple)", "Seafood (prawns, smoked salmon)"...
```

The problem with this is that every time Pizza.__str__() asks for self.toppings.all() it has to
query the database, so Pizza.objects.all() will run a query on the Toppings table for every item 
in the Pizza QuerySet.

We can reduce to just two queries using prefetch_related:
```python
Pizza.objects.all().prefetch_related('toppings')
```

This implies a self.toppings.all() for each Pizza; now each time self.toppings.all() is called, 
instead of having to go to the database for the items, it will find them in a prefetched QuerySet 
cache that was populated in a single query.

That is, all the relevant toppings will have been fetched in a single query, and used to make 
QuerySets that have a pre-filled cache of the relevant results; these QuerySets are then used in 
the self.toppings.all() calls.

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-related

question id: 1bc4075b-32ef-40bc-82a5-8a7417836d71


### What's wrong with this?

```python
pizzas = Pizza.objects.prefetch_related('toppings')
[list(pizza.toppings.filter(spicy=True)) for pizza in pizzas]
```

The fact that pizza.toppings.all() has been prefetched will not help you. 
The prefetch_related('toppings') implied pizza.toppings.all(), but pizza.toppings.filter() is a
new and different query. The prefetched cache can’t help here; in fact it hurts performance, 
since you have done a database query that you haven’t used. So use this feature with caution!

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-related

question id: 52d105ba-e7c3-44a9-b6db-3a78e123683f


### What does this mean? 

```python
Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')
```

answer
You are preselecting best_pizza object (select_related because it's related via Foreign key) and 
also preselecting toppings which is many-to-many with pizza. You could do it at one fell swoop with

```python
Restaurant.objects.prefetch_related('best_pizza__toppings')
```

...but that would be 3 calls to the database since .prefetch_related() makes a separate database
call for every related object, when .select_related() selects everything in one SQL query.

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#prefetch-related

question id: e10e1eb8-aea7-41d8-80f5-c909cac29bba


### What is the difference between .select_related() and .prefetch_related()?

.prefetch_related() has a similar purpose to .select_related(), in that both are designed to 
stop the deluge of database queries that is caused by accessing related objects, but the 
strategy is quite different.

.select_related() works by joining related tables via SQL and including the fields of the 
related object in the SELECT statement. For this reason, .select_related() gets all the related 
objects one database query. However, to avoid the much larger result set that would result 
from joining across a ‘many’ relationship, .select_related() is limited to single-valued 
relationships - foreign key and one-to-one.

.prefetch_related(), on the other hand, does a separate lookup for each relationship, and does the 
‘joining’ in Python. This allows it to prefetch many-to-many and many-to-one objects, which cannot 
be done using .select_related(), in addition to the foreign key and one-to-one relationships that are 
supported by select_related. 

question id: 59b29f8d-fbb4-44fd-b076-88b5dc7ae13b


### How to not load some field in a QuerySet? 

For example, you have a column with text where can be megabytes of text, but you don't want to
load this column in one of your QuerySets. How to avoid loading this field?

answer
use .defer() like this:
```python
Post.objects.defer('text').all()
```

You can choose several fields as well.
If you, instead, need to load only one field field, use .only()

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#defer

question id: 1435f37d-90c9-4633-abfb-3271e75a9034


### What is .defer() for? 

answer
To avoid loading (SELECTing) given column(s)

Use...
```python
Post.objects.defer('text').all()
```
...if you want to load all fields of Post but text. Keep in mind that it will be loaded anyway
if you refer to it explicitly.

question id: b6e94452-2fd8-4ecb-8b34-9f215ac052f1


### How to fetch only specific column(s) using QuerySet?

answer
Use .only() like this:
```python
Person.objects.only("name")  # will load only name, other field will be loaded on demand - when you reference them
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.only

question id: f9573e44-db27-4333-8e62-14605bc49e31


### What's .only() for?

answer
It allow you to specify what fields to load immediately from a table

```python
Person.objects.only("name")  # will load only name, other field will be loaded on demand - when you reference them
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#django.db.models.query.QuerySet.only

question id: 19a5d575-42f0-4ae8-822b-ee87e2ec9e4b


### What is .get() for? 

answer
Returns exactly one object matching the given lookup parameters. It will raise an error if zero or more than one 
objects found

```python
Entry.objects.get(blog=blog, entry_number=1)
```

question id: af184056-aefb-4c27-8181-98beb04df82c


### How to bulk-create several objects?

```python
objs = Entry.objects.bulk_create(
 [
  Entry(headline='This is a test'), 
  Entry(headline='This is only a test')
  ]
)
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-create

question id: da2469e5-7f5f-4a28-b5b8-28727a39f5a0


### How to bulk-update several rows?

```python
articles = Article.objects.filter(...).all()

articles[0].title = "Whatever"
articles[1].title = "Who cares"
Article.objects.bulk_update(articles, ["title"])
```

Each model’s save() method isn’t called, and the pre_save and post_save signals aren’t sent.

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#bulk-update

question id: 0056a7ab-8d11-409e-986d-2853d7adbd20


### How to count rows?

answer
Use .count() on your QuerySet, for example like this:

```python
Blog.objects.filter(title__startswith='Sex').count()
```

or 

```python
sex_blogs = Blog.objects.filter(title__startswith='Sex').all()
len(sex_blogs)
```

The first one will not load the data, but will execute SELECT COUNT(*)
The second one will load data of the QuerySet during execution of len().
So choose wisely.

question id: ac7dea15-1d8b-4640-98b9-b595184adfb9


### How to count rows - with .count() or len()?

The first one will not load the data, but will execute SELECT COUNT(*)
The second one will load data of the QuerySet during execution of len().

Choose .count() if you are not going to load the data. Choose len() otherwise.

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#count

question id: 41de2691-6b96-4392-97bc-8f0f5c5a4c7e


### How to get a dict where key is a model field (e.g. name) and item is the row corresponding to this field?

answer
user .in_bulk()
```python
Blog.objects.in_bulk([1, 2])  # by id
{1: <Blog: Beatles Blog>, 2: <Blog: Cheddar Talk>

# or 

Blog.objects.distinct('name').in_bulk(field_name='name')
{'Beatles Blog': <Blog: Beatles Blog>, 
 'Cheddar Talk': <Blog: Cheddar Talk>, 
 'Django Weblog': <Blog: Django Weblog>}
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#in-bulk

question id: b02aaa6a-bf9d-4598-b6cd-2207d75fcc2a


### How to iterate over a QuerySet without caching values to memory?

For example, you want to iterate over a huge amount of data and you only need it once. So why should
you bother store it all in memory? But QuerySet's cache values on iteration. How to avoid it?

answer
use .iterator()
```python
star_set = Star.objects.all()

for star in star_set.iterator():
    print(star.name)
```
https://docs.djangoproject.com/en/3.2/ref/models/querysets/#iterator
https://blog.etianen.com/blog/2013/06/08/django-querysets/

question id: bc01f525-8b75-4cf2-9bf6-231790830c94


### How to find a row with the latest or earliest date in a given date field? 

For example, you have field `created_at` in your table. How to get the latest created row?
How to find the first one?

Use methods .latest() or .earliest(), for example:
```python
Entry.objects.latest('created_at')
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#latest

question id: 2531022d-5fee-42af-9a29-2da3b547d3de


### What is the equivalent of BETWEEN in Django ORM? 

answer 
__range

```python
Entry.objects.filter(id__range=(1, 10))
```
https://docs.djangoproject.com/en/3.2/ref/models/querysets/#range
question id: abf52259-d07c-4b1f-9dc3-39172255e806


### What if I have a timestamp(tz) field and want to filter by a part of it?

For example, filter all rows where `created_at` is bigger, smaller or equal to some second, hour,
week, date etc?

answer
Django ORM has special lookups for all this stuff:
date
year
iso_year
month
day
week
week_day
iso_week_day
quarter
time
hour
minute
second

examples: 
```python
Entry.objects.filter(pub_date__date=datetime.date(2005, 1, 1))
Entry.objects.filter(pub_date__year=2005)
Entry.objects.filter(pub_date__month__gte=6)
Entry.objects.filter(pub_date__day__gte=3)
Entry.objects.filter(pub_date__week__gte=32, pub_date__week__lte=38)
Entry.objects.filter(pub_date__week_day__gte=2)
Entry.objects.filter(pub_date__quarter=2)
Entry.objects.filter(pub_date__time=datetime.time(14, 30))
Event.objects.filter(timestamp__hour=23)
Event.objects.filter(timestamp__minute__gte=29)
Event.objects.filter(timestamp__second__gte=31)
```

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#date

question id: 67bea753-a5c6-4b9c-b585-09aedb6f0720


### What would be the equivalent in Django ORM?

```sql
SELECT blog WHERE pub_date IS NULL
```
answer
```python
Blog.objects.filter(pub_date__isnull=True)
```

question id: 8974fa16-d2e7-4c69-84dc-eb8dea3f03a2
