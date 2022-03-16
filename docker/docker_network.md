Viewing networks
docker network ls


### How to create network for containers to be able to communicate with each other? 

(it's of a bridge type by default)

docker network create my-network-name

question id: 8cf0fe9e-9b9e-4d33-9283-f17626574199


### How to inspect a network? 

docker network inspect name

question id: 5b9f8ccb-3733-4f83-a133-b15665b1317b



=====================================================================================================================

How to add several containers in one network:
1. Create a new network
docker network create my-net

2. Run a container adding it to the net:
docker run -d --name blabla --net my-net -p 5432:5433 other stuff... (-p the left one for your network, the right one is if you want to get access from the outside)

Or add existing container
docker network connect my-net my-container

3. Don't forget to inspect containers network to figure out their IPs