__author__ = 'kathiria'


def f(*args):
    print args


f(10, 30, 40, 50)


def print_all(*args):
    for x in enumerate(args):
        print x

print_all('A','b','b','a')


def f(**kargs):
    print(kargs)

f(x=1)


def kargs_function(**kargs):
    for k, v in kargs.iteritems():
        print (k,v)

my_dict = {'one' : 1, 'two': 2, 'three' : 3}

kargs_function(**{'uno':'one','dos':'two','tres':'three'})
kargs_function(x=20, y=40, z=55)

kargs_function(**my_dict)

import os
print(os.getcwd())