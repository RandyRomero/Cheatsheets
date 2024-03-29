### How to set some default ordering for a Django model?

answer:

Add class `Meta` with field `ordering` which should be a tuple (or iterable, I am not sure)

```python
from django.db import models

class Cat(models.Model):
    ...
    class Meta:
        ordering = 'name',
```

question id: 0b34dd9a-843c-4bd0-997a-2a6b42bb86be

### What is the ordering kind there?

```python
from django.db import models

class Cat(models.Model):
    ...
    class Meta:
        ordering = 'name',
```

answer

ascending

question id: baf60298-ee58-47dd-92a9-5985ba51abd8


### What is the ordering kind there?

```python
from django.db import models

class Cat(models.Model):
    ...
    class Meta:
        ordering = '-name',
```

answer

descending

question id: 8d26e3f0-0716-4ebf-b175-f1f43a16075d


### What is the ordering kind there?

```python
from django.db import models

class Cat(models.Model):
    ...
    class Meta:
        ordering = '-name', 'birthdate',
```

answer

descending for name, ascending for birthdate

question id: 78d7ccad-969a-4d4d-b6ce-39c2e78327ec


### How to order Article model by default by last_name of related Reporter?

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

answer

```python
from django.db import models

class Article(models.Model):
    ...
    class Meta:
        ordering = 'reporter__last_name',
```

question id: 221516b2-a538-4b1e-b7be-6a76099e7afe