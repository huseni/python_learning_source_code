#!/usr/bin/python
# Filename: func_doc.py


def printMax(x, y):
    """
    Prints the maximum of two numbers.
    """
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__