print("Name: Neetu Salunkhe")
print("Roll no.: S109")

from queue import Queue
from threading import Thread
import time

# Queue with maximum size of 3
q = Queue(maxsize=3)

# Producer function
def producer():
    for i in range(1, 7):
        print("Producing:", i)
        q.put(i)          # Blocks if queue is full
        print("Added:", i)
        time.sleep(1)

# Consumer function
def consumer():
    for i in range(1, 7):
        item = q.get()    # Blocks if queue is empty
        print("Consumed:", item)
        time.sleep(2)
        q.task_done()

# Create threads
t1 = Thread(target=producer)
t2 = Thread(target=consumer)

# Start threads
t1.start()
t2.start()

# Wait for completion
t1.join()
t2.join()

print("Done")
