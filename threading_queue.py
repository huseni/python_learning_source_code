__author__ = 'kathiria'

import threading
import time
import Queue

job_queue = Queue.Queue()


class count_stuff(threading.Thread):
    """
    A thread class that will count a number, sleep and output that number
    """

    def __init__(self, start_num, end, q):
        self.num = start_num
        self.end = end
        self.que = q
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.num != self.end:
                self.num += 1
                print "In jobs: ", str(self.num)
                self.que.put(self.num)
                time.sleep(5)
            else:
                break


myThread = count_stuff(1, 5, job_queue)
myThread.start()

while True:
    if not job_queue.empty():
        job = job_queue.get()
        print ("Out jobs: ", job)
    time.sleep(2)