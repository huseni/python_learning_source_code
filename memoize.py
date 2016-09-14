__author__ = 'kathiria'

cg
class Memoize(object):
    def __init__(self,func):
        self._cache = {}
        self._func = func

    def __call__(self,*args):
        print ("In callable")
        print (self._cache)
        r = self._func(*args)
        if args not in self._cache:
            self._cache[args] = r
        return self._cache[args]

    def clear(self):
        self._cache.clear()

@Memoize
def d(*args):
    print ("hi")
    return args

t = (10,20,30,40,50,60)
t2 = (40,50,60, 70,80,90)
t3 = (60,80, 100,130, 140)
t4 = (10,20,30,40,50,60)

print(d(t))
print(d(t2))
print(d(t3))
print(d(t4))


#m()



#m = Memoize(d(a=12,b=41,c=42))
#m = Memoize(d(a=10,b=11,c=12))
#print(m.__call__(1,2,3))
#m = Memoize(d(a=10,b=11,c=12))
#print(m(14,22,12))
#print(m(a=10,b=11,c=12))

#print (m._cache)
#print (m._func)