__author__ = 'kathiria'

import random


def cf():
    """
    Consumer function.
    """
    while True:
        val = yield
        print val,


def pf(c):
    """
    Producer function.
    """
    while True:
        val = random.randint(1, 10)
        c.send(val)
        yield

if __name__ == '__main__':
    c = cf()
    #c.send(None)
    next(c)
    p = pf(c)
    #print next(p)
    for wow in range(10):
        next(p)