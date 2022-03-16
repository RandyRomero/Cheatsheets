### How to get a list of calls of a mock?

```python
your_mock.call_args_list  # [call(), call(3, 4), call(key='fish', next='w00t!')]
```

where call() is a tuple-like object with the args with which the mocked function was called

https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.call_args_list

question id: 76777de2-bacc-45e3-96e2-dc7cd9a0cbc3


### What is the difference between side_effect and return_value? When to use each of them?

side_return is for iterables, exceptions and async functions
return_value for the rest

answer

Examples:
```python
mocker.patch(
        "amocrm_consumer.managers.amocrm.AMOCRMManager._fetch_entity_data_by_query",
        side_effect=CoroutineMock(
            return_value=main_contact_factory(custom_fields_values=custom_fields, _quantity=1),
        ),
    )
```
Here we used `side_effect=CoroutineMock(...)` because `_fetch_entity_data_by_query` is an async method
and `return_value=main_contact_factory(...)` because it is a usual function.

question id: 2eaf682e-1920-40e1-9054-7516f2ab7540


### How to make mock return new value each time?

answer

You can assign an iterable to side_effect, and the mock will return the next value in the 
sequence each time it is called:
```python
from unittest.mock import Mock
m = Mock()
m.side_effect = ['foo', 'bar', 'baz']
m()  # 'foo'
m()  # 'bar'
m()  # 'baz'
```

question id: c6708096-7632-4617-a4c1-253e850373de
