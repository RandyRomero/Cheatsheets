List images:
docker image ls

List containers (will be shown only running containers):
docker container ls

List both running and exited containers:
docker container ls --all

### How to remove specific image?

docker image rm your_image

question id: 675e50ad-2188-4946-9742-8f56b7b48373



### How to set build-time variables?

--build-arg YOUR_KEY=YOUR_VALUE

e.g

--build-arg GITLAB_LOGIN="hacker666"

question id: 3cc01bf9-43d3-4496-84ec-005b76f7b952


### What is ARG and what is ENV instructions for?

The ARG instruction defines a variable that users can pass at build-time to the builder with 
the docker build command using the --build-arg <varname>=<value> flag. They are only 
available from the moment they are ‘announced’ in the Dockerfile with an ARG instruction 
up to the moment when the image is built. Running containers can’t access values of ARG variables.

The ENV instruction sets the environment variable <key> to the value <value>.
The environment variables set using ENV will persist when a container is run from the resulting 
image.

https://vsupalov.com/docker-arg-env-variable-guide/#arg-and-env-availability

https://stackoverflow.com/questions/41916386/arg-or-env-which-one-to-use-in-this-case

question id: eac5385e-c41f-4efc-84de-ab7f4aa3ba26
