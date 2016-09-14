__author__ = 'kathiria'

from abc import ABC, abstractmethod

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
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

class ColumnFormatMixin(object):
    formats = []
    def row(self, rowdata):
        rowdata = [ (fmt % item) for fmt, item in zip(self.formats, rowdata)]
        super(ColumnFormatMixin, self).row(rowdata)

class ColumnReprMixin(object):
    def row(self, rowdata):
        rowdata = [ repr(item) for item in rowdata ]
        super(ColumnReprMixin, self).row(rowdata)

def create_formatter(name, column_formats=None, use_repr=False):
    if name == 'text':
        formatter = TextTableFormatter
    elif name == 'csv':
        formatter = CSVTableFormatter
    elif name == 'html':
        formatter = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class column_formatter(ColumnFormatMixin, formatter):
              formats = column_formats
        return column_formatter()

    elif use_repr:
        class repr_formatter(ColumnReprMixin, formatter):
            pass
        return repr_formatter()

    else:
        return formatter()

