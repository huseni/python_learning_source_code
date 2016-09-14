__author__ = 'kathiria'

from reader import read_csv
from stock import Stock



class Ride(object):
         def __init__(self, route, date, daytype, numrides):
             self.route = route
             self.date = date
             self.daytype = daytype
             self.numrides = numrides
         @classmethod
         def from_row(cls, row):
             return cls(row[0], row[1], row[2], int(row[3]))


rides = read_csv(Ride, 'C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\ctabus.csv', skip_first=True)
len(rides)