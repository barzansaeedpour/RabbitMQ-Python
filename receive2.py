
import pika
import json


# Stablish the connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# declare the queue
queue = channel.queue_declare('order_report')
queue_name = queue.method.queue

# bind the exchange to the queue 
channel.queue_bind(
    exchange='order', # the exchange
    queue=queue_name, # the queue
    routing_key='order.report' # binding key
)

# Consume the messages:

def callback(ch, method, properties, body):
    payload = json.loads(body)
    print('[x] Generating report')
    print(f"""
          ID: {payload.get('id')}
          User Email: {payload.get('user_email')}
          Product: {payload.get('product')}
          Quantity: {payload.get('quantitiy')}
          """)
    print('[x] Done')
    # we will send an aknowledgement to RabbitMQ that we received the message, and RabbitMQ is free to delete the message
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(on_message_callback=callback, queue=queue_name)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

