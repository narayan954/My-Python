from collections import deque
import time
import threading


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)

def serve_order():
    while not queue.is_empty():
        print("Now serving: ",queue.dequeue())
        time.sleep(2)


queue = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order)

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()


