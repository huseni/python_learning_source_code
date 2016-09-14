__author__ = 'kathiria'

# tableformat.py
from abc import ABC, abstractmethod
from tableformat_new import  TableFormatter

class NewFormatter(ABC):
    @abstractmethod
    def headers(self, headings):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

    def __enter__(self):
        return self

    def __exit__(self, ty, val, tb):
        pass

f = NewFormatter()
print (f)
