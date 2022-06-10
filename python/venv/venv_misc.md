### How to create virtual environment based on active Python verison with out-of-the-box method?

answer:

```
python -m venv /path/where/to/create/venv/
```

for example:
```
python -m venv ./venv
```
will create venv folder within the current folder

question id: 08f72bf4-4a12-42e5-a766-f331dd7da1fe


### How to activate an environmet created by venv?

answer: 

```
source venv_folder_name/bin/activate
```

in fish:
```
source venv_folder_name/bin/activate.fish
```

question id: e57d79a8-d599-4828-8cb6-85f23119a69c


### How to install all requirements from requirements.txt?

answer:

```
pip install -r requirements.txt
```

question id: 29238d2b-c1c5-4ad0-a800-e9721d9f6c5b


### How to deactivate virtual environment created by venv?

answer:

```
deactivate
```

question id: 5a16db13-c992-48cb-99a2-590f91507010