__author__ = 'kathiria'

import sys

text = ""
while 1:
   c = sys.stdin.read(1)
   text = text + c
   if c == '\n':
       break

print "Input: %s" % text


def fun(x, y):
    t = x
    i = 0
    while i < y-1:
        t = x * t
        i +=1
    return t

x = fun(2,4)
print x

ld = ['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
ld = sorted(ld)
for index, elm in enumerate(ld):
    print index ,elm


def delta_deck():
    """
    Adding slides for DB2 & Sybase
    """
    deck = []
    delta_deck = ""
    platform_tuple = ('DB2', ' & ', 'Sybase')
    for db in platform_tuple:
        delta_deck += db
    print ("%s" % delta_deck)
    deck =

delta_deck()