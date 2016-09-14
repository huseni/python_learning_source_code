__author__ = 'kathiria'

import csv

def read_csv(cls, filename, skip_first=False):
    '''
    Read a CSV file into a list of instances. Instances are created using cls.from_row(row)
    '''
    records = []
    with open(filename) as f:
        f_csv = csv.reader(f)
        if skip_first:
            headers = next(f_csv)
        for row in f_csv:
            records.append(cls.from_row(row))
    return records
