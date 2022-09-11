### What is the name of the library that allows you to read files from the package itself?

answer:

importlib-resources

https://pypi.org/project/importlib-resources/

question id: 983f80f1-1b68-48cd-a51b-595c28ba1719


### How to open a text file that lies is located within your package?

```python
from importlib_resources import files

with open(files("package_name", "path/to/file.txt"), "r") as file:
    for line in file:
        print(line)
```

More on using importlib:
https://youtu.be/ZsGFU2qh73E

question id: f369138d-f88f-4731-bd81-79fc36b6d417


### How to get a Path of a file from inside the running package?

```python
import importlib_resources

async foo():
    with importlib_resources.path('package_name.folder_in_package.another_folder', "my_script.py") as my_script_path:
        # do something with my_script_path
```

question id: ae9d3632-4896-4384-81cf-4515ed2b5a32