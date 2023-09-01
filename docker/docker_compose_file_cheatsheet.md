### Convert this json file to yaml format

```json
{
    "name": "The Ultimate Docker Course",
    "price": 149,
    "is_published": true,
    "tags": ["software", "devops"],
    "author": {
        "first_name": "Mosh",
        "last_name": "Hamedani"
    }    
}
```

answer:

```yml
name: The Ultimate Docker Course
price: 149
is_published: true
tags: 
    - software
    - devops
author:
    first_name: Mosh,
    last_name: Hamedani
```

question id: 9848904e-2b58-4d80-9df3-4105e83d947


### Write a docker-compose file:

- for one service with a random name
- that is on the host system, not in docker-hub
- map some ports

answer:
```yaml
version: "3.8"

services:
    my_app:
        build: ./my_app
        ports:
            - "3000:3000"
```

question id: 6c66674c-d5ff-40a7-b39e-7f4ca39b7410
    

### Write a docker-compose file:

- for one service with a random name
- that is on dockerhub
- define a couple of environmental variables


answer:
```yaml
version: "3.8"

services:
    python:
        image: python:3.11.2-alpine3.17
        environment:
            ENV_NAME: env_value
            ANOTHER_ENV: another_value
```

question id: 6c1459ae-2f05-4e0e-9a5f-732219fe1360


### Write a docker-compose file:

- that only starts up mongo database
- use image called mongo:4.0-xenial
- map port 27017
- use a volume with any name and path '/data/db` (that's where mongo stores its data)

answer:

```yaml
version: "3.8"

services:
    database:
        image: mongo:4.0-xenial
        ports: 
            - "27017:27017"
        volumes:
            - vol_name:/data/db
volumes:
    vol_name:
```

Note that in order to use a volume we need to declare it. The key is a volume name, the value is empty

question id: 5e037fab-cce2-4843-ba7a-40a9476162ee


### What to use instead of 'localhost` in your docker-compose.yml when proviging a link to a db or any other service?

```YAML
version: "3.8"

services:
  broker:
    image: rabbitmq:3.11.10-management
  meter:
    image: bancini/meter:3
    environment:
      RABBIT_HOST: ???
```

answer:

Instead of `localhost` you need to use the name of the service as it is defined in your docker-compose.yml. 

So, for example:
```YAML
version: "3.8"

services:
  broker:
    image: rabbitmq:3.11.10-management
  meter:
    image: bancini/meter:3
    environment:
      RABBIT_HOST: broker
```

Here you can see that in order to make service `meter` able to connect to our rabbitmq broker,
we set RABBIT_HOST env to be equal to name of rabbit service `broker`.

question id: 690e973b-fbfd-447d-91a5-dcd752114110


### How to run tests in your docker-compose?

answer:

Inside your docker-compose.yml you can define a copy of your service, but with '-test' prefix,
and override its command with, let's say, pytest -x or whatever.

Example:
```YAML
version: "3.8"

services:
  one_service:
    image: one_service:1.0
  another_service:
    build: ./another_service
    depends_on:
      - another_service_tests
  another_service_tests:
    image: foldername_another_service  # reusing already build meter image (dockercompose+name + image name)
    command: pytest -x
```

question id: 1b19d460-a875-440d-b4f1-dde6afa46406


### How to make sure your containers restart if they fail?

Use `restart` directive

answer:
```YAML
version: "3.8"

services:
  my_service:
    restart: on-failure  # or it could be on-failure:5 to limit the number of attempts
```

You can read more about restart policies here:
https://docs.docker.com/config/containers/start-containers-automatically/

question id: 43243e07-6aae-4539-b0ff-68cd491a75ba


### How to use .env file in docker-compose.yml?

answer:

First, define your variables in .env like

```
DB_PASSWORD=111111
````

You .env file must reside in the same folder as your .docker-compose file

Docker will assign enviromental variables from .env file automatically when you
execute `docker-compose up`.

Secondly, access these variable in your docker-compose.yml via `${DB_PASSWORD}` like this:

```YAML
version: "3.8"

