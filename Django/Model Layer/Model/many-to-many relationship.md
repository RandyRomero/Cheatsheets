Example of m2m relationship

```python
from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ['headline']

    def __str__(self):
        return self.headline
```


### What field should we use to define many-to-many relationship in Django?

answer

`django.db.models.ManyToManyField()`

question id: 8f47f44f-dd80-4cb3-b09a-255dfc01a826


### How to associate an Article with the Publication?

Article and Publications are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

```python
article = Article.objects.filter(id=1).first()
publication = Publication.objects.filter(id=1).first()
# your code here
```

answer
```python
article = Article.objects.filter(id=1).first()
publication = Publication.objects.filter(id=1).first()

article.publications.add(publication)
# or
publication.article_set.add(article)
```

question id: 008f2016-6154-4b73-82e6-d57d268a04a1


### How to add multiple records to ManyToManyField at once?

For example you have this code

```python
publication = Pubclication.objects.filter(id=1).first()
if not publication:
    return None

a1, a2, a3 = Articles.objects.all()
# You need to associate these articles with the publication
# your code here
```

answer

```python
publication.article_set.add(a1, a2, a3)
```

question id: 3149343a-55e2-430d-b122-bebebb16cf91


### What if you associate a particular Article with a particular Publication more than once?

Article and Publications are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

```python
article = Article.objects.filter(id=1).first()
publication = Publication.objects.filter(id=1).first()
article.publications.add(publication)
article.publications.add(publication)
```

answer

Adding a second time is OK, it will not duplicate the relation

question id: f1efc3e5-c03b-4386-ab70-a29898bde1ab


### Create and add an Article to a Publication via publication instance:

Article and Publications are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

```python
publication = Publication.objects.filter(id=1).first()
# your code here
```

answer

```python
publication = Publication.objects.filter(id=1).first()
new_article = publication.article_set.create(title='Highlights for Children')
```

question id: 2d7e8d24-6139-4229-ae47-f696185731f8


### Get all articles of some Publication and all publications which contain some Article

Article and Publications are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

```python
publication = Publication.objects.filter(id=1).first()
# your code here - get all related articles

article = Article.objects.filter(id=1).first()
# your code here - get all related publications
```

answer

```python
publication = Publication.objects.filter(id=1).first()
publication.article_set.all()

article = Article.objects.filter(id=1).first()
article.publications.all()
```

question id: e7095d9a-9261-4094-ae0a-acffac8ea8c3


### Get all articles except related to a specific publication

Article and Publications are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

answer

```python
Article.objects.exclude(publications=p2)
```

question id: 3354b98a-eaa3-42b5-a501-e9f0ea7a05f4

### How to remove connection between two m2m entities?

For example you have  rticle and Publications that are related via m2m relationship
(https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/#many-to-many-relationships)

like 
```python
article = Article.objects.filter(id=1).first()
publication = Publication.objects.filter(id=1).first()

article.publications.add(publication)
# or
publication.article_set.add(article)
```

How to disconnect them?

answer

```python
article.publications.remove(publication)
# or 
publication.article_set.remove(article)
```

question id: e65821bb-ab6e-4ee0-8d02-acf2dc81696a

### How to remove all Publications which title begins with "Science"?

```python
Publication.objects.filter(title__startswith='Science').delete()
```

question id: 96c58507-ae9c-4d1e-b9d0-7aec18b8834c