__author__ = 'kathiria'

import csv

def read_rides(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        date = row[1]
        daytype = row[2]
        numrides = int(row[3])
        ride = (route, date, daytype, numrides)
        rides.append(ride)
    f.close()
    return rides


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)
    for row in f_csv:
        route = row[0]
        datefields = row[1].split('/')
        date = (int(datefields[2]), int(datefields[0]), int(datefields[1]))   # (year, mon, day)
        daytype = row[2]
        numrides = int(row[3])
        ride = {
            'route': route,
            'date': date,
            'daytype': daytype,
            'numrides' : numrides
            }
        rides.append(ride)
    f.close()
    return rides


def read_rides_as_dicts(filename):
    '''
    Read the bus ride data as a list of dicts
    '''
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        datefields = row[1].split('/')
        daytype = row[2]
        numrides = int(row[3])
        ride = {
            'route': route,
            'year': int(datefields[2]),
            'month': int(datefields[0]),
            'day': int(datefields[1]),
            'daytype': daytype,
            'numrides' : numrides
            }
        rides.append(ride)
    f.close()
    return rides


if __name__ == '__main__':
    import os
    rides = read_rides('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\ctabus.csv')
    print('Look at memory use of PID', os.getpid())

