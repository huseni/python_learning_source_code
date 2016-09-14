__author__ = 'kathiria'


def my_gen():
    """a simple generator function"""
    n = 1
    print("This is printed first")
    # Generator function contains yield statements
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed at last")
    yield n

a = my_gen()
next(a)