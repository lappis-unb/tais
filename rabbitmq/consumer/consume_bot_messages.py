#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()

channel.queue_declare(queue='bot_messages')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(
        queue='bot_messages', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for bot messages.')
    channel.start_consuming()
