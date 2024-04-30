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

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='order',
    exchange_type='direct'
)

order = {
    'id': str(uuid.uuid4()),
    'user_email': 'barzansaeedpour@gmail.com',
    'product': 'RabbitMQ',
    'quantity': 1
}

channel.basic_publish(
    exchange='order',
    routing_key='order.notify',
    body=json.dumps({'user_email': order['user_email']})
)

print('[x] Sent notify message')

channel.basic_publish(
    exchange='order',
    routing_key='order.report',
    body=json.dumps(order)
)

connection.close()