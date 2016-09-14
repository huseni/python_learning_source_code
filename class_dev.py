__author__ = 'kathiria'


class Super():
    def method1(self):
        print "Hello in super class"
        pass


class Sub(Super):
    def method1(self, param1, param2, param3):
       super(Sub, self).method1() # a proxy object, see http://docs.python.org/library/functions.html#super
       print "In Subclass"


sub = Sub()
sub.method1(1,2,3)