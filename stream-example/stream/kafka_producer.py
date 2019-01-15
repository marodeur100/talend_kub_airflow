#!/usr/bin/python
"""Simulates user activities of a websites and sends the values to Kafka """
import time
import json
import argparse
import random
import datetime
from kafka import KafkaProducer

# Dummy user data
actions = ['login', 'checked_balance', 'cash_transfered',
           'creditcard_payment', 'contacted_support', 'logout']
users = [('1', 'DarthVader'), ('2', 'C-3PO'), ('3', 'Chewbacca'), ('4', 'HanSolo'), ('5', 'LukeSkyWalker'), ('6', 'ObiWan'), ('7', 'R2D2'), ('8', 'Yoda'),
         ('9', 'SpiderMan'), ('10', 'IronMan'), ('11', 'DeadPool'), ('12', 'Thor'), ('13', 'Hulk')]


def produce():
    """Simulates a user activity and stores the object in Kafka"""
    # argument parsing
    args = parse_args()
    broker = args.broker_host
    topic = args.kafka_topic
    print 'Starting up ... Broker: ' + broker
    # connect to Kafka
    producer = KafkaProducer(bootstrap_servers=broker)
    counter = 1
    while True:
        # send messages
        for user in users:
            user_activity = generate_activity(user)
            producer.send(topic, user_activity)
            print 'Message ' + str(counter) + ' send...'
            time.sleep(0.5)
            counter += 1


def generate_activity(user):
    """Generates a user activity formatted as JSON"""
    data = {}
    random_index = random.randint(0, 5)
    data['uid'] = user[0]
    data['username'] = user[1]
    data['action'] = actions[random_index]
    data['ts'] = datetime.datetime.now().isoformat()
    return json.dumps(data)


def parse_args():
    """Parses the necessary environment parameters"""
    parser = argparse.ArgumentParser(
        description='Handover of environment properties')
    parser.add_argument('broker_host',
                        help='hostname:port of the kafka broker')
    parser.add_argument('kafka_topic',
                        help='name of the kafka topic to store the messages')
    return parser.parse_args()


def main():
    """Start simulating user activity"""
    produce()


if __name__ == "__main__":
    main()

