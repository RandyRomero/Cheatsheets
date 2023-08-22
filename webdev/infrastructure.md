



### What are microservices? 

Microservices - is a design approach to complex 
programs or services in breaking the system into 
independent small services and components.

question id: b1d47ffc-b19e-4152-9b5e-43612587303a


### What is Kubernetes (k8s)?

Kubernetes (k8s) is a tool for management and launching of 
containerized apps

question id: af2878c3-0bfb-404e-9703-6bd3dd0c51dd


### What is Serverless? 

Serverless computing (or serverless for short), is an execution model 
where the cloud provider (AWS, Azure, or Google Cloud) is responsible 
for executing a piece of code by dynamically allocating the resources. 
And only charging for the amount of resources used to run the code.

The code is typically run inside stateless containers that can be 
triggered by a variety of events including http requests, database events, 
queuing services, monitoring alerts, file uploads, scheduled events (cron 
jobs), etc. 

The code that is sent to the cloud provider for execution is
usually in the form of a function. Hence serverless is sometimes referred 
to as “Functions as a Service” or “FaaS”.

Our functions are typically run inside secure (almost) stateless containers.
This means that you won’t be able to run code in your application server 
that executes long after an event has completed or uses a prior execution 
context to serve a request. You have to effectively assume that your 
function is invoked in a new container every single time.

https://serverless-stack.com/chapters/what-is-serverless.html

question id: b19d3b67-bb98-47fa-a6af-1b45d0b262a5



### What are Kubernetes pros over Serverless? (3)   

- easy to test because containers are run on the same platform where they are deployed
- latency is lower because containers work all the time, where they are destroyed in Serverless for short inactivity
- suitable for long-standing tasks

question id: c020fc7c-a427-4273-94b9-666c3d9bbbe2

### What are Kubernetes cons over Serverless? (2)  
- you need an engineer or a team of engineers to set up kubernetes, scaling, every container etc
- you have to acquire some skills to build proper containerized apps

question id: b876da96-854b-417d-9b77-93188bd17033


### What are Serverless pros over Kubernetes? (4)

- makes it easier to start your project very in no time, especially if you don't have people with operational experience (network, storage, monitoring, etc.)
- if you have significant drop in traffic/workload from time to time (like Woosh doesn't work during winter in Moscow) and you want to pay less to cloud provider during times like these
- don't need even to make containers by yourself, only write features
- that you don't have to set up autoscalling, for you it just works automagically, providing better accessibility

question id: 72b0701c-3707-4016-9660-c746e14afe37


### What are Serverless cons over Kubernetes? (4)

- not suitable for very long-running computing operations (functions have timeouts, like 15 minutes, but still)
- less responsive (if function is not used for some time, container with it will be desrtoroed, it will require time to start it again, or you can restart it with cron every so often)
- difficult to test and debug because of challenges with the backend environment replication on the local environment

question id: 2aa9466a-045f-4997-877e-01818da99b24

