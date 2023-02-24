# '''
# A program is an executable file which consists of a set of instructions to perform some task and is usually stored on the disk of your computer.
# A process is what we call a program that has been loaded into memory along with all the resources it needs to operate. It has its own memory space.
# A thread is the unit of execution within a process. A process can have multiple threads running as a part of it, where each thread uses the process’s memory space and shares it with other threads.
# Multithreading is a technique where multiple threads are spawned by a process to do different tasks, 
# at about the same time, just one after the other. 
# This gives you the illusion that the threads are running in parallel, but they are actually run in a concurrent manner. In Python, the Global Interpreter Lock (GIL) prevents the threads from running simultaneously.
# Multiprocessing is a technique where parallelism in its truest form is achieved. 
# Multiple processes are run across multiple CPU cores, 
# which do not share the resources among them. Each process can have many threads running in its own memory space. In Python, each process has its own instance of Python interpreter doing the job of executing the instructions.
# '''


import threading
from threading import *
from time import sleep
class AnilThread(Thread):
    def run(self):
        for i in range(10):
            print("this is first thread")
            print(threading.current_thread().getName())
            sleep(5)
class KiranThread(Thread):
    def run(self):
        for i in range(10):
            print("this is second thread")
            sleep(5)
A = AnilThread()
B = KiranThread()
A.start()
print(A.is_alive())
sleep(1)
B.start()





# import threading

# print('this is thread',threading.current_thread().getName())





