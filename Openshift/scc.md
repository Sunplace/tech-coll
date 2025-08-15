# scc

https://developer.ibm.com/learningpaths/secure-context-constraints-openshift/scc-tutorial/

https://docs.okd.io/3.11/admin_guide/manage_scc.html

```shell
oc create serviceaccount redis -n clm-poc
oc adm policy add-scc-to-user privileged system:serviceaccount:clm-poc:redis
```