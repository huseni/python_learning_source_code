__author__ = 'kathiria'


class it:

    def __init__(self):
        #start at -1 so that we get 0 when we add 1 below.
        self.count = -1
    #the __iter__ method will be called once by the for loop.
    #the rest of the magic happens on the object returned by this method.
    #in this case it is the object itself.

    def __iter__(self):
        return self
    #the next method will be called repeatedly by the for loop
    #until it raises StopIteration.

    def next(self):
        self.count += 1
        if self.count < 10:
            return self.count
        else:
            #a StopIteration exception is raised
            #to signal that the iterator is done.
            #This is caught implicitly by the for loop.
            raise StopIteration


def some_func():
    return it()

#for i in some_func():
#    print i

iterator = some_func()
try:
    while 1:
        print iterator.next()
except StopIteration:
    pass