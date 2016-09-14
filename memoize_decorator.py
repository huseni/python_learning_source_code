__author__ = 'kathiria'


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

#for i in range(1,10):
#    print(i, factorial(i))

print(factorial(12))
print("------------------------------------------------------------------------")


def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__

    return helper

@call_counter
def succ(x,y):
    return x + y

print(succ.calls)
print("------------------------------------------------------------------------")
for i in range(10):
    print(succ(i,i))
print("------------------------------------------------------------------------")
print(succ.calls)