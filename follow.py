__author__ = 'kathiria'

# Reading a stock exchange ticker updates through generator #

import os
import time

def trace_logs(filename):
    """
    Generator that produces a sequence of lines being written at the end of a file.
    """

    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
             line = f.readline()
             if line == '':
                 time.sleep(0.1)    # Sleep briefly to avoid busy wait
                 continue
             yield line

# Example use
if __name__ == '__main__':
    for line in trace_logs('C:\\Users\\kathiria\\Desktop\\Advanced Python\\pythonmaster\\pythonmaster\\Data\\stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))


#for line in trace_install_logs('Data/stocklog.csv'):
#    print(line, end='')
