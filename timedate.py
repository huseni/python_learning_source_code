__author__ = 'kathiria'

import sys
import datetime
from time import gmtime, strftime
from datetime import timedelta

def daterange(start_date, end_date):
   for n in range(int ((end_date - start_date).days)):
       start_date=start_date + datetime.timedelta(n)

       for i in range (1,23):
             print  start_date + timedelta(hours=hr)


start_date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d").date()
end_date = datetime.datetime.strptime(sys.argv[2], "%Y%m%d").date()
#for single_date in daterange(start_date, end_date):
#    print strftime("%Y%m%d", single_date.timetuple())
print ','.join(strftime("%Y%m%d%H", single_date.timetuple()) for single_date in daterange(start_date, end_date))