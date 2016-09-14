__author__ = 'kathiria'

import random

def cf():
    while 1 == 1:
        val = yield
        yield val * 10


def pf(c):
    while True:
        rn = random.randint(1,100000000)
        print ("Random Number : %r" % rn)
        c.send(rn)
        yield

if __name__== "__main__":
    c = cf()
    next(c)
    p = pf(c)
    print (p)
    for elm in p:
        next(p)