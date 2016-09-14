__author__ = 'kathiria'

# cofollow.py
import os
import time

# Data source
def follow(filename,target):
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
            line = f.readline()
            if line != '':
                target.send(line)
            else:
                time.sleep(0.1)

# Decorator for coroutine functions
from functools import wraps

def coroutine(func):
    @wraps(func)
    def start(*args,**kwargs):
        f = func(*args,**kwargs)
        next(f)
        return f
    return start

# Sample coroutine
@coroutine
def printer():
    while True:
        item = yield     # Receive an item sent to me
        print(item)

# Example use
if __name__ == '__main__':
    follow('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\stocklog.csv',printer())

