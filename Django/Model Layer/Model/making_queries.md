https://docs.djangoproject.com/en/3.1/topics/db/queries/

### Reference models

```python
from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
```

### How many database hits are here and where are they?

```python
q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
print(q)
```

answer

only one, in print() function

question id: fd2c6fbe-254b-4fe9-b354-3288411c6250


### Having Entry model, how to retrieve first 5 objects?

answer
```python
Entry.objects.all()[:5]
```

question id: 41f93971-a7e1-4dee-b317-eb283c40b7c4


### Determine how many entries were made in each Blog

Having Blog and Entry models like here: https://docs.djangoproject.com/en/3.1/topics/db/queries/

You want to make a queryset with all Blogs, where every row also contains how many entries were made in each Blog

answer
```python
q = Blog.objects.annotate(number_of_entries=Count('entry'))
# The number of entries on the first blog, using the name provided
q[0].number_of_entries # 42
```
question id: 260ea8da-c48d-4ef0-a33f-fe99d08266cb


### Having Entry model, how to retrieve the sixth through tenth objects?

answer

```python
Entry.objects.all()[5:10]
```

question id: f446e8b1-0ce9-4a0b-a412-31437c248ead


### Can you get the last object of Entry model like this?

```python
Entry.objects.all()[-1]
```

answer:
Nope. Negative index is not supported.

question id: e79fce6a-ff43-4169-8c10-b3822bfa73e7


### Having Entry model with pub_date field, find all entries published before the 1st of January, 2006.

```python
Entry.objects.filter(pub_date__lte='2006-01-01')
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups

question id: 052bab7d-fc0d-4a6e-8aa2-693b7ebafaa6


### Having `Entry` model with `headline` field find article(s) with headline that completely matches 'Cat bites dog'

```python
Entry.objects.filter(headline__exact='Cat bites dog')
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups

question id: c4831a91-6e08-4672-aefe-66aecf99e7eb


### Having `Blog` model with `name` field find article(s) with name that exactly matches "Beatles Blog", "beatles blog", or even "BeAtlES blOG" regardless of its case

```python
Blog.objects.filter(name__iexact="beatles blog").all()
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups
question id: 01d6e95d-d815-497c-a171-7007d91e77c8


### What are Django lookups for >, >=, <, <= ?

answer
__gt, __gte, __lt, __lte
For example
```python
Entry.objects.filter(pub_date__lte='2006-01-01')
```
will return all the Entries that were published before the 1st of January, 2006

question id: 4672de63-79a2-430f-abf8-fc6ac3355a62

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#gt




### Having `Entry` model with `headline` field find all the articles with headline that have 'Lennon' in it

```python
Entry.objects.get(headline__contains='Lennon')
```

Note that for case-insensitive match there is 'icontains' lookup

https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups

question id: 9e6bebe0-0866-4667-a2ef-31a51fad75b1


### Having `Place` model with `name` field find all the places where the name begins with 'Demon' and finishes with 'Dogs'

```python
Place.objects.filter(name__startswith='Demon', name__endswith='Dogs')
```

Note that there is 'istartswith' and 'iendswith' for case-insensitive lookup

https://docs.djangoproject.com/en/3.1/topics/db/queries/#field-lookups

question id: 5b2434e3-d956-45d7-b216-d3799efa9ef0


### Having Car model with fields `manufacturer` and `colour` get all cars that are Mazda's AND of a red colour.

```python
Car.objects.filter(manufacturer='Mazda', colour='Red')
```

question id: df52e5be-2431-4867-a17e-c81b4ef4edc0


### Is the following filtering by two keywords are represent AND or OR logic?

```python
Car.objects.filter(manufacturer='Mazda', colour='Red')
```

answer

It's AND logic. Cars should be both Mazda and red at the same time.

question id: 09ceba5b-94e5-4313-951b-789fd6cb4e85


### Having Car model with fields `manufacturer` and `colour` get all cars that are Mazda's OR of a red colour.

```python
from django.db.models import Q

Car.objects.fitler(Q(manufacturer='Mazda') | Q(color='red'))
```

question id: e7258bf9-d82b-43ab-92fa-6efca9b62a58


### How to implement dynamic filter with OR logic? 

For example, how to filter YourObject by these keywords: `{'size': 10, 'colour': 'red', 'weight': 1}`

```python
from functools import reduce
from operator import or_
from django.db.models import Q

