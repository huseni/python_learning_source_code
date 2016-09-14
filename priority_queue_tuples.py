__author__ = 'kathiria'


try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
q.put((10,'a'))
q.put((1,'b'))
q.put((5,'d'))
while not q.empty():
    print q.get(),