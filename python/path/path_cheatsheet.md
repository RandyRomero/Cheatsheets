### What does 'pathlib.Path.cwd().glob('*.txt')' mean?

answer:

Find in current working directory all the files with *.txt extension.
The method will return a generator with paths to these files.

question id: 472f7638-0fb3-4f22-b234-733ede41380f


### How to find all the files with *.txt extenstion in the current working directory?

answer:

```python
pathlib.Path.cwd().glob('*.txt')
```

The method will return a generator with file names.

question id: df5edef3-f77d-4b95-bf7b-fcf84dce7d70


### How to add a directory of a file to Path object?

For example you have:
```python
from pathlib import Path

start_path = Path.cwd()
start_path   # PosixPath('/home/aleksandr/yad/Studies/Cheatsheets') for example
```

How to add 'foo/bar.py' to this path?

answer:
```python
from pathlib import Path

start_path = Path.cwd()
start_path   # PosixPath('/home/aleksandr/yad/Studies/Cheatsheets') for example
final_path = start_path / "foo" / "bar.py"
final_path  # PosixPath('home/aleksandr/yad/Studies/Cheatsheets/foo/bar.py')
```

question id: 0893e976-735e-43d6-ac3d-fe55d048ad58


### How to remove a file or directory from the Path?

For example you have:
```python
from pathlib import Path

start_path = Path.cwd()
start_path   # PosixPath('/home/aleksandr/yad/Studies/Cheatsheets') for example
final_path = start_path / "foo" / "bar.py"
final_path  # PosixPath('home/aleksandr/yad/Studies/Cheatsheets/foo/bar.py')
```

How to remove 'bar.py'?

answer:

```python
from pathlib import Path

start_path = Path.cwd()
start_path   # PosixPath('/home/aleksandr/yad/Studies/Cheatsheets') for example
final_path = start_path / "foo" / "bar.py"
final_path  # PosixPath('home/aleksandr/yad/Studies/Cheatsheets/foo/bar.py')
most_final_path = final_path.parent
most_final_pat  # PosixPath('/home/aleksandr/yad/Studies/Cheatsheets/foo')
```

question id: 17af260d-189d-43fe-9d2a-69616620b06b


### Path.mkdir(parents=True) - what does the flag mean?

answer:

It means any missing parents of thes path are created as needed

https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir

question id: 0893e976-735e-43d6-ac3d-fe55d048ad58


### How to recursively create a dir with pathlib.Path.mkdir()? 

Means that if some directories in the given path are missing - create them as well

answer:

Use parents=True flag

```pyton
from pathlib import Path

Path.mkdir(parents=True)
```

https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir

question id: c67fc5e4-b9b2-43b1-a1f3-0dfa2fa94d77


### How to ignore that directory already exists while pathlib.Path.mkdir()?

answer:

Use flag `exist_ok=True`

https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir

question id: 7903d297-2f00-474c-8d3d-51a0eea5d4a2


### Path.mkdir(exist_ok=True) - what does the flag mean?

answer:

FileExistsError exceptions will be ignored (same behavior as the POSIX mkdir -p command), 
but only if the last path component is not an existing non-directory file.

https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir

question id: 3fe43204-93a4-48ef-a40c-2d988c7adc3b