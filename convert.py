__author__ = 'kathiria'


def bytesto(bytes, to, bsize=1024):
    """
    Convert bytes to megabytes or gigabytes, etc.
    sample code:
           print('mb= ' + str(bytesto(314575262000000, 'm')))

    sample output:
           mb= 300002347.946
    """
    a = {'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6}
    csize = float(bytes)
    for i in range(a[to]):
        csize = csize / bsize

    print ('Bytes %s converted to %s' % (bytes, to))
    return csize


print(bytesto(745656635264, 'k'))
print(bytesto(745656635264, 'm'))
print(bytesto(745656635264, 'g'))
print(bytesto(745656635264, 't'))
print(bytesto(745656635264, 'p'))
print(bytesto(745656635264, 'e'))