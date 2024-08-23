# K8s tricks

## get pod name by ip
kubectl get --all-namespaces  --output json  pods | jq '.items[] | select(.status.podIP=="10.22.19.69")' | jq .metadata.name