__author__ = 'kathiria'

def memoize(f):
    memo = {}
    def helper(x):
        helper.calls += 1
        print("Number of times the decorator method is called %r " % helper.calls)
        if x not in memo:
            memo[x] = f(x)
            print("Caching and  returning the results starts")
            print (memo)
            print("Caching and  returning the results ends")
        print("returning the results")
        return memo[x]
    helper.calls = 0
    return helper

@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#fib = memoize(fib)

print(fib(40))



def is_palindram(n):
    ns = list(str(n))
    for nn in ns:
        if nn != ns.pop():
            return False
    return True


n = 3003
print (is_palindram(n))

n = 'raar'
print (is_palindram(n))


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

x = [[ 2,4],
     [8,12],
     [93,74,6]]

res = [[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        res[j][i] = x[i][j]

for r in res:
    print r



