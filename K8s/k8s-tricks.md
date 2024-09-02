# K8s tricks

## get pod name by ip
kubectl get --all-namespaces  --output json  pods | jq '.items[] | select(.status.podIP=="10.22.19.69")' | jq .metadata.name

## get pod event
kubectl get event --namespace abc-namespace --field-selector involvedObject.name=my-pod-zl6m6