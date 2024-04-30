######################## simple example
# import pika
# connection = pika.BlockingConnection(
#     pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()

# channel.queue_declare(queue='hello')

# channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
# print(" [x] Sent 'Hello World!'")
# connection.close()

######################## Another example

import pika
import json
import uuid

# Stablish the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare the exchange
channel.exchange_declare(
    exchange='order', # name of the exchange
    exchange_type='direct' # the exchange type
)

# the message that we want to send
order = {
    'id': str(uuid.uuid4()),
    'user_email': 'barzansaeedpour@gmail.com',
    'product': 'RabbitMQ',
    'quantity': 1
}


# publish the messages
channel.basic_publish(
    exchange='order',  # the exchange that we want to use
    routing_key='order.notify', # the routing key
    body=json.dumps({'user_email': order['user_email']}) # body of the message
)

print('[x] Sent notify message')

channel.basic_publish(
    exchange='order', # the exchange that we want to use
    routing_key='order.report',
    body=json.dumps(order) # body of the message
)

print('[x] Sent report message')


# close the message
connection.close() 