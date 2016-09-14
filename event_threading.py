__author__ = 'kathiria'


from threading import Thread, Event
import time


def countdown(n, started_evt):
    print("Starting countdown")
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(2)

# creating the object that will be used for signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print ('Launching count down')
t = Thread(target=countdown, args=(10, started_evt))
t.start()
t.join()
# Wait for the thread to start
started_evt.wait()
print('Countdown is running')



