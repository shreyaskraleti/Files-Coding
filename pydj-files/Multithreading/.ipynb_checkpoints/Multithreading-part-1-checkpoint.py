# Different ways to create a thread:
# 1. without class:
from threading import Thread
def display():
    for i in range(1, 11):
        print("Child Thread")
t = Thread(target=display)
t.start()
for i in range(1,11):
    print("Main Thread")

# 2. with class:
from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(1, 11):
            print("Child Thread")
t = Mythread()
t.start()
for i in range(1,11):
    print("Main Thread")
    
# 3. without threading:
import time
numbers = [1,2,3,4,5]

def double_numbers(numbers):
    for n in numbers:
        print("Doubles", 2 * n)

def square_numbers(numbers):
    for n in numbers:
        print("Squares", n * n)

begin_time = time.time()
double_numbers(numbers)
square_numbers(numbers)
end_time = time.time()

print(f"Time taken:, {end_time-begin_time}")   

# 4. with threading:
import threading
import time

numbers = [1,2,3,4,5]

def double_numbers(numbers):
    for n in numbers:
        print("Doubles", 2 * n)

def square_numbers(numbers):
    for n in numbers:
        print("Squares", n * n)

begin_time = time.time()
thread1 = threading.Thread(target=double_numbers, args=(numbers, ))
thread2 = threading.Thread(target=square_numbers, args=(numbers, ))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

end_time = time.time()

print(f"Time taken:, {end_time-begin_time}")

# Setting and Getting name of a thread:
from threading import current_thread

print("Current Thread name:", current_thread().name)
current_thread().name = "New Name"
print("Current Thread Name:", current_thread().name)

# ident():
import threading
def child_thread_func():
    print("Child Thread")
    print("Child Thread Identification Number", threading.current_thread().ident)

if __name__ == "__main__":
    print("Main Thread Identification Number", threading.current_thread().ident)
    
    child_thread = threading.Thread(target=child_thread_func)
    child_thread.start()

# active_count:
from threading import Thread, active_count, current_thread
import time

def display():
    print(current_thread().name), "....started"
    time.sleep(3)
    print(current_thread().name), "....ended"
    
if __name__ ==  "__main__":
    print("Main Thread Started")
    print("number of active threads:", active_count())
    
    t1 = Thread(target=display, name="ChildThread1")
    t2 = Thread(target=display, name="ChildThread2")
    t3 = Thread(target=display, name="ChildThread3")
    
    t1.start()
    t2.start()
    t3.start()
    
    print("number of active threads after the thread creation:", active_count())
    
    time.sleep(5)
    
    print("number of active threads after the waiting", active_count())
    
    print("Main thread ended")    
    
# is_alive():
from threading import Thread, current_thread
import time

def display():
    print(current_thread().name), "....started"
    time.sleep(3)
    print(current_thread().name), "....ended"
    
t1 = Thread(target=display, name="ChildThread1")
t2 = Thread(target=display, name="ChildThread2")
    
t1.start()
t2.start()
    
print(t1.name, "is Alive", t1.is_alive())
print(t2.name, "is Alive", t2.is_alive())
    
time.sleep(5)
    
print(t1.name, "is Alive", t1.is_alive())
print(t2.name, "is Alive", t2.is_alive())

# join() method:
from threading import Thread
import time

def display():
    for i in range(1, 11):
        print("Bonkers")
        time.sleep(3)

t = Thread(target=display)
t.start()
t.join()

for i in range(1, 11):
    print("Shreya")
    

    
 