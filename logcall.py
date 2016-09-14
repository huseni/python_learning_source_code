__author__ = 'kathiria'

def logged(func):
    print('Adding logging to', func.__name__)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


import os

def logged(func):
    # If logging not enabled, return the original function unwrapped
    if 'LOGDISABLE' in os.environ:
        return func
    print('Adding logging to', func.__name__)
    def wrapper(*args,**kwargs):
        print(func.__name__)
        return func(*args,**kwargs)
    return wrapper