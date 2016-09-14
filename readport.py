__author__ = 'kathiria'

from pprint import pprint

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        for line in f:
            fields = line.split()
            record = {
                'name' : fields[0],
                'shares' : int(fields[1]),
                'price' : float(fields[2])
                }
            portfolio.append(record)
    return portfolio

portfolio = read_portfolio('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\portfolio.dat')


def stock_name(s):
        return s['name']

def cost(s):
        return s['shares']*s['price']

def name_and_shares(s):
        return s['name'],s['shares']

def stock_price(s):
        return s['price']


portfolio.sort(key=stock_name)
portfolio.sort(key=cost,reverse=True)
portfolio.sort(key=name_and_shares)
pprint(portfolio)
print ("-" *50)
pprint(min(portfolio, key=stock_price))
pprint(max(portfolio, key=stock_price))

pprint(portfolio.sort(key=lambda s: s['name']))
pprint(portfolio.sort(key=lambda s: s['shares']*s['price']))
pprint(min(portfolio, key=lambda s: s['price']))

print ('*'*40)
cost = sum([s['shares']*s['price'] for s in portfolio])
print (cost)

more100 = [s for s in portfolio if s['shares'] > 100]
pprint(more100)

msftibm = [s for s in portfolio if s['name'] in ['MSFT','IBM']]
pprint(msftibm)

names = [s['name'] for s in portfolio]
print(names)

names = { s['name'] for s in portfolio }
print(names)

shares = dict.fromkeys(names, 0)
print(shares)
for s in portfolio:
    shares[s['name']] += s['shares']

print(shares)

values = ['1','2','-','3','N/A','4','5']
nums = [int(x) for x in values]
print(nums)

nums = [int(x) for x in values and x.isdigit()]
print(nums)