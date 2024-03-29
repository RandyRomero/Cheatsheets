============ DISPLAY ===========

only show selected test, do not run them
pytest --collect-only -q

show you time spent on every test
pytest --durations=0

show your log messages and prints
pytest -s

vesbose
-v

stop on the first fail
pytest -x:

run last failed tests
pytest --lf:

### hide all warnings
```pytest --disable-warnings```

question id: c54fa584-4eeb-4116-9218-236eebf8a3f1

### show local variables (shortcut)
pytest -l

show reasons why tests were skipped
pytest -r

============= MARKING TESTS WITH CUSTOM MARKS ===========

first add marker to pytest.ini

[pytest]
markers =
    your_mark_name: description of this marker

then use decorator:

@pytest.mark.your_mark_name
def test_bla_bla_bla
	pass

then run pytest with -m flag
>> pytest -m 

============ MARKING TESTS TO BE SKIPPED ==================

# just skip test
@pytest.mark.skip(reason='misunderstood the API')

# skip if any valid python expression
@pytest.mark.skipif(tasks.__version__ < '0.2.0',
reason='not supported until version 0.2.0')

============ MARKING TESTS AS EXPECTED TO FAIL ==================
@pytest.mark.xfail()

test_unique_id_4.py xxX. - x means test was expected to fail and failed; X means test was expected to fail but it passed

You can configure pytest to report the tests that pass but were marked with
xfail to be reported as FAIL. This is done in a pytest.ini file:
[pytest]
xfail_strict=true


============ RAISES =================
from pytest import raises

with pytest.raises(TypeError):
	run your function that should raise TypeError (or something)

=========== FIXTURES ================

--setup-show shows you when and which fixtures were used during the running of each test




