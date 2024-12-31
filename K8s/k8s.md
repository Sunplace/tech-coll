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

