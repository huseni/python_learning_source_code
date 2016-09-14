__author__ = 'kathiria'

sum = 0
for i in range(0, 10):
    sum += i
    #print sum
print sum


def sumOfN3(n):
   return (n*(n+1))/2

print(sumOfN3(9))



def find_min_in_list():
    l = [4, 8, 598, 37, 57, 947, 56, 3559, 5736, 354, 241]
    x = min(float(s) for s in l)
    print x

find_min_in_list()


