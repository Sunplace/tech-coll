from kafka import KafkaAdminClient
from kafka.admin import ConfigResource, ConfigResourceType
import ssl
import logging
logging.basicConfig(level=logging.DEBUG)

try:
    #topic = "topic-name"
    security_protocol = "SSL"
    ssl_cafile = "./cluster-ca.crt"
    ssl_certfile = "./user.crt"
    ssl_keyfile = "./user.key"
    #ssl_password = "xxxxxxxxxxxxx"

    client = KafkaAdminClient(bootstrap_servers='kafka.app.com:443',
                              ssl_certfile = ssl_certfile,
                              ssl_keyfile = ssl_keyfile,
                              #ssl_password = ssl_password,

                              security_protocol=security_protocol,
                              ssl_check_hostname=True,
                              ssl_cafile = ssl_cafile )

    #KAFKA_TOPIC = "topic-name"
    #configs = client.describe_configs(config_resources=[ConfigResource(ConfigResourceType.TOPIC, KAFKA_TOPIC)])
    KAFKA_BROKER = "0"
    configs = client.describe_configs(config_resources=[ConfigResource(ConfigResourceType.BROKER, KAFKA_BROKER)])
    print(configs)

except Exception as e:
    print(e)