args = {'size': 10, 'colour': 'red', 'weight': 1}
query = reduce(or_, (Q(key=value) for key, value in args.items()))
YourObject.objects.filter(query)
```

question id: 218e17a8-58b6-477f-aff9-24007423a8ad


### What are the logic of this query? AND or OR?

```python
SomeModel.objects.filter(some_field='foo').filter(another_field='baz')
```

answer: 
It's an AND logic. The result should contain blogs with `foo` AND `baz`.

question id: 24cbd7f5-a3a7-4ab0-b493-28e55f548550



### What are the logic of this query? AND or OR?

```python
SomeModel.objects.filter(foreign_table__field_in_foreign_table='foo').filter(foreign_table__another_field_in_foreign_table='baz')
```

answer:
 
It's OR logic. The result can contain blogs with `foo` OR `baz`.

https://docs.djangoproject.com/en/3.1/topics/db/queries/#spanning-multi-valued-relationships
https://hacksoft.io/django-filter-chaining/

question id: 239e2a7c-0f0c-4446-b759-b6066995639a


### What is the difference between these two queries?

```python
Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3), headline='Hello')  # 1

Entry.objects.exclude(pub_date__gt=datetime.date(2005, 1, 3)).exclude(headline='Hello')  # 2
```

answer
- the first one returns  excludes all entries whose pub_date is later than 2005-1-3 AND whose 
headline is “Hello”
- the second one excludes all entries whose pub_date is later than 2005-1-3 OR whose headline
is “Hello”
  
question id: 17e2ca9a-78c4-4190-9b6b-d2254df04606


### How to exclude blogs that contain entries with “Lennon” in the headline or entries published in 2008?

Having Blog model and Entry model like in here:
https://docs.djangoproject.com/en/3.1/topics/db/queries/#making-queries

answer
```python
Blog.objects.exclude(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)
```

Note: inside `filter()` this will be AND logic, but with `exclude()` it's OR logic. 

question: 41c3aef7-c53b-44f6-b49e-28547801a0f8


### What are the logic of this query? AND or OR?

```python
Blog.objects.exclude(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)
```

answer:
It's an OR logic. 
Note: inside `filter()` this will be AND logic, but with `exclude()` it's OR logic.

https://docs.djangoproject.com/en/3.1/topics/db/queries/#spanning-multi-valued-relationships

question id: 9121a7cd-3821-4693-94b9-0278676e00f3

### How to select all blogs that do not contain entries published with “Lennon” that were published in 2008?

Having Blog model and Entry model like in here:
https://docs.djangoproject.com/en/3.1/topics/db/queries/#making-queries

answer:

```python
Blog.objects.exclude(
    entry__in=Entry.objects.filter(
        headline__contains='Lennon',
        pub_date__year=2008,
    ),
)
```
https://docs.djangoproject.com/en/3.1/topics/db/queries/#spanning-multi-valued-relationships

question id: 3784a434-e8a7-4e0c-9224-73a6f422c7d3


### How to find all the entries where number of likes is more than number of comments?

You have an `Entry` model that have fields `number_of_comments` and `number_of_likes`. 

answer: 

```python
from django.db import models

Entry.objects.filter(number_of_likes__gt=models.F('number_of_comments'))
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#filters-can-reference-fields-on-the-model

question id: 26273766-a9b0-428a-be55-9f31d286a597


### How to find all entries where `rating` is less than sum of `number_of_fields` and `number_of_likes`?

You have an `Entry` model that have fields  rating`, `number_of_comments` and `number_of_likes`.

```python
from django.db import models

Entry.objects.filter(rating__lt=models.F('number_of_fields') + models.F("number_of_likes"))
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#filters-can-reference-fields-on-the-model

question id: b086b2d0-5296-4b8f-a417-6f3d51961154


### How to select all the entries where author's name is the same as the name of the blog?

Having Blog, Author and Entry models like in here:
https://docs.djangoproject.com/en/3.1/topics/db/queries/#making-queries

```python
from django.db import models

Entry.objects.filter(authors__name=models.F('blog__name'))
```

question id: 802476bb-c2f5-4544-974c-8b3e4ddd14e0

### Why this

```python
queryset = Entry.objects.all()
print([p.headline for p in queryset]) # Evaluate the query set.
print([p.pub_date for p in queryset]) 
```

is better than this?

```python
print([e.headline for e in Entry.objects.all()])
print([e.pub_date for e in Entry.objects.all()])
```

answer:

Because in the second case you make calls to your database twice (because you create two querysets), while in the 
first case you use cache that is stored in the queryset

https://docs.djangoproject.com/en/3.1/topics/db/queries/#caching-and-querysets

question id: 17a6caf7-2304-4d71-a752-d3bc085aab17


### When queryset caches items from a database?

answer

Only when a queryset gets iterated over.

For example:
```python
queryset = Entry.objects.all()
print(queryset[5]) # Queries the database
print(queryset[5]) # Queries the database again
```

