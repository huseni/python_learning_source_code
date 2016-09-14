__author__ = 'kathiria'


def modulus_three(n):
    r = n % 3
    try:
        if r == 0:
            print "multiple of 3"

        elif r ==1:
            print "reminder 1"

        else:
            assert r ==2, "Remainder is not 2"
            print("Reminder 2" )
    except IOError as v:
        raise v


if __name__ == '__main__':
    modulus_three(4.5)