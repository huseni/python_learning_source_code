__author__ = 'kathiria'


class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


uno = Node(1)
due = Node(2)
tri = Node(3)
qua = Node(4)

print uno
print due
print tri
print qua


class LinkedList(object):
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

    def __iter__(self):
        return self



