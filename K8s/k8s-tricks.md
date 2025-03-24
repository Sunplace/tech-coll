# K8s tricks

## get pod name by ip
kubectl get --all-namespaces  --output json  pods | jq '.items[] | select(.status.podIP=="10.22.19.69")' | jq .metadata.name

## get pod event
kubectl get event --namespace abc-namespace --field-selector involvedObject.name=my-pod-zl6m6

## How to find out what podcidr is assigned to each node by calico CNI in kubernetes
https://stackoverflow.com/questions/65301771/how-to-find-out-what-podcidr-is-assigned-to-each-node-by-calico-cni-in-kubernete

kubectl get ipamblocks.crd.projectcalico.org 

kubectl get ipamblocks.crd.projectcalico.org -o jsonpath="{range .items[*]}{'podNetwork: '}{.spec.cidr}{'\t NodeIP: '}{.spec.affinity}{'\n'}"

## k8s get service/pod cidr
https://stackoverflow.com/questions/44190607/how-do-you-find-the-cluster-service-cidr-of-a-kubernetes-cluster

kubectl cluster-info dump | grep -m 1 cluster-cidr

kubectl cluster-info dump | grep -m 1 service-cluster-ip-range

echo '{"apiVersion":"v1","kind":"Service","metadata":{"name":"foo"},"spec":{"clusterIP":"1.1.1.1","ports":[{"port":443}]}}' | kubectl apply -f - 2>&1 | sed 's/.*valid IPs is //'