services:
  my_app:
    build: ./my_app
    environment:
      - DB_PASSWORD=${DB_PASSWORD}
```

question id: c61310c8-b937-423b-8cea-a7d374daceea


### How to start a container only if the other one has already started?

answer:

Use `depends_on` and `healthcheck` like this:

```YAML
version: "3.8"

services:
  my_app:
    build: ./my_app
    depends_on:
      another_app:
        condition: service-healthy
  another_app:
    build: ./another_app
    healthcheck: 
      test: curl --fail http://another_app:3000/health-check || exit 1
      interval: 5s
      timeout: 5s
      retries: 10
```

question id: 5fd3a1c4-ba14-4f22-bd29-67c2a355bd15


### What is the difference between `interval` and `timeout` in docker compose file?

An example of a docker compose file:

```YAML
version: "3.8"

services:
  my_app:
    build: ./my_app
    depends_on:
      another_app:
        condition: service-healthy
  another_app:
    build: ./another_app
    healthcheck: 
      test: curl --fail http://another_app:3000/health-check || exit 1
      interval: 5s
      timeout: 5s
      retries: 10
```

answer:


interval - time before next attempt to test the container
timeout - if one attempt to test the container takes more than `timeout` time, it is considered failed

question id: 5c4bcb3f-0ca6-4eee-bbe5-e43b4a1e6e38



### How to apply migrations before the start of the application?

answer:

In case, for example, you have two apps in your docker-compose file: a backend-app and a database,
you need to follow these two steps:
- make sure your db starts first
- then you need to override the starting command of your backend app. For example, if it was `python run.py` it should become something like `alembic upgrade head && python run.py`

E.g.:
```YAML
version: "3.8"

services:
  back:
    build: ./
    ports:
    - "8000:8000"
    restart: on-failure:5
    environment:
      - POSTGRES_DB_USER=fastapi_books
      - POSTGRES_DB_NAME=fastapi_books
      - POSTGRES_DB_PASSWORD=fastapi_books
      - POSTGRES_DB_SERVER=db
    depends_on: 
      db:
        condition: service_healthy
    command: sh -c "alembic upgrade head && python run.py"
  db:
    image: postgres:15.2
    restart: on-failure:5
    healthcheck:
      test: /usr/bin/pg_isready
      interval: 5s
      timeout: 5s
      retries: 10
    environment:
      - PGUSER=fastapi_books
      - POSTGRES_PASSWORD=fastapi_books
      - POSTGRES_DB=fastapi_books
```

question id: 482283d9-272a-4589-a59b-b60f46cec47f


### How to run docker-compose with custom file name?

For example, you would like to run docker-compose-test.yml file

answer:

`docker-compose -f docker-compose-test.yml up`

question id: 1aff2d5e-174e-493b-8737-558471c12e42


### How to override a CMD of Dockerfile in docker-compose.yml?

answer:

With `command` directive, like this:

```YAML
version: "3.8"

services:
  back:
    build: ./
    command: sh -c "alembic upgrade head && python run.py"
```

question id: 21d7ddd6-cfa4-470a-8191-d7cd123da842


### How to specify what Dockerfile to use?

answer:
```YAML
version: "3.8"

services:
  back:
    build:
      context: ./ # path to your app
      dockerfile: your-dockerfile-name
```

question id: b88edf49-384d-414a-89eb-e1529cfef969


### How to force docker-compose to recreate containers?

answer:

With flag `--force-recreate`

E.g.:
`docker-compose up --force-recreate`

Note: somehow it doesn't recreate postgres container if you don't provide a flag `-V` as well
which stands for removing anonymous volumes.

question id: 84da9b45-2f3f-41d7-86da-87a7b9e33ac4


### How to specify a name of your docker-compose project on start?

answer:

`docker-compose up -p my-app`

question id: 090a67b7-fe4f-403e-b247-a383efd07646


### How to `docker-compose down` automatically when on of containers exists?

For example, when you use docker-compose to test your app with database and want
all of it to stop when tests are completed.

answer:

`docker-compose up --abort-on-container-exit`


question id: e35fa21d-f3f8-4341-99ee-82a8523f220c



