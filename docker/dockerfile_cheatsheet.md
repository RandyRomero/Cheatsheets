### What is a command to specify a base image to build you image from it?

answer:

`FROM`

e.g.
`FROM python:3.11.2-alpine3.17`

question id: 98a12198-1537-4891-a5f3-31ce61811baa


### What is the command to change working directory?

answer:

`WORKDIR`

e.g.

`WORKDIR /app`

question id: cb4c3c26-e6f9-4722-ba83-3c63177b1f2


### How to copy all files from the current working directory to cwd of the container?

answer

`COPY . .`

question id: bd1a57c7-9b21-4036-8c17-294e658a509f


### What's wrong with this dockerfile code?

```Dockerfile
RUN mkdir /src
COPY . /src
```

answer:

You don't have to create a new folder, COPY will create one for you if it doesn't exist

```Dockerfile
COPY . /src
```

question id: d00b8524-7df9-4670-ba56-b17afc62b5e4


### How to copy a file that has spaces in its name?

answer:

There is special COPY syntax for this case

```Dockerfile
COPY ["file name.txt", "another file name.txt", "."]
```

question id: a2b92acc-3cd8-46bd-bb3e-8da01f63cdea


### What is ADD command for?

answer:

It's the same as COPY, but has additional features.
For example, it let's you copy file from URL, if you have access to it, e.g:

```Dockerfile
ADD http://.../file.json .
```

Also, it can auto unarchive archives for you like this:
```Dockerfile
ADD file.zip .
```

question id: 2e08e9a4-b92a-434d-8602-ab050682c39f


### How to execute a shell command?

Use RUN command
e.g.
`RUN pip install -r requirements.txt`

question id: c2307c77-9e22-465e-92c5-1bb82be1b2e4


### What is CMD command?

answer:

The CMD command​ specifies the instruction that is to be executed when a Docker container starts.

e.g.

`CMD python main.py`

question id: bc67b7f3-a61c-48f3-adfe-3db424ed756c


### How to specify a command that is to be executed when a Docker container starts?

answer;

Use CMD

e.g.

`CMD python main.py`

question id: 98107122-1b22-44e9-938d-b6e8f05b34a2


### Write the simplest Dockerfile that run hello_docker.py script

answer:

```dockerfile
FROM python:3.11.2-alpine3.17

WORKDIR /src

COPY . .

CMD ["python", "hello_docker.py"]
```

question id: b9fa9f8c-f07b-438e-806d-23bb48737dd7


### How to set an eviromental variable in Dockerfile?

answer

```Dockerfile
ENV YOUR_VAR=whatever
```

For example:

dockerfile
```Dockerfile
FROM python:3.11.2-alpine3.17

WORKDIR /src

COPY poetry.lock pyproject.toml /src/

RUN pip install -U pip && \
    pip install poetry && \
    poetry export --without-hashes --format=requirements.txt > requirements.txt && \
    yes | pip uninstall poetry && \
    pip install -r requirements.txt

COPY . .

RUN pip install --editable .

ENV RABBIT_HOST=localhost \
	RABBIT_PORT=5672 \
	RABBIT_LOGIN=guest \
	RABBIT_PASSWORD=guest \
	SLEEP_TIMEOUT_SECONDS=60

CMD ["python", "meter"]
```

question id: 68d19232-f2bf-4084-88e0-5209ecd62ae2


### What is EXPOSE for?

answer:

It is just a form of documentation. It tells anyone who is gonna use the container
that the container is going to listen to the port that is mentioned after EXPOSE command.
It does not expose a port of the cointainer. To expose a port of a container you need
to use -p flag when you create your container like `docker run -p 3000:3000`. 

https://docs.docker.com/engine/reference/builder/#expose


question id: 669dab01-02bf-45d1-b309-3c4a3fc90416


### How to denote what ports the application in the container is going to listen to?

answer:

You can use EXPOSE command to denote any ports your application is supposed to listen to

https://docs.docker.com/engine/reference/builder/#expose

