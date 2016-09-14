__author__ = 'kathiria'

# coticker.py
from structure import Structure
from descrip import String, Integer, Float

class Ticker(Structure):
    name = String()
    price =Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import coroutine, follow
from tableformat import create_formatter
import csv

# This one is tricky. See solution for notes about it
@coroutine
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield
        target.send(next(reader))

@coroutine
def create_ticker(target):
    while True:
        row = yield
        target.send(Ticker.from_row(row))

@coroutine
def negchange(target):
    while True:
        record = yield
        if record.change < 0:
            target.send(record)

@coroutine
def ticker(fmt, fields):
    formatter = create_formatter(fmt)
    formatter.headings(fields)
    while True:
        rec = yield
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)
