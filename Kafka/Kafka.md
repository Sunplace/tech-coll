# Kafka

## Kafka introduction
https://medium.com/nerd-for-tech/a-basic-introduction-to-kafka-a7d10a7776e6

https://medium.com/javarevisited/kafka-partitions-and-consumer-groups-in-6-mins-9e0e336c6c00

## kafka python sdk
https://kafka-python.readthedocs.io/en/master/index.html

## kafka c/c++ sdk
https://github.com/confluentinc/librdkafka

## kafka client tools: Kcat, plumber, kafka-ui, kafkatool
https://github.com/provectus/kafka-ui

https://github.com/edenhill/kcat

https://github.com/streamdal/plumber

https://www.kafkatool.com/

## Kafka consumer group
https://medium.com/javarevisited/kafka-partitions-and-consumer-groups-in-6-mins-9e0e336c6c00

https://codingharbour.com/apache-kafka/what-is-a-consumer-group-in-kafka/

it is mandatory to specify Kafka which consumer would belong to which consumer group. If you do not set the consumer group id in your app, you will get an exception. If you start a consumer to consume from a topic using the Kafka CLI command, then a new random consumer group is created with the name console-consumer-<some_random_number> and the consumer automatically falls under this consumer group.

## Can single consumer read from multiple partitions of a kafka topic?
https://stackoverflow.com/questions/69502892/can-single-consumer-read-from-multiple-partitions-of-a-kafka-topic

## kafka python auto.offset.reset
https://quix.io/blog/kafka-auto-offset-reset-use-cases-and-pitfalls

## reset_kafka_consumer_group_offset
https://gist.github.com/marwei/cd40657c481f94ebe273ecc16601674b

## ssl.client.auth=required
https://stackoverflow.com/questions/49063771/what-does-ssl-client-auth-specify

## kafka message retention time
https://www.baeldung.com/kafka-message-retention

## keystore and truststore
https://aiven.io/docs/products/kafka/howto/keystore-truststore

https://www.baeldung.com/spring-boot-kafka-ssl

https://medium.com/@ahosanhabib.974/enabling-ssl-tls-encryption-for-kafka-with-jks-8186ccc82dd1

https://kafka.apache.org/documentation/streams/developer-guide/security.html

https://stackoverflow.com/questions/72904899/how-can-i-use-keystore-jks-and-truststore-jks-files-for-kafka-python-ssl-authent

https://stackoverflow.com/questions/42276672/using-apache-kafka-in-ssl-mode

https://github.com/edenhill/kcat/issues/309

## kafka helm chart bitnami
https://github.com/bitnami/charts/tree/main/bitnami/kafka/#installing-the-chart

## topic, partition, offset
https://www.geeksforgeeks.org/topics-partitions-and-offsets-in-apache-kafka/

https://stackoverflow.com/questions/57054843/kafka-offset-and-partition-identification

## topic retention time
https://www.baeldung.com/linux/kafka-view-topic-retention

## log retenion hours, topic retention time
https://www.baeldung.com/kafka-message-retention

## Difference between delete.retention.ms and retention.ms
https://forum.confluent.io/t/difference-between-delete-retention-ms-and-retention-ms/10613

## kafka lag
https://www.redpanda.com/guides/kafka-performance-kafka-lag

## kafka storage
https://strimzi.io/blog/2021/12/17/kafka-segment-retention/
https://stackoverflow.com/questions/74971714/how-often-does-kafka-check-to-cleanup-the-segment-files
https://www.baeldung.com/kafka-message-retention

```
共同控制消息保持的几个参数：（具体作用机制，参考如上文档。）
server层：
log.retention.ms log.retention.hours log.retetion.minutes
topic层：
retention.ms retention.bytes
cleanup.policy
delete.retention.ms
segment.bytes
segment.ms
```

## how to list kafka producers
it's impossible
https://stackoverflow.com/questions/60318519/how-to-list-all-producers-of-a-kafka-cluster

## kafka docker compose deployment
https://www.confluent.io/blog/how-to-use-kafka-docker-composer/

https://github.com/conduktor/kafka-stack-docker-compose/blob/master/zk-single-kafka-single.yml

https://github.com/bitnami/containers/blob/main/bitnami/kafka/docker-compose.yml

https://developer.confluent.io/confluent-tutorials/kafka-on-docker/

## kafka operator
https://strimzi.io/docs/operators/latest/deploying#kafka-cluster-str

https://strimzi.io/quickstarts/

## kafka browser
offset explorer

## kafka 命令行操作
```shell
# 获取topic
./bin/kafka-topics.sh --bootstrap-server 10.1.1.145:9092 --list

./bin/kafka-topics.sh --bootstrap-server 10.1.11.18:9092 --list

# 查看topic offset 详情
bin/kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 10.1.1.145:9092 --topic omdb_endpoint

# create topic
bin/kafka-topics.sh --create --topic omdb_endpoint_syj_test --bootstrap-server 10.1.1.145:9092

# produce message
bin/kafka-console-producer.sh --topic omdb_endpoint_syj_test --bootstrap-server 10.1.1.145:9092

# consume message
bin/kafka-console-consumer.sh --bootstrap-server 10.1.1.145:9092 --topic omdb_endpoint --offset 52436266 --partition 5
```