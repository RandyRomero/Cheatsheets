### Cronjobs: Get a list of existing cronjobs
`kubectl -n namespace get cronjobs`

question id: c3f2dafe-4bf5-40df-a4ba-ee3c40bbe490


### Cronjobs: How to trigger a Kubernetes cronjob manually
`kubectl create job --from=cronjob/<name of an existing cronjob> <name of a new job>`

for example:

`kubectl -n namespace create job --from=cronjob/vertica-service-check-offer-state vertica-service-check-offer-state-manual-001`

question id: 9514f5cf-6899-4b82-ade1-36f4dd2c7406


### Cronjobs: How to get an info about certain cronjob?

`kubectl -n prod get cronjob job-name (-o yaml)`

question id: 02841d04-7c8c-45be-aebe-ac758b73d6ca


### Cronjobs: How to suspend cronjob for a while?

`kubectl patch cronjobs <job-name> -p '{"spec" : {"suspend" : true }}'`

https://kubernetes.io/docs/tasks/job/automated-tasks-with-cron-jobs/#suspend

question id: 3ab7884d-90df-445e-a08e-d89b1df20fdd


### Cronjob: How to delete a cronjob? 

```
kubectl -n prod delete cronjob-name
```
question id: 93f8758c-790b-4f99-a208-fbd90f38ab23



### Pods: Get pod info (like envs for example)
`kubectl -n prod describe pod your_pod_name`

question id: ce54e087-8eb2-4bf9-b7d0-eafbe7e6319a


### Pods: Get list of pods
`kubectl -n namespace get pods (| grep your_pod_name)`

question id: 4379defb-3508-47b8-8501-df72972e893b


### Pods: How to delete a pod (to make get it restarted)
`kubectl -n namespace delete pod your_pod_name`

question id: 1f0062db-0fe0-4580-bb81-25ab0c30c60d


### Pods: How to stop a pod for a while?
You can scale it down to 0
`kubectl -n prod scale --replicas=0 deployment/name-of-your-deployment

question id: 91c1962f-c0de-4f08-b165-4fa8e77907c1



### Pods: how to check logs of a pod?

`kubectl -n namespace logs your_pod_name`

It works even for failed or stopped pod

question id: 172543e1-0861-47ea-b666-ece8d359a3f4


### Deployment: How to list all deployments? 
`kubectl -n prod get deployments`

question id: 418a6832-ba7f-40d3-9438-9a916f388249


### Secrets: Get a list of secrets' names
`kubectl -n stage/prod get secrets`

question id: 771e1a14-6c05-42e9-adc3-e59dd1e45238


### Secrets: how to get a specific secret by name?
`kubectl -n stage/prod get secret your-secret-name -o yaml`

question id: a3cc7e13-0ee2-4304-a23f-cad93c8e2ff3


### Shell: Start a shell in a running pod based on alpine
`kubectl -n namespace exec --stdin --tty your_pod_name -- /bin/ash`

question id: b8d6e46d-642f-4122-aa9a-d2dab178c5de


### How to connect to rabbitmq on stage
`kubectl port-forward svc/rabbitmq-2-stage-rabbitmq-svc -n stage 15672`

question id: ab5d8b5d-0aff-45a2-835a-9cc56fde583a

### How to connect to rabbitmq on prod
`kubectl port-forward svc/rabbitmq-rabbitmq-svc --namespace prod 15672`

question id: 148ca549-abdc-4652-a8b9-f5b3300eea0e



### How to connect to redis-cli?

```shell
# amo
gcloud compute ssh telegram-proxy -- -N -L 6379:172.22.211.188:6379 

# auth
gcloud compute ssh telegram-proxy -- -N -L 6379:10.25.78.91:6379

https://console.cloud.google.com/memorystore/redis/instances?project=plaster-project

# then redis-cli from another terminal
```

question id: 17816fe6-e7d6-4cef-9eee-ac2a45312dcc


## How to get a list of configmaps? 

```
kubectl -n namespace get configmaps
```

question id: 42c7b69c-d07b-44ce-8b1f-b12c14eea3bd


## How to read a specific configmap?

```
kubectl -n stage get configmap auth-redis -o yaml
```

question id: b49e8111-8cfa-4339-a392-32b59f17a95b


### How to create configmap from literals?

```
kubectl -n namespace create configmap some_name --form-literal REDIS_DB="6" --from-literal REDIS_PORT="6379"
```

question id: b32f7fda-e0d0-48a7-8c1f-c7244ac4c5e8


### How to delete a configmap?

```kubectl -n namespace delete configmap name-of-configmap```

question id: 1a13785c-77cc-481f-8f92-b6a7e043dd5c


### How to add new key-value pair to a scpecific secret?

```
kubectl -n stage get secret your_secret -o json | jq '.data["your_key"]="value in base64url"' | kubectl apply -f -
```

question id: 18e62958-21f9-4d1c-9ff6-20d35f0d0565


### How to set env in deployment manually?

`kubectl -n stage set env deployment/deployment-name MY_ENV=MY_VALUE`

https://stackoverflow.com/questions/57601495/how-to-leverage-kubectl-patch-deployment-to-update-an-environment-variable

question id: 9e6465d4-e2ed-4f1c-8bdd-35c7bc54bffe


### How to set env in cronjob manually?

`kubectl -n prod set env cronjob cj-name KEY=VALUE`

for example:

`kubectl -n prod set env cronjob battleground-check-db-sanity DB_NAME=battleground`

question id: 3ed94c53-e880-4290-a819-c9d802a9c3fd
