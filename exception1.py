__author__ = 'kathiria'

import this

def test_exception(a=None):

    if not a:
        raise ValueError("Missubg the value for a")
    if a < 10:
        raise OverflowError ("Value grater than expected")
    if a == 10:
        print("This is the right value")



test_exception(10)

