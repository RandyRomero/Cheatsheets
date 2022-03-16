### Update translations (django.po)

```bash
python manage.py makemessages --locale='ru_RU'
```

question_id: 3006b743-72f7-4a54-b8aa-d5a7ec3a9a91


### How to rerun django migration? 

0.  Fake back to the migration before the one you want to rerun.

```python
./manage.py migrate --fake yourapp 0010_my_previous_data_migration
```

1. Then rerun the migration.

```python
./manage.py migrate yourapp 0011_my_data_migration
```

https://stackoverflow.com/questions/31953587/rerun-a-django-data-migration

question id: 443edc3d-f68a-4ea6-97fd-8bb73782fe45


### How to enforce unique constraint on condition?

For example, you have a model like this:
```python
class Process(Place):
    isRunning = models.BooleanField(default=True)
    name      = models.CharField(max_length=20)
```
And you would like to enforce that the `name` field is unique when `isRunning` is true.
How would you do that?

answer
```python
from django.db.models import Q, UniqueConstraint

class Process(Place):
    ...
    class Meta:
        constraints = [UniqueConstraint(fields=["name"], condition=Q(isRunning=True))]
```

https://stackoverflow.com/questions/32124186/django-uniqueness-constraint-when-a-specific-field-is-true

question id: 6d071f13-5315-4a2b-97ac-3e9f639dc8


### What's decorator 'classproperty' for?

You can use it two wrap your class method to be able to get result of the method as an attribute
of your class.

Example:

```python
from django.utils.decorators import classproperty

class MasterStatus(models.TextChoices):
    """Master status choices."""

    ENABLED__WORK = "ENABLED__WORK", _("Enabled - At work")
    ENABLED__RESERVE = "ENABLED__RESERVE", _("Enabled - In reserve")

    @classproperty
    def enabled_statuses(self) -> tp.Set[str]:
        """All enabled statuses."""
        return {str(status) for status in self if status.startswith("ENABLED")}

'whatever' in MasterStatus.enabled_statuses  # False
```

Available since Django 3.1

question id: 19b2a5e9-54e9-4d8e-903c-a5c50b28f626


### How to make PATCH request testing DRF app?

```python
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()  # actually it is more complicated, but for the sake of example it will do
payload = {"key": "value"}
resp = client.admin_api_client.patch(reverse("users-detail", args=[user.id]), data=payload)
```

question id: 364dff48-a2c7-452d-991f-38c99042d245


### How to start django shell?

```
python manage.py shell
```

question id: eaf2ce63-4f7e-4627-b5dc-a498dcc3e3fe


### How to return an empty queryset?

```python
queryset.none()
```

question id: 0374ab9a-e449-4ce2-b2c7-bf5d8f085e50


### How to list applied and not-yet-applied migrations?

python manage.py showmigrations

question id: 29a2185d-b46e-4d2b-8c73-029b3652caa3


### How to list applied and not-yet-applied migrations in a specific app?

python manage.py showmigrations my_app

question id: fc1468dc-883b-41ac-8bac-e678f3735db1


### How to rollback a migration?

You can revert by migrating to the previous migration.

For example, if your last two migrations are:

0010_previous_migration
0011_migration_to_revert
Then you would do:

```bash
python manage.py migrate my_app 0010_previous_migration
```

You don't actually need to use the full migration name, the number is enough, i.e.

```bash
python manage.py migrate my_app 0010
```

You can then delete migration 0011_migration_to_revert.

https://stackoverflow.com/questions/32123477/how-to-revert-the-last-migration

question id: 9d3a0d86-e9fb-4a67-80f8-cb217de94bdb