import pika

# Establish a connection with RabbitMQ server
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='172.17.0.3'))
channel = connection.channel()

# Create a queue 
channel.queue_declare(queue='idk',durable=True)

# Send a message to the queue
channel.basic_publish(exchange='',
                      routing_key='idk',
                      body='Hello, World!')
print(" [x] Sent 'Hello, World!'")

# Close the connection
connection.close()

