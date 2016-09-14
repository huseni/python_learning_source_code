__author__ = 'kathiria'


class A(object):

    def __init__(self, a):
        print "This is a constructure - %s" % a

    def foo(self, x):
        print "executing instance method foo(%s,%s)" % (self, x)
        print "Constructure value - %s" % a

    @classmethod
    def class_foo(cls, x):
        print "executing class_foo(%s,%s)" % (cls, x)

    @staticmethod
    def static_foo(x):
        print "executing static_foo(%s)" % x

    def instance_foo(self, x):
        print "executing instance_foo(%s)" % x

a = A(10)
print " ********** starting ************"
a.foo(1)


print " ********** Methods with Class decorators ***********"
a.class_foo(1)
A.class_foo(1)


print " ********** Methods with Static decorators ***********"
a.static_foo(1)
# executing static_foo(1)

A.static_foo('hi')
# executing static_foo(hi)