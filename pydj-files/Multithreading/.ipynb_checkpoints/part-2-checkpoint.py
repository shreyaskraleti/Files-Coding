# # daemon threads:
# from threading import *
# print(current_thread().isDaemon())
# print(current_thread().daemon)

# #
# from threading import *
# t = Thread(target=lambda:None)
# t.setDaemon(True)
# # print(t.isDaemon())

# #
# from threading import *
# def job():
#     print("Child Thread")
    
# t = Thread(target=job) # job is function name
# print(t.isDaemon())

# t.setDaemon(True)

# print(t.isDaemon())

# #
# from threading import *
# import time
# def job():
#     for i in range(10):
#         print("Child Thread")
#         time.sleep(2)
# t = Thread(target=job)

# t.setDaemon(True)
# t.start()
# time.sleep(5)
# print("End of the main thread")

# # Synchronization:
# from threading import *
# import time
# def wish(name):
#     for i in range(10):
#         print("Good Afternoon", name)
#         time.sleep(2)

# t1 = Thread(target=wish, args=("Bonky", ))
# t2 = Thread(target=wish, args=("Shreya", ))

# t1.start()
# t2.start()

# # Lock:
# from threading import *
# l = Lock()
# def wish(name):
#     l.acquire()
#     for i in range(10):
#         print("Good Afternoon", name)
#         time.sleep(2)
#     l.release()
        
# t1 = Thread(target=wish, args=("Bonky", ))
# t2 = Thread(target=wish, args=("Shreya", ))
# t3 = Thread(target=wish, args=("Phani", ))

# t1.start()
# t2.start()
# t3.start()

#
# from threading import *
# l = Lock()
# l.acquire()
# print("Main thread trying to execute lock")
# l.acquire()
# print("Main thread trying to execute lock")

#
# from threading import *
# l = RLock()
# l.acquire()
# print("Main thread trying to execute lock")
# l.acquire()
# print("Main thread trying to execute lock")

#
# from threading import *
# import time
# l = RLock()
# def factorial(n):
#     l.acquire()
#     if n == 0:
#         result = 1
#     else:
#         result = n * factorial(n-1)
#     l.release()
#     return result

# def result(n):
#     print("factorial of ", n, factorial(n))
    
# t1 = Thread(target=result, args=(5, ))
# t2 = Thread(target=result, args=(9, ))

# t1.start()
# t2.start()

# # Semaphore
# from threading import *
# import time
# l = Semaphore(3)
# def wish(name):
#     l.acquire()
#     for i in range(5):
#         print("Good Afternoon", name)
#         time.sleep(2)
#     l.release()
        
# t1 = Thread(target=wish, args=("Bonky", ))
# t2 = Thread(target=wish, args=("Shreya", ))
# t3 = Thread(target=wish, args=("Phani", ))
# t4 = Thread(target=wish, args=("Deepika", ))
# t5 = Thread(target=wish, args=("Subbu", ))
# t6 = Thread(target=wish, args=("Shravya", ))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()

# Bounded Semaphore:
# from threading import *
# import time
# l = BoundedSemaphore(3)
# def wish(name):
#     l.acquire()
#     for i in range(5):
#         print("Good Afternoon", name)
#         time.sleep(2)
#     l.release()
#     l.release()
#     l.release()
        
# t1 = Thread(target=wish, args=("Bonky", ))
# t2 = Thread(target=wish, args=("Shreya", ))
# t3 = Thread(target=wish, args=("Phani", ))
# t4 = Thread(target=wish, args=("Deepika", ))
# t5 = Thread(target=wish, args=("Subbu", ))
# t6 = Thread(target=wish, args=("Shravya", ))

# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t5.start()
# t6.start()

# # Inter thread communication:
# # 1. Event()
# # 2. Condition()
# # 3. Queue()....
# import threading
# event = threading.Event()

# # methods:
# # set()
# # clear()
# # isset()
# # wait()
# # wait(seconds)

# import threading
# import time
# event = threading.Event()

# Event code:
def trafficpolice():
    while True:
        time.sleep(5)
        print("Traffic police giving green signal")
        event.set()
        time.sleep(10)
        print("Traffic police is giving red signal")
        event.clear()

def driver():
    num = 0
    while True:
        print("Drivers waiting for green signal")
        event.wait()
        print("Traffic signal is green... vehicles can move")
        while event.isSet():
            num = num + 1
            print("Vehicle No", num, "Crossing the signal")
            time.sleep(2)
            print("Traffic signal is red ..... drivers have to wait")

t1 = threading.Thread(target=trafficpolice)
t2 = threading.Thread(target=driver)

t1.start()
t2.start()





