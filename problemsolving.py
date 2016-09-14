__author__ = 'kathiria'

l = [1,3,4,5,6,7,8,4,5,8,2,9,0,3,6,4,8,9,5,3,6]
duplist=[]
uniqudict={}
for elm in l:
    if elm not in uniqudict:
        uniqudict[elm] = elm
    else:
        duplist.append(elm)

#print "All the duplicate elements"
#print duplist


duplist1 = []
uniqlist =[]
for elm in l:
    elm1 = elm + 1
    for elm1 in l:
        if elm == elm1:
            duplist1.append(elm)
        else:
            uniqlist.append(elm)

print duplist1
final_set = set(duplist1 )
print final_set


l1 = [ 'x', 'f','w','f','j']
l1 = [6,34,86,43,76,43,87,54,4]
#l2 = l1
l2 = sorted(l1, reverse= True)
l3 = l1.sort()

print l2
print l3

flatlist = []
ll = [1, [2, 3], [4, 5, [6, 7]]]
for elm in ll:
    if type(elm) == list:
        flatlist.extend(elm)
    else:
        flatlist.append(elm)
print flatlist




lr = [1,2,3]
f = lambda a, b: a if a>b else b
ff = reduce(f, lr)
print ff



c = ''.join([`x` for x in range(101)])
print c

v = xrange(3)
print v