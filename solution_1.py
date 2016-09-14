__author__ = 'kathiria'


def print_msg():
    n = int(raw_input('enter a number'))
    numbers = range(1, n)
    for num in numbers:
        if num % 3 == 0 and num % 5 ==0:
            print "fuzzbuzz"
        elif num % 3 == 0:
            print "fuzz"
        elif num % 5 == 0:
            print "buzz"
        else:
            print num


print_msg()