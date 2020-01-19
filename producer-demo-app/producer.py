import sys

import config
from confluent_kafka.cimpl import Producer

conf = {'bootstrap.servers': config.resolve_config("BROKER")}


def on_delivery(err, msg):
    if err:
        sys.stderr.write('%% Message failed delivery: %s\n' % err)
    else:
        sys.stdout.write('%% Message delivered to %s [%d] @ %d\n' %
                         (msg.topic(), msg.partition(), msg.offset()))


producer = Producer(**conf)


def produce(message, topic=None, count=1):
    _topic = topic or config.resolve_config("CONSUMER_TOPICS")
    try:
        for i in range(count):
            producer.produce(_topic, message + ": " + str(i), on_delivery=on_delivery)
    except Exception as e:
        sys.stderr.write("Exception " + e.__class__.__name__ + " :: " + e)
