# Rancher

## run on docker of a single node
docker run -d --restart=unless-stopped -p 80:80 -p 443:443 -v /docker_volume/rancher_home/rancher:/var/lib/rancher -v /docker_volume/rancher_home/auditlog:/var/log/auditlog --name rancher --privileged=true rancher/rancher:v2.10.0

## debug verification error" while trying to verify candidate authority certificate "kube-ca"
https://github.com/rancher/rancher/issues/14479

## RKE1 and RKE2
https://ranchermanager.docs.rancher.com/how-to-guides/new-user-guides/launch-kubernetes-with-rancher/rke1-vs-rke2-differences

## Rancher vs. RKE
https://www.suse.com/c/rancher_blog/rancher-vs-rke-what-is-the-difference/

## K3s and RKE2
https://www.suse.com/c/rancher_blog/when-to-use-k3s-and-rke2/

## k3s private registry
https://docs.k3s.io/installation/private-registry