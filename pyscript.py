__author__ = 'kathiria'




def f(x,y):
    t = x
    i=0
    while (i<y-1):
          t = t*x
          i +=1

    return t

u = f(3,3)
print "%s" % u


items = [1,2,3,4,5]

def sqrt(x): return x**2

a = list(map(sqrt, items))
print a


def sqr(x):
    return x**2

def cub2(x):
    return x**3

def cube(x):
    return x**4

def cube1(x):
    return x**5

fun = [sqr, cub2, cube, cube1]

for r in range(5):
    value = map(lambda x : x(r), fun)
    print value




a = range(-5, 5)
z = list(filter((lambda x : x<0), range(-2,4)))
print z

w = list(map((lambda x : x<0), range(-2,4)))
print w

def foo(x,y):
    return lambda x, y: x ** y

j = foo(2,3)
print j


do = list(filter(lambda x, y: x**y, [1, 2, 3, 4, 5]))
dod = reduce(lambda x, y: x+y, ['a','b','c','d','e','f'])
print do















