### What do you need to define many-to-one relationship?

You need to specify Foreign key in your 'many' side of relationship to 'one' side of relationship

If you have Reporter who can have multiple articles, you put Foreign Key in Article model that (key) points to 
your Reporter model. Like this:

```python
from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']
```

question id: 440105c1-32d5-483f-b7c5-ec53b84b60dd


### Create a new Article entry via Article model 

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

create an a new Article entry via Article model, tied to a existing reporter

```python
from datetime import date

reporter = Reporter.objects.filter(id=1).first()
if not reporter:
    return None

articles = Article.objects.create(headline='whatever', pud_date=date(2012, 1, 7), reporter=reporter)
```

question id: 0b764278-affa-41e2-b984-5a71b8a903f1


### How to update ForeignKey? In other words, how to set a reporter for already existing article?

```python
article = Entry.objects.get(id=1)
reporter = Reporter.objects.get(id=1)
# your code here
```

answer:
Updating a ForeignKey field works exactly the same way as saving a normal field – assign an object of the right type 
to the field in question

```python
article = Entry.objects.get(id=1)
reporter = Reporter.objects.get(id=1)

article.reporter = reporter
article.save()

# or
reporter.article_set.add(article)
```

question id: a222aa44-2e26-46d2-854d-e916c8e8cc04

### How to get a reporter (of Reporter model) via an article (of Article model)?

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

answer: 

```python
a.reporter  # <Reporter: John Smith>
```

question id: 71d487bc-d65c-4b0a-87b5-196c3f0283ac


### How to create an Article via Reporter object

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
new_article = r.article_set.create(headline="John's second story", pub_date=date(2005, 7, 29))
new_article  # <Article: John's second story>
new_article.reporter  # <Reporter: John Smith>
new_article.reporter.id  # 1
```

question id: 9e6637ce-0e33-4add-a95e-826ee1dcbfbd


### Change parent of an object

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
r = Reporter.objects.create(first_name='John', last_name='Smith', email='john@example.com')
r2 = Reporter.objects.create(first_name='Paul', last_name='Jones', email='paul@example.com')

new_article = Article.objects.create(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
new_article2 = Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17), reporter=r)


new_article.reporter  # <Reporter: John Smith>
new_article2.reporter  # <Reporter: John Smith>


# now both articles belong to the r reporter. How to connect new_article2 to the r2 reporter?
# your code here
```

answer


```python
r = Reporter.objects.create(first_name='John', last_name='Smith', email='john@example.com')
r2 = Reporter.objects.create(first_name='Paul', last_name='Jones', email='paul@example.com')

new_article = Article.objects.create(id=None, headline="This is a test", pub_date=date(2005, 7, 27), reporter=r)
new_article2 = Article.objects.create(headline="Paul's story", pub_date=date(2006, 1, 17), reporter=r)

new_article.reporter  # <Reporter: John Smith>
new_article2.reporter  # <Reporter: John Smith>

# there are two ways
r2.article_set.add(new_article2)
new_article2.reporter   # <Reporter: Paul Jones>

# or
new_article2.reporter = r2
new_article2.save()
new_article2.reporter   # <Reporter: Paul Jones>
```

question id: 6519dcf8-4cff-4dc4-9542-d666791872c5


### Get all articles of a reporter

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
reporter.article_set.all()
```

question id: e314c695-3a83-4695-b7c8-3da9ce8c31d5


### How many articles does a reporter have? 

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
reporter.article_set.count()
```

question id: 8f568cfa-bc64-45cb-8a19-3b566114f02e


### Through a Reporter instance find all articles where headline begins with the word 'This'

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
reporter = Reporter.objects.filter(id=1)
if not reporter:
    return None

qs = reporter...
```

answer
```python
qs = reporter.article_set.filter(headline__startswith='This')  # <QuerySet [<Article: This is a test>]>
```

question id: d712a518-3500-4949-be9e-96ecfbcb3389

### Find all Articles for any Reporter whose first name is "John"

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

```python
article = Article.objects.filter(id=1)
if not article:
    return None

# your code here
```

answer 
```python
articles = Article.objects.filter(reporter__first_name='John')  # <QuerySet [<Article: John's second story>, <Article: This is a test>]>
```

question id: 439cbe0b-f0e8-46cd-a39b-48143fa2be55


### Find all Articles for any Reporter whose first name is "John" and the last name is "Smith"

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)


answer

```python
articles = Article.objects.filter(reporter__first_name='John', reporter__last_name='Smith') 
articles # <QuerySet [<Article: John's second story>, <Article: This is a test>]>
```

question id: 09bce10f-b0bf-425b-9172-6953a81cbdaf


### Find all the articles that belong to reporters with id 1 and 2

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

answer
```python
Article.objects.filter(reporter__in=[1,2]).distinct()
# <QuerySet [<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]>
```

question id: '952ec3b1-c000-44b2-af89-8980027685bf

### Find all the articles that belong to reporters instances reporter1 and reporter2

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

answer
```python
Article.objects.filter(reporter__in=[reporter1,reporter2]).distinct()
# <QuerySet [<Article: John's second story>, <Article: Paul's story>, <Article: This is a test>]>
```

question id: d2dba754-a7aa-442b-ad2c-92ca3dc26d0b


### Find all the reporters whose articles' headlines begin with 'This'

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

answer
```python
Reporter.objects.filter(article__headline__startswith='This').distinct()
# <QuerySet [<Reporter: John Smith>, <Reporter: John Smith>, <Reporter: John Smith>]>
```

question id: 0109e1e3-63d2-4cd6-9985-78fd7212690e

### Delete all the reporters whose articles' headlines begin with 'This'

Having Reporter and Article relationship via Foreign Key 
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_one/#many-to-one-relationships)

answer
```python
Reporter.objects.filter(article__headline__startswith='This').delete()
```

question id: 250a6873-9661-4b10-8329-428175f9c3fa

### How does caching work for many-to-one relations?

Forward access to one-to-many relationships is cached the first time the related object is accessed. Subsequent 
accesses to the foreign key on the same object instance are cached. Example:

```python
e = Entry.objects.get(id=2)
print(e.blog)  # Hits the database to retrieve the associated Blog.
print(e.blog)  # Doesn't hit the database; uses cached version.
```

question id: 01e0dcd7-776d-4830-badb-949164df26af


### How to get all the streets of a country?

Let's imagine you have these four models

```python
from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=128)

class City(models.Model):
    name = models.CharField(max_length=128)
    country = models.ForeignKey(Country, related_name="cities")

class Dictrict(models.Model):
    name = models.CharField(max_length=128)
    city = models.ForeignKey(City, related_name="districts")

class Street(models.Model):
    name = models.CharField(max_length=128)
    district = models.ForeignKey(Dictrict, related_name="districts")
```

How to get all the streets of some country?
For example, you have country:
```python
germany = Country.objects.filter(name="Germany").first()
```

And you want to get a list of all the streets in this country. How would you do it?
To get all streets of a District would be stupidly easy, just 
```python
some_district = District.objects.filter(name="some_district").first()
some_district.streets.all()
```

But how to get all the streets of a Country?

answer
As easy as that:
```python
germany = Country.objects.filter(name="Germany").first()

Street.objects.filter(district__citry__country=germany)
```

https://docs.djangoproject.com/en/3.2/topics/db/queries/#lookups-that-span-relationships

question id: 590a8a67-0cc3-4aa2-98ea-e762a99e07bd
