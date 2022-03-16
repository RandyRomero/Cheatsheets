### Problem: "selector does not match template labels"

Something like:
Deployment.apps "notifications" is invalid: spec.template.metadata.labels: 
Invalid value: map[string]string{"io.kompose.service":"notifications"}: `selector` does not match template `labels`

It means that you tried to change lables, but you can, they are immutable.

You have to leave them as they are, or remove deployment of your app and recreate it with new labels.

https://stackoverflow.com/questions/53304461/error-selector-does-not-match-template-labels
https://github.com/kubernetes/kubernetes/issues/26202

question id: c84ab21b-1060-49d6-b097-91e0eb95dd12


