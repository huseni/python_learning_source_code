__author__ = 'kathiria'


def sum_of_num(l):
    i = 0
    summ = 0
    for i in l:
        summ = summ + i
    return summ

l = [1,3,5,6]
s = sum_of_num(l)
print s



def sumofnum(l):

    return l[0]+sumofnum(l[1:])


def power(p,q):
    if q == 0:
        return 1
    else:
        return p * power(p, q-1)

pp = power(5, 3)
print pp


def toStr(n,base):
    convertString = "0123456789ABCDEF"
    if n < base:
       return convertString[n]
    else:
       return toStr(n//base,base) + convertString[n%base]

print(toStr(10,2))


def revstring(name):
