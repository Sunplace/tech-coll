# Rancher

## run on docker of a single node
docker run -d --restart=unless-stopped -p 80:80 -p 443:443 -v /docker_volume/rancher_home/rancher:/var/lib/rancher -v /docker_volume/rancher_home/auditlog:/var/log/auditlog --name rancher --privileged=true rancher/rancher:v2.10.0

## debug verification error" while trying to verify candidate authority certificate "kube-ca"
https://github.com/rancher/rancher/issues/14479