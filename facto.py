__author__ = 'kathiria'


def get_factorial(n):

    if n == 0:
        return 1
    else:
        return n * get_factorial(n-1)



def main():
    fact = get_factorial(5)
    print fact

main()