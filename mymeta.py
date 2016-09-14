__author__ = 'kathiria'

class mytype(type):
    def __new__(cls,name,bases,__dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super(mytype, cls).__new__(cls,name,bases,__dict__)

class myobject(metaclass=mytype):
    pass

class Stock(myobject):
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares


class MyStock(Stock):
    pass

print ("_"*50)
s = Stock('GOOG', 400, 748.3)
print ("_"*50)
ms = MyStock('GOOG', 400, 748.3)