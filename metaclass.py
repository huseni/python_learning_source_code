__author__ = 'kathiria'

import metaclass


## Inheriting type class to build the meta class
class ArrtibuteType(type):
    def __call__(self, *args, **kwargs):
        obj = type.__call__(self, *args)
        for name, value in kwargs.items():
            setattr(obj, name, value)
        return obj


class Submarain(object, metaclass=ArrtibuteType):
    my_attr = ['color', 'year', 'name']


class Tank(object, metaclass=ArrtibuteType):
    my_attr = ('weight', 'year', 'identifier')


class animal(object, metaclass=ArrtibuteType):
    attr_set = ['fruits', 'vegi', 'meat', 'seafood']


sub = Submarain(name="Huseni", year = '1999', color = 'red')
print(sub.name)

#anm = animal(fruits = 'Apple', vegie = 'carrot', meat = 'chicken', seafood = 'fish')

#print ( anm.vegie)
#print ( anm.fruits)
#print ( anm.meat)

#print ( anm.seafood)