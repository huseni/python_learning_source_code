__author__ = 'kathiria'


### Palindrom Number ###
s1 = "rajamaharaja"
s2 = 'golog'

if s2[::] == s2[::-1]:
    print ("Palindrom")
else:
    print ("Not Palindrom")

### Fibonacci Series ###

## recursive
def fib(n):
    if isinstance(n, int):
        if n < 2:
            return n
        else:
            return fib(n-2) + fib(n-1)


#fib_num = [n for n in fib(range(10))]

print (fib(30))

## Generator
def fibI():
    a, b = 0, 1
    while True:
        a,b = b, a+b
        yield a
f = fibI()
for i in range(30):
    print next(f)

## Is Prime number


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

