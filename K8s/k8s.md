# K8s 

## allowPrivilegeEscalation
https://www.tigera.io/learn/guides/kubernetes-security/kubernetes-security-context/

https://medium.com/pareture/how-allowprivilegeescalation-works-in-kubernetes-ce696494f87b

https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

## security context
https://kubernetes.io/docs/tasks/configure-pod-container/security-context/

https://github.com/rook/rook/issues/11755

## k8s 版本选择
https://kubernetes.io/releases/version-skew-policy/

https://kubernetes.io/releases/patch-releases/

https://endoflife.date/kubernetes

https://learn.microsoft.com/en-us/azure/aks/supported-kubernetes-versions?tabs=azure-cli

https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html

https://cloud.google.com/kubernetes-engine/docs/release-schedule

https://www.alibabacloud.com/help/en/ack/ack-managed-and-ack-dedicated/user-guide/support-for-kubernetes-versions

## containerd 版本选择
https://containerd.io/releases/

## containerd linux kernel version compatibility
https://github.com/containerd/containerd/blob/main/README.md#runtime-requirements

## k8s Linux Kernel Version Requirements
https://kubernetes.io/docs/reference/node/kernel-version-requirements/

## k8s static pod
https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/

## containerd rhel8.6 docker repository
https://github.com/docker/cli/issues/5364

## k8s container runtime storage configuration
https://kubernetes.io/blog/2024/01/23/kubernetes-separate-image-filesystem/

## k8s Liveness, Readiness, and Startup Probes
https://kubernetes.io/docs/concepts/configuration/liveness-readiness-startup-probes/

https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

## k8s port forward
https://kubernetes.io/docs/reference/kubectl/generated/kubectl_port-forward/

https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/

## k8s get service/pod cidr
https://stackoverflow.com/questions/44190607/how-do-you-find-the-cluster-service-cidr-of-a-kubernetes-cluster

kubectl cluster-info dump | grep -m 1 cluster-cidr

kubectl cluster-info dump | grep -m 1 service-cluster-ip-range

## k8s iptables vs ipvs
https://learncloudnative.com/blog/2023-05-31-kubeproxy-iptables

https://github.com/kubernetes/kubernetes/blob/master/pkg/proxy/ipvs/README.md

## allow scheduling of pods to k8s master
https://stackoverflow.com/questions/43147941/allow-scheduling-of-pods-on-kubernetes-master

## list taint of k8s node
https://stackoverflow.com/questions/43379415/how-can-i-list-the-taints-on-kubernetes-nodes

## delete k8s cluster
https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/#tear-down
```shell
kubeadm reset
iptables -F && iptables -t nat -F && iptables -t mangle -F && iptables -X
ipvsadm -C
```

## clean flanne cni
https://stackoverflow.com/questions/46276796/kubernetes-cannot-cleanup-flannel

```shell
rm -rf /var/lib/cni/
rm -rf /var/lib/kubelet/*
rm -rf /run/flannel
rm -rf /etc/cni/
ifconfig cni0 down
brctl delbr cni0
ip link delete cni0
ip link delete flannel.1
```

## kubectl create docker registry config
```shell
kubectl create secret docker-registry quay-secret \
  --docker-server=quay.globalapp.mindray.com \
  --docker-username='xxx' \
  --docker-password='xxx' -n sunyangjian
```

## k8s hostip, hostport
https://stackoverflow.com/questions/63691946/kubernetes-what-is-hostport-and-hostip-used-for

https://kubernetes.io/docs/concepts/configuration/overview/

https://www.fairwinds.com/blog/tutorial-how-to-check-host-port-configuration

## 证书超期检查
```shell
kubeadm certs check-expiration
```

## How to Make Kubectl Exec Run Against Multiple Pods
```shell
kubectl get pods -o name | xargs -I{} kubectl exec {} -- <command goes here>
```