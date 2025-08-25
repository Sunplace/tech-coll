# Elasticsearch Extra

## how to calculate elasticsearch index size
https://discuss.elastic.co/t/get-index-size-result/138228

## node role
https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-node.html

## size shard
https://www.elastic.co/guide/en/elasticsearch/reference/current/size-your-shards.html

## elasticsearch plugin
https://github.com/ElasticHQ/elasticsearch-HQ

https://github.com/lmenezes/cerebro

## indice size，total size
```
GET logstash-ocp-dev01-audit-2024.09.02/_stats
GET _cat/indices
GET _stats/store
GET logstash*/_stats/store
```

## es disk space usage
https://stackoverflow.com/questions/29417830/elasticsearch-find-disk-space-usage

https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-nodes-stats.html


## es cerebro
https://github.com/lmenezes/cerebro/blob/main/conf/application.conf

https://github.com/lmenezes/cerebro/issues/388

https://github.com/lmenezes/cerebro/issues/473

https://github.com/lmenezes/cerebro/issues/441

## es lucene 语法
https://lucene.apache.org/core/2_9_4/queryparsersyntax.html

## es watermark
https://www.elastic.co/guide/en/elasticsearch/reference/current/fix-watermark-errors.html

https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-cluster.html#disk-based-shard-allocation

https://www.elastic.co/guide/en/elasticsearch/reference/current/index-modules-blocks.html

## index rollover manually
https://www.elastic.co/guide/en/elasticsearch/reference/8.17/indices-rollover-index.html

## how to check iptables or ipvs
https://stackoverflow.com/questions/66746018/how-to-find-which-mode-kube-proxy-is-running-in

https://stackoverflow.com/questions/73092627/kubernetes-kube-proxy-modewhich-one-ipvs-iptables-or-userspace

## 插件离线安装
```shell
elasticsearch-plugin install  file:///tmp/elasticsearch-analysis-ik-8.5.2.zip
```