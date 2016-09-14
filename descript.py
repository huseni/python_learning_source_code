__author__ = 'kathiria'

import decimal

from descrip import Descriptor

# Descriptor that implements type-checking
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

_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('String', str) ]


_typed_classes = [
    ('Integer', int),
    ('Float', float),
    ('Complex', complex),
    ('Decimal', decimal.Decimal),
    ('List', list),
    ('Bool', bool),
    ('String', str) ]

globals().update((name, type(name, (Typed,), {'expected_type':ty}))
                 for name, ty in _typed_classes)

