__author__ = 'kathiria'


def func():
    print "func()"

funcObj = func
funcObj()


def myFunction(in_function):
    def out_function():
        print "Entry: ", in_function.__name__
        print ("I am executed in out function")
        in_function()
        print "Exit: ", in_function.__name__
    return out_function


def simple_function():
    print ("I am executed in simple function")

enhanced_function = myFunction(simple_function)
exec_fun = enhanced_function
exec_fun()


def dollar(in_fnc):
    def out_fnc(in_fnc):
        return '$' + str(in_fnc)
    return out_fnc


@dollar
def price(amount):
    return amount

print price(100)


def pound(in_fnc):
    def out_fnc(in_fnc):
        return (u"\u00A3").encode('utf-8') + str(in_fnc)
    return out_fnc

@pound
def price(amount):
    return amount

print price(100)


def count(f):
    def inner(*args, **kargs):
        inner.counter += 1
        return f(*args, **kargs)
    inner.counter = 0
    return inner

@count
def my_fnc():
    print "i am called "


import time


def timer(f):
    def inner(*args, **kargs):
        t = time.time()
        ret = f(*args, **kargs)
        print 'timer = %s' %(time.time()-t)
        return ret
    return inner

@timer
def my_fnc():
    pass


def bold(f):
    def wrapped():
        return '<b>' + f() + '</b>'
    return wrapped


def italic(f):
    def wrapped():
        return '<i>' + f() + '</i>'
    return wrapped

@bold
@italic
def hello():
    return 'hello'

print hello()