__author__ = 'kathiria'

def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter(object):
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError

    def __enter__(self):
        return self

    def __exit__(self, ty, val, tb):
        pass

class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print('%10s' % h, end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print('%10s' % d, end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end=' ')
        for h in headers:
            print('<th>%s</th>' % h, end=' ')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end=' ')
        for d in rowdata:
            print('<td>%s</td>' % d, end=' ')
        print('</tr>')

    def __enter__(self):
        print('<table>')
        return self

    def __exit__(self, ty, val, tb):
        print('</table>')

def create_formatter(name):
    if name == 'text':
        formatter = TextTableFormatter
    elif name == 'csv':
        formatter = CSVTableFormatter
    elif name == 'html':
        formatter = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    return formatter()

# Sample
if __name__ == '__main__':
    import stock
    import reader
    portfolio = reader.read_csv(stock.Stock, 'C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\portfolio.csv')
    textformatter = TextTableFormatter()
    cvsformatter = CSVTableFormatter()
    htmlformatter = HTMLTableFormatter()


    print("-"*50)
    print_table(portfolio,['name','shares','price'], textformatter)
    print("-"*50)
    print_table(portfolio,['name','shares','price'], cvsformatter)
    print("-"*50)
    print_table(portfolio,['name','shares','price'], htmlformatter)
    print("-"*50)
    formatter = create_formatter('html')
    print_table(portfolio, ['name','shares','price'], formatter)

    print("-"*50)
    with create_formatter('html') as formatter:
        print_table(portfolio, ['name','shares','price'], formatter)

