__author__ = 'kathiria'

def lookups():
    s = [1,3,5,7,9]
    try:
        item = s[8]

    except LookupError:
        print("Handled Index Error")

    d = dict(a=65, b=66, c=67)
    try:
        value = d['x']
    except LookupError:
        print("Handled KeyError")


if __name__ == '__main__':
    lookups()