but

```python
queryset = Entry.objects.all()
[entry for entry in queryset] # Queries the database
print(queryset[5]) # Uses cache
print(queryset[5]) # Uses cache
```

https://docs.djangoproject.com/en/3.1/topics/db/queries/#when-querysets-are-not-cached

question id: b56b4c47-a413-4f60-a5e4-4600fee2c110


### Querying JSONField

For example you have a model like this

```python
from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name
```

and some objects/rows based on this model like these
```python
Dog.objects.create(name='Rufus', data={
    'breed': 'labrador',
    'owner': {
        'name': 'Bob',
        'other_pets': [{
            'name': 'Fishy',
        }],
    },
})  # <Dog: Rufus>
Dog.objects.create(name='Meg', data={'breed': 'collie', 'owner': None})  # <Dog: Meg>
Dog.objects.filter(data__breed='collie')  # <QuerySet [<Dog: Meg>]>
``` 

filter all the rows where a name of first in a row of other pets of the owner of the dog is 'Fishy'

answer 
```python
Dog.objects.filter(data__owner__other_pets__0__name='Fishy'
```

question id: 2eec92a3-ffda-4433-a319-af3d9b9f04f9


## Complex lookups with Q objects

### What does this statement yield? 

```python
from django.db.models import Q

Q(question__startswith='Who') | Q(question__startswith='What')
```

answer:
It yields a single Q object that represents the “OR” of two "question__startswith" queries

question id: 752501a5-80c2-4883-a803-48a5425bc571


### What is the equivalent of this statement in SQL?

```python
from django.db.models import Q

Q(question__startswith='Who') | Q(question__startswith='What')
```

answer:
```sql
WHERE question LIKE 'Who%' OR question LIKE 'What%'
```

question id: da7a22e7-1e4d-4e72-badb-857d9e557912


### Having Car model with fields `manufacturer` and `colour` get all cars that are Mazda's OR NOT of a red colour.

```python
from django.db.models import Q

Car.objects.fitler(Q(manufacturer='Mazda') | ~Q(color='red'))
```

question id: 87e3779e-59fd-4278-ab56-7f6f687a29c5


### How does this query translates to SQL?

```python
Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)
```

answer:
```sql
SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```

question id: 51c1525e-c07f-4fff-a55e-a03e4930a34d


### How does this SQL query translate to Django query?

```sql
SELECT * from polls WHERE question LIKE 'Who%'
    AND (pub_date = '2005-05-02' OR pub_date = '2005-05-06')
```

answer:

```python
Poll.objects.get(
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
    question__startswith='Who',
)
```

question id: 26658952-e01e-403e-98fc-5d4db227fec0


### How does Django compare two objects? For example:

```python
from django.db import models

class Person(models.Model):
    name = ...
    # a lot of other fields

vasya = Person.objects.filter(name='Vasya')
petya = Person.objects.filter(name='Person')

if vasya == petya:  
    # how does Django compare this two objects?
```

answer 

Django just compares primary keys of objects, not any other fields.

question id: 779897ac-ad9d-4138-94a5-37dcca7cd1ac


### How to delete all rows in a table via Django ORM?

```python
SomeModel.objects.all().delete()
```

question_id: 5515b954-2a0a-4183-8283-c464cbb30bda


### How to delete all Entry objects with a pub_date year of 2005?

```python
Entry.objects.filter(pub_date='2005').delete()
```

question id: 2468de15-59bc-4aeb-980c-4752842e2ef2

### In which case you need to iterate over your queryset and delete every item individually? And why?

When you have a custom `delete()` method. Because Django will try to use SQL query to delete all items at once and can
completely skip your custom `delete()` method.

question id: 4fa3b60a-71d2-4d89-8cbb-9d654bab3717


### You have an `Article` model with `headline` field. How to update all the headlines with pub_date in 2007?

```python
Article.objects.filter(pub_date__year=2007).update(headline='Everything is the same')
```

Beware that `update()` doesn’t run any `save()` methods on your models, or emit the `pre_save` or `post_save` signals 
(which are a consequence of calling `save()`), or honor the auto_now field option.

question id: ec42aa91-c212-4e11-a2b5-626e970e8962


### How to connect all articles to one blog?

```python
b = Blog.objects.filter(id=1).first()
if not b:
    return

Article.objects.all().update(blog=b)
``` 

question id: b6bfea87-7fde-471e-a613-a0887529c935


### Increment `number_of_likes` by one on every article

```python
from django.db.models import F

Article.objects.all().update(number_of_likes=F('number_of_likes') + 1)
```

question id: abcb3b51-4e90-4fc8-94bf-bd53edf3ae10



