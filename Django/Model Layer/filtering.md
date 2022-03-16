### Get several rows if they are in lists of some keys

```python
tasks = Task.objects.filter(id__in=[1, 3, 4])
```

SQL equivalents:
```sql
SELECT <...> WHERE id IN (1, 3, 4);
```

question id: 4b05f0f3-e9eb-4374-84d7-ca824c279d11



### Filter objects by a year part of timezone.now()
`Someobj.objects.filter(some_timezone_field__year=timezone.now().year)`

question id: 6923611a-261f-4302-8af3-1c25cb3d630b


