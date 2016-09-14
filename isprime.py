__author__ = 'kathiria'


def is_prime(x):
    if x < 2:
        return False
    else:
        if x == 2:
            return True
        else:
            for i in range(2, x):
                if x % i == 0:
                    return False
            return True
x = int(raw_input("enter a prime number"))
print is_prime(x)