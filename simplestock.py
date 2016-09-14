__author__ = 'kathiria'

class SimpleStock(object):
        def __init__(self,name,shares,price):
            self.name = name
            self.shares = shares
            self.price = price
        def cost(self):
            return self.shares*self.price

goog = SimpleStock('GOOG',100,490.10)
ibm  = SimpleStock('IBM',50, 91.23)

print(goog.__dict__)
print(ibm.__dict__)

goog.date = "6/11/2007"
print(goog.__dict__)

print(ibm.__dict__)
goog.__dict__['time'] = '9:45am'
print(goog.time)

print(goog.__class__)
print(ibm.__class__)

print(goog.cost())
print(ibm.cost())

print(SimpleStock.__dict__['cost'])
print(SimpleStock.__dict__['cost'](goog))
print(SimpleStock.__dict__['cost'](ibm))
