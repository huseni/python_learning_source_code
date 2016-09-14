__author__ = 'kathiria'


import threading
import time
import logging

#class MyThread(threading.Thread):
#
#    def run(self):
#        #print("This is a thread start")
#        time.sleep(1)
#        #print("This is a thread end")
#        return
#
#if __name__ == '__main__':
#    for i in range(4):
#        t = MyThread()
#        t.start()
#        t.join()
#    print("Main Complete")

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)
class MyThread(threading.Thread):

    def run(self):
        time.sleep(1)
        logging.debug('running')
        return

if __name__ == '__main__':
    for i in range(3):
        t = MyThread()
        t.start()
        print ('t.is_alive()=', t.is_alive())
        t.join()
        print ('t.is_alive()=', t.is_alive())