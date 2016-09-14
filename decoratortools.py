__author__ = 'kathiria'
    return x + y

import time
from functools import wraps
import logging


def execution_time(func):
    """
    Decorator that reports the execution time.
    USAGE:
    @execution_time
    def test(n):
        g = range(n)
        return g
    print(test(100000))
    """
    @wraps(func)
    #def wrapper(a, b, c):
    def wrapper(*args, **kwargs):
        start = time.time()
        #res = func(a)
        res = func(*args, **kwargs)
        print args
        end = time.time()
        print(func.__name__, end-start)
        return res
    return wrapper


def log_it(level, name = None, message=None):
    """
    Add logging to a function. level is the logging level, name is the logger name, and message is the log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# Example use
@log_it(logging.DEBUG)
def add(x, y):

@log_it(logging.CRITICAL, 'example')
def spam():
    print('Spam!')

print(add(10,20))
print(spam())


#from inspect import
#from functools import wraps
#
#def typeassert(*ty_args, **ty_kwargs):
#def decorate(func):
## If in optimized mode, disable type checking
#if not __debug__:
#return func
## Map function argument names to supplied types
#sig = signature(func)
#bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
#@wraps(func)
#def wrapper(*args, **kwargs):
#bound_values = sig.bind(*args, **kwargs)
## Enforce type assertions across supplied arguments
#for name, value in bound_values.arguments.items():
#if name in bound_types:
#if not isinstance(value, bound_types[name]):
#raise TypeError(
#'Argument {} must be {}'.format(name, bound_types[name])
#)
#return func(*args, **kwargs)
#return wrapper
#return decorate