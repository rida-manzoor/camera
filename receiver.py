import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.17.0.3'))
channel = connection.channel()

# Create a queue
channel.queue_declare(queue='idk', durable=True)

# Define a callback function to handle incoming messages
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# Set up a consumer to listen for incoming messages
channel.basic_consume(queue='idk', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')

# Start consuming messages
channel.start_consuming()

