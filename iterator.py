__author__ = 'kathiria'


class MyIterator(object):
    def __init__(self, steps):
        self.steps = steps

    def next(self):
        if self.steps == 0:
            raise StopIteration
        self.steps -=1
        return self.steps

    def __iter__(self):
        return self


for e1 in MyIterator(10):
    print e1

