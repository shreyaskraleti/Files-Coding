# import threading
# condition = threading.Condition()
# acquire()
# release()
# notify()
# notifyAll()
# wait() # wait until notification
# wait(seconds) # wait until notification or get expired

#
import threading
import time
import random
items = []
c = threading.Condition()
def producer(c):
    while True:
        c.acquire()
        item = random.randint(1,101)
        print("Producer Producing Item", item)
        items.append(item)
        print("Producer giving notification")
        c.notify()
        c.release()
        time.sleep(5)
        
def consumer(c):
    while True:
        c.acquire()
        print("Consumer waiting for updation..")
        c.wait()
        print("Consumer consumed the item.", items.pop())
        c.release()
        time.sleep(5)

t1 = threading.Thread(target=producer, args=(c,))
t2 = threading.Thread(target=consumer, args=(c,))

t1.start()
t2.start()



