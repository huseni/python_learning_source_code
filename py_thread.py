__author__ = 'kathiria'

import sys
import threading

TOTAL = 0
MY_LOCK = threading.Lock()

class CountThread(threading.Thread):
    def run(self):
        global TOTAL
        for i in range(100):
            MY_LOCK.acquire()
            TOTAL = TOTAL + 1
            if TOTAL == 100:
                break
            MY_LOCK.release()
        print('%s\n' % (TOTAL))

a = CountThread()
b = CountThread()
a.start()
b.start()
#a.join()
#b.join()


