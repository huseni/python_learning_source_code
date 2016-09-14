__author__ = 'kathiria'

from threading import Thread
import time

def timer(name, delay, repeat):
    print ("Timer: " + "started")
    while repeat > 0:
        time.sleep(delay)
        print (name + ":" + str(time.time()))
        repeat -=1
    print ("Timer: " + name + " " + "completed")


def main():
    t1 = Thread(target = timer, args=("Timer1", 1, 5))
    t2 = Thread(target = timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    t1.join() # wait until the thread is finish
    t2.join()
    print("Main Complete")


if __name__ == '__main__':
    main()
