### Problen when executing any command

Unable to connect to the server: error executing access token command "/snap/google-cloud-sdk/186/bin/gcloud config config-helper --format=json": err=fork/exec /snap/google-cloud-sdk/186/bin/gcloud: no such file or directory output= stderr=

Decision:
0. gcloud container clusters list  // get cluster name and region from here

1. gcloud container clusters get-credentials your_cluster_name --region=your_region 