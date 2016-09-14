__author__ = 'kathiria'

import threading
import time
import logging

logging.basicConfig(level=logging.CRITICAL,
                    format='(%(threadName)-9s) %(message)s',)

class MyThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(MyThread,self).__init__(group=group, target=target, name=name )
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.critical('running with %s and %s', self.args, self.kwargs)
        #print(self.args, self.kwargs)
        return

if __name__ == '__main__':
    for i in range(3):
        t = MyThread(args=(i,), kwargs={'a':1, 'b':2})
        t.start()
