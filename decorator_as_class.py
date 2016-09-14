__author__ = 'kathiria'


class IdentityDecorator(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        self.func()


@IdentityDecorator
def a_function():
    print "I'm a normal function."

a_function()
# >> I'm a normal function


from functools import wraps


def argumentative_decorator(gift):
    def func_wrapper(func):
        @wraps(func)
        def returned_wrapper(*args, **kwargs):
            print "I don't like this " + gift + " you gave me!"
            return func(gift, *args, **kwargs)
        return returned_wrapper
    return func_wrapper


@argumentative_decorator("sweater")
def grateful_function(gift):
    print "I love the " + gift + "! Thank you!"

grateful_function()
# >> I don't like this sweater you gave me!
# >> I love the sweater! Thank you!