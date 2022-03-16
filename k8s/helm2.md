### How to rollback to the previous release if something went wrong?

0. get the last version of release of your interest

```shell
helm list | grep your_release_name
```

1. rollback to the previous version

```shell
helm rollback your_release_name <last version> (where last version is current version - 1)
```

for example

```
ayamikheev@ryzen:~$ helm list | grep graph

graph-gateway                           222             Mon Mar 15 18:40:24 2021        DEPLOYED        kubernetes-0.0.1                        prod                                                                                                                            
stage-graph-gateway                     313             Wed Mar 31 12:00:49 2021        DEPLOYED        kubernetes-0.0.1                        stage                                                                                                                           

ayamikheev@ryzen:~$ helm rollback stage-graph-gateway 312
Rollback was a success.

ayamikheev@ryzen:~$ 

```

question id: c8a2f276-554e-4060-bc31-f894dd294a2a


### How to get history of releases of specific release?

```
helm history your-release-name
```

question id: e4598042-6f97-4f68-8904-6f96386fcfc8
