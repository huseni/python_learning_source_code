__author__ = 'kathiria'

class Validator(object):

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value
    @classmethod
    def validate(cls, value):
        pass

class Typed(Validator):
    expected_type = object
    @classmethod
    def validate(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError('Expected %s' % cls.expected_type)
        super(Typed, cls).validate(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def validate(cls, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        super(Positive, cls).validate(value)

class NonEmpty(Validator):
    @classmethod
    def validate(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        super(NonEmpty, cls).validate(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

if __name__ == '__main__':
    class Stock(object):
        __slots__ = ('name','_shares','_price')
        def __init__(self,name,shares,price):
            self.name = name
            self.shares = shares
            self.price = price

        def __repr__(self):
            return 'Stock(%r,%r,%r)' % (self.name, self.shares, self.price)

        @property
        def shares(self):
            return self._shares
        @shares.setter
        def shares(self,value):
            PositiveInteger.validate(value)
            self._shares = value

        @property
        def price(self):
            return self._price
        @price.setter
        def price(self,value):
            PositiveFloat.validate(value)
            self._price = value

        @property
        def cost(self):
            return self.shares * self.price

        def sell(self,nshares):
            self.shares -= nshares
            return self.shares

Integer.validate(10)
print(Integer.validate(10))
#Integer.validate('10')

PositiveInteger.validate(10)
PositiveInteger.validate(40)

