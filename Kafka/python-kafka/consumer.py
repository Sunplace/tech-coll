from kafka import KafkaConsumer
topic = "test"
sasl_mechanism = "SCRAM-SHA-256"
username = "user1"
password = "HTUaoeblTy"
security_protocol = "SASL_PLAINTEXT"

consumer = KafkaConsumer(topic, bootstrap_servers='172.18.0.4:31749',
                          security_protocol=security_protocol,
                          sasl_mechanism = sasl_mechanism,
                          sasl_plain_username = username,
                          sasl_plain_password = password)

for msg in consumer:
    print (msg)