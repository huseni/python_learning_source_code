__author__ = 'kathiria'

#How many bus routes exist in Chicago?
# What is the total number of rides taken on each bus route?
# What bus route numbers existed in 2001, but no longer exist in 2013?
# What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

import csv


def read_rides_in_dict(filename = None):
    my_dict = {}

    with open('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\ctabus.csv' , 'r') as f:
        for line in f:
            items = line.split()
            key, values = items[0], items[1:]
            my_dict[key] = values
    return my_dict



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

if __name__ == '__main__':
    import os
    total_rides = read_rides_in_dict()

    print (total_rides)
   # print('Look at memory use of PID', os.getpid())