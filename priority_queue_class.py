__author__ = 'kathiria'

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q


class Skill(object):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print 'New Level:', description
        return

    def __cmp__(self, other):
        a = cmp(self.priority, other.priority)
        print ("level : %s " %a)
        return cmp(self.priority, other.priority)

q = Q.PriorityQueue()

q.put(Skill(5, 'Proficient'))
q.put(Skill(10, 'Expert'))
q.put(Skill(1, 'Novice'))

while not q.empty():
    next_level = q.get()
    print 'Processing level:', next_level.description
