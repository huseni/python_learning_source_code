__author__ = 'kathiria'

import sys

def main():
    try:
        print("I am trying")
        return 0
    except :
        print("I am an exception")
        return 1

if __name__ == "__main__":
    print"executing main"
    sys.exit(main())

