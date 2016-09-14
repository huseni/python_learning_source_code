__author__ = 'kathiria'

class Descriptor(object):
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)

class Typed(Descriptor):
    expected_type = object
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected %s' % self.expected_type)
        super(Typed, self).__set__(instance, value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super(Positive, self).__set__(instance, value)

class Negative(Descriptor):
    def __set__(self, instance, value):
        if value > 0:
            raise ValueError('Expected <= 0)')
        super(Negative, self).__set__(instance, value)

# Mixing it up
class PositiveInteger(Integer,Positive):
    pass

class PositiveFloat(Float,Positive):
    pass

class Foo(object):
        a = Descriptor('a')
        b = Descriptor('b')
        c = Descriptor('c')

# Sample typed class
if __name__ == '__main__':
    class Stock(object):
        name   = String('name')
        shares = Integer('shares')
        price  = Float('price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price
        @property
        def cost(self):
            return self.shares * self.price


s = Stock('GOOG',100,490.10)
print(s.name)
print(s.shares)
print(Stock.__dict__.keys())

q = Stock.__dict__['shares']
#print(q.__get__(s))
q.__set__(s,75)
print(s.shares)

q.__set__(s, 88)
print(s.shares)

f = Foo()
print(f)
print(f.a)
print(f.b)
f.a=55
print (f.a)

s = Stock('GOOG', 100, 490.10)
print (s.name)

