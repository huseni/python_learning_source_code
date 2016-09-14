__author__ = 'kathiria'


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def getdata(self):
        return self.data

    def setdata(self, newdata):
        self.data = newdata

    def getnext(self):
        return self.next

    def setnext(self, newnext):
        self.next = newnext


class unorderlist:
    def __init__(self):
        self.head = None

    def add(self, item):
        nd = Node(item)
        nd.setnext(self.head)
        self.head = nd

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getnext()
        return found

    def remove_data(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())


mylist = unorderlist()
mylist.add(12)
mylist.add(15)
mylist.add(18)
mylist.add(22)
mylist.add(25)
mylist.add(67)
print (mylist.size())
print(mylist.search(10))
print(mylist.search(25))
mylist.remove_data(22)
print (mylist.size())
#print (mylist.getdata())


#tempnode = Node(37)
#tempnode.setdata(21)
#tempnode.setdata(23)
#print (tempnode.getdata())
#print(tempnode.getnext())
