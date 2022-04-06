### How to use two or move variables in parametrize?

Write some dummy test function and parametrize it with variables `foo` and `baz` which takes in first iteration of 
test values 1 and 2, and in the second iteration values 3 and 4. 

```python
import pytest

@pytest.mark.parametrize(("foo", "baz"), [(1, 2), (3, 4)])
def test_something(foo, baz):
    return foo + baz
```

Key point: variable names your put in tuple, values should be in list - one tuple of values for one iteration

question id: 3368cdbb-bb6a-4321-b925-011455dc809e


### How to ensure that calling a function raises an error? 

answer
```python
with pytest.raises(WhateverExecptionYouAnticipate):
    call_your_function()
```

question id: 43d0faf6-93e6-4df2-929c-c7c684842cd0


### How to assert error message?

answer
```python
with pytest.raises(WhateverExecptionYouAnticipate) as excinfo:
    call_your_function()

assert str(excinfo.value) == 'Whatever error message you anticipate'
```

https://stackoverflow.com/questions/57560531/assert-exception-message

question id: 0ab836f9-358a-4988-be9d-9238e2db4f20


### How to parametrize a fixture?

For example you have a fiture that returns something. 
You want to make it return diffrent values for a "cat" key on each call instead of a hardcoded one. 

Your list of values: [1, 2, 3]
Your fixture: 

```python
import pytest 

@pytest.fixture()
def test_return_some_payload():
    return {"cats": 1, "dogs": 0}
```

answer
Create a new fixture, pass your iterable as a param.request, 
see details below in the example code:

```python
import pytest

CAT_VALUES = [1, 2, 3]

# auxiliary fixture
@pytest.fixture(params=CAT_VALUES)
def cat_values(request):
    """Return all possible cat values."""
    return request.param

# your actual fixture
@pytest.fixture()
def test_return_some_payload(cat_values):
    return {"cats": cat_values, "dogs": 0}
```

question id: should not learn by heart