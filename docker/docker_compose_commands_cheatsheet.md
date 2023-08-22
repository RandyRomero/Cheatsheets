### What does `docker-compose build` does?

answer:
It builds and/or pulls all images specified in your docker-compose.yml file, so they are ready to run

question id: a796bf08-d6ad-4bcf-b2dd-a2fe7d2acd41


### How do you start all containers defined in docker-compose.yml?

answer:

First of all, you need to change you working directory to one which contains 
your docker-compose.yml. Then run a command:

`docker-compose up`

`docker-compose up -d` if you want to start container in detached mode

`docker-compose up --build` if you want to rebuild all images and then start

question id: cbd76e38-e9b9-4935-9d11-5200ac2262dc


### How to check what containers are running?

answer:

`docker-compose ps`

question id: 308c612f-0392-4b22-97cb-62aa78220b78


### What is a command to stop all containers of a particular docker-compose.yml?

answer:

`docker-compose down`

question id: 3ebeed15-3ec2-4cc4-8cec-bd51802baef8


### Can you view logs of all containers of one docker-compose?

answer:
`docker-compose logs`

P.S. Execute command for the same folder where your docker-compose.yml is.

question id: 27028ba2-d92f-4b6a-981c-6b0ccb5c4ba4


