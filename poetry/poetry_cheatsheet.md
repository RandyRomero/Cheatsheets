activate environment
poetry shell

### How to install all dependencies from pyproject.toml?

poetry install

question id: 5db3016a-1543-4b08-8de3-33525ff59c1e


install a new package and add it to dependencies
poetry add package-name

list all packages:
poetry show

### How to bump version of your library?

```markdown
poetry version major/minor/patch
```

https://python-poetry.org/docs/cli/#version

question id: 0141d980-9d0a-4bc3-8fdc-805534afd38a


### How to install a library with its extra dependencies?

answer:

`poetry add -E main_package`

 will install main package with extra dependencies

 question id: 396cea0b-9edf-4a6a-a4b1-297609cec861

