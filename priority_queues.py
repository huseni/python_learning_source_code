__author__ = 'kathiria'


try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

q = Q.PriorityQueue()
qq = Q.deque(3)
q.put(10)
q.put(1)
q.put(5)
q.put('a')
q.put('j')
#while not q.empty():
#    print q.get(),

qq.append(8)
qq.append(7)
qq.append(4)
#qq.append(65)
#qq.append(21)

while not qq.empty():
    print qq.pop(4)


