__author__ = 'kathiria'

#from stock import Stock
import reader


class Stock(object):
    ...
    def __eq__(self, other):
        return ((self.name, self.shares, self.price) ==
                (other.name, other.shares, other.price))

    def __lt__(self, other):
        return ((self.name, self.shares, self.price) <
                (other.name, other.shares, other.price))

    def __le__(self, other):
        return ((self.name, self.shares, self.price) <=
                (other.name, other.shares, other.price))




#s = MyStock('GOOG', 100, 490.1)
#print (s)

portfolio = reader.read_csv(stock.Stock, 'C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\portfolio.csv')
print("*"*50)
print(portfolio)
print("*"*50)
portfolio.sort()
