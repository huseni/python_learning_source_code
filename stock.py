__author__ = 'kathiria'

# stock.py


class Stock(object):
    _rowtypes = (str, int, float)
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._rowtypes, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self,nshares):
        self.shares -= nshares
        return self.shares

    def __repr__(self):
        # Note: The %r format code produces the repr() string
        return 'Stock(%r,%r,%r)' % (self.name, self.shares, self.price)

    def __eq__(self, other):
        return ((self.name, self.shares, self.price) ==
                (other.name, other.shares, other.price))

    def __lt__(self, other):
        return ((self.name, self.shares, self.price) <
                (other.name, other.shares, other.price))

    def __le__(self, other):
        return ((self.name, self.shares, self.price) <=
                (other.name, other.shares, other.price))

def read_portfolio(fileread):
    import csv
    portfolio = []
    with open(fileread) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            s = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(s)
    return portfolio



def print_portfolio(portfolio):
    '''
    Make a nicely formatted table showing stock data
    '''
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))

s = Stock('GOOG',100,490.10)
d = s.sell(25)
portfolio = read_portfolio('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\portfolio.csv')
for s in portfolio:
   print(s)

for s in portfolio:
    print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
print ("-"*40)
print_portfolio(portfolio)

print(getattr(s, 'name'))
setattr(s, 'shares', 50)
delattr(s, 'shares')

print(hasattr(s, 'name'))
print(hasattr(s, 'blah'))

s= Stock('GOOG', 100, 490.1)
fields = ['name','shares','price']
for name in fields:
    print(name, getattr(s, name))

row = ['AA', '100', '32.20']
s = Stock.from_row(row)
print (s.name)
print (s.shares)
print (s.price)
print (s.cost())

print("*"*40)
a = [1,9,4,25,16]
i = a.__iter__()
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(i.__next__())

