__author__ = 'kathiria'

import stock

# Print a table
def print_table(records, fields):
    # Print the table headers in a 10-character wide field
    for fieldname in fields:
        print('%10s' % fieldname, end=' ')
    print()

    # Print the separator bars
    print(('-'*10 + ' ')*len(fields))

    # Output the table contents
    for r in records:
        for fieldname in fields:
            print('%10s' % getattr(r, fieldname), end=' ')
        print()


portfolio = stock.read_portfolio('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\portfolio.csv')
print_table(portfolio, ['name','shares','price'])

print_table(portfolio,['shares','name'])
