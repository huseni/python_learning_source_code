__author__ = 'kathiria'

import threading

def worker():
    print 'I am a worker'
    return

threads = []

for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
