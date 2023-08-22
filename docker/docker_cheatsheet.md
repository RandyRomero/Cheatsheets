
### How to list both running and exited containers?

answer:

docker ps -a
or
docker container ls -a

question id: 81b168e4-e516-499f-9259-5262a2c85d22


### How to remove specific image?

`docker image rm your_image`

question id: 675e50ad-2188-4946-9742-8f56b7b48373


### What's the command to build a docker container from a Dockerfile?

answer:
`docker build -t container-name .`

where -t is a flag to give your container a name and . means the directory with dockerfile is

question id: fc4bded9-19af-4c14-ad5b-f1b4c017b574


### What's the command for downloading an image from DockerHub?

answer:

`docker pull image-name`

question id: 67490d5f-8f3c-4e89-b591-d551ab04d675


### How to run your image in an interactive mode?

answer:
`docker run -it your-img-name`

question id: bf73b5f7-74cf-4d86-bd0d-b095e9ca3dc8


### How to set build-time variables?

`--build-arg YOUR_KEY=YOUR_VALUE`

e.g

`--build-arg GITLAB_LOGIN="hacker666`

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


### How to exclude files from copying from source folder by docker to your new container?

answer:

You need to create a .dockerignore file and list there files and directories in it
if you want to skip them while copying.

# .dockerignore
.python-version
some_folder/

question id: 5e5ca865-57b0-45b2-a521-03cb4538d3f6


### How to login in container as a root user?

answer:

`docker exec -it -u 0 container-name sh`

question id: 028cd4c3-39d8-438a-8d80-ab136f9fcacb


### How to get rid of dangling images?

answer:

`docker image prune`

question id: ff488396-0e44-4837-98ae-e1c7cbecf0aa


### How to tag an image while building it?

answer:

`docker build -t image-name:image-tag .`

e.g.

`docker build -t my_app:0.17.1 .`

question id: b382f92b-4832-4215-8b95-8309cbeaafc4


### How to tag existing image?

answer:
`docker image tag image-id name:tag`
e.g.
`docker image tag lfl3lf my-app:0.17.1`

question id: 5c117236-bd4e-4fba-aeac-6993f13ac314


### How to make latest tag point to the last version of your image?

answer:

You have to do it manually, just choose an image by id and tag it with 'latest'
like 

`docker image tag kjk343l my-app:latest`

question id: 89209959-6ae6-4b2f-93bd-e2ad86f0def1


### How to push your image to Dockerhub?

answer:

0. Create a repo at Dockerhub at https://hub.docker.com/

1. Tag your image with `dockerhublogin/image-name:tag`

2. Use command `docker push dockerhublogin/image-name:tag` to push the image to the repo

e.g. `docker push banicni/my-app:1`

question id: 06b20d97-8008-49a9-9936-a5fce2b13197


### How to start a container in a detached mode?

answer:

`docker run -d image-name`

where `-d` means detached mode

question id: 78522366-b461-47c1-837b-42f2e1d2c58b


### How to give your container a name when you are creating it?

answer:

`docker run --name foo img-name`

e.g.

`docker run --name my-redis redis`

question id: 95b18fdb-cff0-4114-8ea8-f3978ca9c6d6


### How to watch logs of a specified container?

answer:

- `docker logs container-id`

- `docker logs -f container-id` to follow the logs of the container

- `docker logs -f -t container-id` to get logs with timestamps

question id: e863e79f-58bb-4b55-9aff-0e82cee5e54a


### How to map a port of a container to a port of a host?

answer:

`docker run -p host_port:container_port --name myapp myimage`

e.g.

`docker run --name redis -p 6379:6379 -d redis`

question id: 7552cd3e-2291-46ec-9840-08de42b6b806



### How to execute commands inside a container?

answer:

`docker exec -it container-name/id sh`

e.g.

`docker exec -it my_postgres sh`

Instead of sh can be any shell that is installed in your container. 
There could be no shell at all, so you have to install one during building the image

question id: 614bb802-f7cb-4b22-8076-a2f08a27b0fe


### What's the difference between `docker run` and `docker start` commands?

answer:
`docker run` is for creating a new container from an image
`docker start` is for starting already existing stopped container

question id: 1b75cc3c-5ea5-4c14-89ae-d9f2d2b0c31e


### What is the command to create a new container from an image?

answer:
`docker run`

question id: b39644cc-8df0-41d7-837d-4f9767d567c1


### What is the command to start a stopped container?

answer:
`docker start`

question id: 1bf53fc4-d68b-4cec-8a61-bce2a9bae99d


### What is `docker run` command for?

answer:

For creating a new container from an image

question id: c2587cf4-d304-4be6-80b8-0d63ddaf67f1


### What is `docker start` command for?

answer:

For starting a stopped container

question id: 3536b8f4-f1a2-4f68-a10c-56d6226e9766


