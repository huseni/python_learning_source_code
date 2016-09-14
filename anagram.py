__author__ = 'kathiria'

import os

### Check Off the status of string and list
def anagramSolution1(s1, s2):
    alist = list(s2)
    i = 0

    ok = True
    while i < len(s1) and ok:
        j = 0
        found = False
        while j < len(alist) and not found:
            if s1[i] == alist[j]:
                found = True
            else:
                j += 1
        if found:
            alist[j] = None
        else:
            ok = False
        i += 1
    print alist
    return ok

print(anagramSolution1('python', 'onhtpy'))


### Brute Force Algorithum ###
def testanagram(s1, s2):
    from itertools import permutations
    perms_list = [''.join(p) for p in permutations('stack')]
    if s2 in perms_list:
        print perms_list
        print "String is an anagram"
    else:
        print "String is not anagram"

testanagram('stack', 'kcats')


### Sort and Compare
def anagramsol3(s1, s2):
    sl1 = list(s1)
    sl2 = list(s2)

    sl1.sort()
    sl2.sort()
    i = 0
    match = True

    while i < len(sl1) and match:
        if sl1[i] == sl2[i]:
                i += 1
        else:
            match = False

    return match

print(anagramsol3('python', 'typhon'))

def test_code():
    test = 0
    for i in range(5):
        for j in range(5):
            test = test + i * j
    return test
print (test_code())