question id: 9facb7dc-e198-4a3b-ad56-38d8651001ad


### How to create and use a non-root user in the container?

answer

```Dockerfile
RUN addgroup username && adduser -S -G username username

USER user
```

where -G is for setting primary group for the user and 
-S means that we are creating a so called system user

For example:
```Dockerfile
FROM python:3.11.2-alpine3.17

WORKDIR /src

COPY poetry.lock pyproject.toml /src/

RUN pip install -U pip && \
    pip install poetry && \
    poetry export --without-hashes --format=requirements.txt > requirements.txt && \
    yes | pip uninstall poetry && \
    pip install -r requirements.txt

COPY . .

RUN pip install --editable .

ENV RABBIT_HOST=localhost \
	RABBIT_PORT=5672 \
	RABBIT_LOGIN=guest \
	RABBIT_PASSWORD=guest \
	SLEEP_TIMEOUT_SECONDS=60

RUN addgroup app && adduser -S -G app app

USER app

CMD ["python", "meter"]
```


question id: add8a0b0-a292-48d4-8d50-8ba28252b50c


### What is the difference between RUN and CMD?

answer:

They both for running commands, but RUN is for running commands
during building the image, and CMD is for running a command when
the image is built.

question id: 6f1199c8-3066-419c-9a18-5d015185e093s


### What is the shell form of CMD and execute form of CMD?

answer:

Shell form looks like this:
`CMD python main.py`

Execute form:
`CMD ["python", "main.py"]`

The first one spins a separate shell process to run the given command.
The current best practive is to use execute form so as not to spin a separate shell.
Also, it makes it easier and faster to clean up resources when you stop containers.

question id: b81fe4a4-b475-453c-9f4e-2b7b50bcef52


### What is the difference between CMD and ENTRYPOINT commands?

answer:

They are quite similar, the only difference is that with CMD it is easier
to overwrite the command that is going to be executed on the container start up.

Example:
`docker run my-app` will run whatever command your specified in CMD/ENTRYPOINT.

However, if you specify in Dockerfile your command via CMD, you can easily
overwrite it like this:
`docker run my-app %another-command%`,
e.g. `docker run my-app python manage.py migrate`

If you specify in Dockerfile your command via ENTRYPOINT,
in order to override it you need to use a flag '--entrypoint` like this:

`docker run my-app --entrypoint %another-command%`,
e.g. `docker run my-app --entrypoint python manage.py migrate`

There is no clear answer what to use best, so it's on you

question id: fac24ee4-f917-49a2-808f-0aa8ede327d7


### Why should we install libraries (like npm install, pip install etc) before we copy the project files to the container?

answer:

Docker container consists of layers that sit on top of each other.
Every command creats a layer. Docker caches layers, so if nothing
is changed in the layer,  the docker will not build the layer and will
use the cache instead.

Long story short. If you have a command which installs external libraries after
you copy all files from the disk, this means that if you change at least one 
single character in your files, this layer and the next layers will have to be rebuilt,
so Docker will donwload and install all dependencies again if you change anything
in your files. Of course, there is no point in doing that. We should only
reinstall dependencies if your pyproject.toml (requirements.txt or similar fle) has changed.

So, for example, instead of this
```Dockerfile
COPY . .

RUN pip install -U pip && \
    pip install poetry && \
    poetry export --without-hashes --format=requirements.txt > requirements.txt && \
    yes | pip uninstall poetry && \
    pip install -r requirements.txt
```

do this

```Dockerfile
COPY poetry.lock pyproject.toml /src/

RUN pip install -U pip && \
    pip install poetry && \
    poetry export --without-hashes --format=requirements.txt > requirements.txt && \
    yes | pip uninstall poetry && \
    pip install -r requirements.txt

COPY . .
```

question id: 883c7b7b-7a3e-49a1-b363-57c4958bdf59


### How should you organise the order of commands in your Dockerfile?

answer:
The least frequently changed on top, the most frequently changed at the bottom

question id: dfecf5de-020b-4590-8af2-cdbcc9390d1a


