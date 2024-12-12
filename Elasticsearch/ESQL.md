# ESQL

## ESQL examples

### ES|QL
from logstash-ocp-prd01-application-2024.09.12 | 
where kubernetes.namespace_name == "prd-finance-bin" |
where message like "*取数*"
| GROK message ":%{NUMBER:test:float}s"
| keep test
| limit 500
| sort test desc
| stats max(test)

### 2
from logstash-ocp-*-infrastructure-* | 
where kubernetes.namespace_name.keyword == "openshift-dns"
| where message like "*backend-listener*"
| limit 500000
| GROK message "%{IPV4:test}"
| keep test
| stats count(test) by test

### 3
from logstash-ocp-*-infrastructure-* | 
where kubernetes.namespace_name.keyword == "openshift-dns"
| where message rlike ".*backend-listener.*"
| limit 500000
| GROK message "%{IPV4:test}"
| keep test
| stats count(test) by test