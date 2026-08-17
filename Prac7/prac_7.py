#prac7

import threading
import time
import random

# Size of the bounded buffer
BUFFER_SIZE = 5

# Circular buffer
buffer = [None] * BUFFER_SIZE

# Circular queue pointers
in_position = 0
out_position = 0

# Mutex for synchronized access to the buffer
mutex = threading.Lock()

# Semaphores
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)             


# Producer function
def producer(producer_id):
    global in_position

    for i in range(10):
        item = f"P{producer_id}-{i}"

        # Wait for an empty slot
        empty.acquire()

        # Enter critical section
        mutex.acquire()

        # Insert item into circular buffer
        buffer[in_position] = item
        print(f"Producer {producer_id} produced: {item}")
        print("Buffer:", buffer)

        # Move circularly
        in_position = (in_position + 1) % BUFFER_SIZE

        # Leave critical section
        mutex.release()

        # Increase count of full slots
        full.release()

        time.sleep(random.uniform(0.5, 1.5))


# Consumer function
def consumer(consumer_id):
    global out_position

    for i in range(10):

        # Wait for a filled slot
        full.acquire()

        # Enter critical section
        mutex.acquire()

        # Remove item from circular buffer
        item = buffer[out_position]
        buffer[out_position] = None

        print(f"Consumer {consumer_id} consumed: {item}")
        print("Buffer:", buffer)

        # Move circularly
        out_position = (out_position + 1) % BUFFER_SIZE

        # Leave critical section
        mutex.release()

        # Increase count of empty slots
        empty.release()

        time.sleep(random.uniform(0.5, 2))


# Create producer threads
producer1 = threading.Thread(target=producer, args=(1,))
producer2 = threading.Thread(target=producer, args=(2,))

# Create consumer threads
consumer1 = threading.Thread(target=consumer, args=(1,))
consumer2 = threading.Thread(target=consumer, args=(2,))


# Start all threads
producer1.start()
producer2.start()
consumer1.start()
consumer2.start()


# Wait for all threads to finish
producer1.join()
producer2.join()
consumer1.join()
consumer2.join()

print("\nAll producers and consumers have finished.")