### How to remove a container?

answer:

`docker container rm container-id`

question id: 


### How to remove a running container?

answer:
Either stop container then remove it, or force remove it like this:

`docker container rm -f container-id`

or shorter:

`docker rm -f container-id`

question id: 6ace3538-b85d-4ebb-8920-1b5f156db225


### What is a Volume?

answer:

It's a storage outside of a container. It can be a directory on a host on at a cloud.

question id: fbf6bf7e-0609-4fe7-93f7-98097468722b


### How to list volumes?

answer:

`docker volume ls`

example of an output:
```
DRIVER    VOLUME NAME
local     0a0054f20996224fbd87a2afc2a1c19f323c87945c8a04767e6febf375b59455
local     2d2f3ab41514e33a7586179c83f7e8cbe81aa577b2edb7fdcc3a9feadeddee95
local     2dc2538ee600528a63a5dab84d8b4e6d05776c9728c651085450b70d286c5290
local     40c47337464263451e8f0dc61fe08cbb8d0543ffcae96c521f1916912bef8366
local     57a10c0b8b167850f5e620f0b16ff2a55d41096feee84f059f4578517bf602cb
local     83f03492cb39d52ba8e06ac338d64db303f007a00312841c096d8f59202c5930
local     2501de4522213cf4e1bff231b3af02e5485a34306920efcf6f746cf31cdf0879
local     06080c8d0214afbfd1f29346e7c94a37af0ee477d14d5de71146c85e9f4391ce
local     a67749c04ee2613e115af3f8c370a50265c90b7c056df4f6920a10b892b40a8f
local     abd19857ab06d3a89146427036a18cb0eb19d443b1f5237234d05210f13750c5
local     dd8f83ba29ecef04e03b1f093239b9520b1de142afee7081327e4b2da3cf98f6
local     df61e274299665f459549ef7c15968e1a6232085bcf97271c2f698ac53ebdc7c
local     mb_task_assignment_mobility_house
local     mobility_house_mobility_house
```

question id: 780df520-e6d9-44b9-bbe3-6e1fa4377361


### How to create a volume?

answer:

`docker volume create vlm-name`

question id: d64cc5c8-dd79-4922-b092-22bab5038892


### What does this command `docker volume create` do?

answer:


It creates a new volume. Volume is a directory on the host or in a cloud. So, creating a volume, you create
a directory where files of your container can be stored. In order to use this volume, you
need to map it to the folder within file system of your container when you create a container.

question id: 7012112d-c42e-4c86-858b-ef2b35e94183


### How to inspect a volume?

answer:

`docker volume inspect volume-name`

Example of output:

```
[
    {
        "CreatedAt": "2023-03-12T23:38:30+04:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/0a0054f20996224fbd87a2afc2a1c19f323c87945c8a04767e6febf375b59455/_data",
        "Name": "0a0054f20996224fbd87a2afc2a1c19f323c87945c8a04767e6febf375b59455",
        "Options": null,
        "Scope": "local"
    }
]
```

question id: 95d14b3f-f4a7-4883-8c9e-b4020b9868ad


### How to create a container with a volume?

answer:

`docker run -v volume-name:/path/within/your/container`

Where:
- `volume-name` it's a name of a volume: you can use existing
one otherwise docker will create a new one
- `/path/within/your/container` is a path on filesystem of your container which will be mapped to the folder of the volume
  
So, whatever you or your app in a container puts into `/path/within/your/container`, will appear on the host system in a folder of
specified volume

question id: 021fa458-4c10-4a71-b0cd-5f576016ab2d


### How to copy a file from container to the host?

answer:

`docker cp container-id:/path/on/container/file.txt .` will copy 
the file from your container to the current working directory of your host

question id: 92ef84f4-6780-4a79-a3c0-c244cb9c8666


### How  to copy a file from a host filesystem to a container?

answer:

`docker cp /path/to/file/on/host.txt container-id:/path/on/container`

question id: b3b001fb-e32c-4635-b257-48bea077cc1c


### How to instantly get any change in source code in a container?

In a production environment you always should rebuild your image, tag it properly and so on.
However, for development, there is quite more quick way to get any changes in your source code
in container. How would you do it?

answer:
You can map a directory on your host where your project is to a source directory in your container,
so as soon as you edit the source code on your host, it immediately ends up in your container
without rebuilding the image, without creating new container. There is an example:

`docker --name myapp -d -p 3000:3000 -v /path/on/host/my/app:/source/directory/in/container myapp`

Yes, instead of a named volume you can denote just a path on your machine.

question id: 8da2ce29-ac58-4701-853e-659c5543114d


### Why to use two-stage dockerfile builds?

answer:

To reduce the size of resulting container

question id: 1c007fa0-3ca6-4e55-b888-0cc1f0f44a96

