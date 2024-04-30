################################# simple example
# #!/usr/bin/env python
# import pika, sys, os

# def main():
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='hello')

#     def callback(ch, method, properties, body):
#         print(f" [x] Received {body}")

#     channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

#     print(' [*] Waiting for messages. To exit press CTRL+C')
#     channel.start_consuming()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)

################################# Another example

import pika
import json


# Stablish the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare the queue
queue = channel.queue_declare('order_notify')
queue_name = queue.method.queue

# bind the exchange to the queue 
channel.queue_bind(
    exchange='order', # the exchange
    queue=queue_name, # the queue
    routing_key='order.notify' # binding key
)

# Consume the messages:

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('[x] Notifying {}'.format(payload['user_email']))
    print('[x] Done')
    # we will send an aknowledgement to RabbitMQ that we received the message, and RabbitMQ is free to delete the message
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()


