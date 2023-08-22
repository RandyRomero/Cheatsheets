## What you need to do you to make your app production ready?

- use flag debug=False in django or other applications so they do not return details errors as a response
- use web server app (gunicorn, nginx) instead of django own server
- keep secres in k8s or whatever instead of locally
- setup propper logging, because it would be hard to debug otherwise
- setup alerting like Sentry
- consider your workload properly, set up autoscaling accordingly
- if the workload is high and you use more than one instance of your app (in k8s), make sure they can work together (for example, save cache in Redis, not just in memory)

question id: 8bca61fb-894d-409a-bab3-5dc8972deef5