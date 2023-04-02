import pika
import random
import threading
import time

# RabbitMQ server configuration
host = "172.17.0.3"
port = 5672
username = "guest"
password = "guest"
virtual_host = "/"

# Thread function
def send_message(thread_id):
    # Create a connection to the RabbitMQ server
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(host, port, virtual_host, credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    # Declare the queue
    queue_name = "idk"
    channel.queue_declare(queue=queue_name, durable=True)

    # Send messages
    while True:
        try:
            # Randomly decide whether the thread is up or down
            is_up = random.choice([True, False])

            # Send the message
            message = f"Thread {thread_id} is {'up' if is_up else 'down'}"
            channel.basic_publish(exchange="", routing_key=queue_name, body=message)
            print(message)

            # Wait for a random amount of time before sending the next message
            time.sleep(random.randint(10, 110))
        except:
            # If an exception occurs, assume that the thread has gone offline
            message = f"Thread {thread_id} has gone offline"
            print(message)

            # Wait for a random amount of time before trying to send the next message again
            time.sleep(random.randint(120, 300))

    # Close the connection
    connection.close()

# Create and start the threads
threads = []
for i in range(10):
    thread = threading.Thread(target=send_message, args=(i,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

