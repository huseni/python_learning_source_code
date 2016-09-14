__author__ = 'kathiria'
import datetime
import itertools
import time
import random

class Sensor:
    def __iter__(self):
        return self

    def __next__(self):
        return random.random()


sensor = Sensor()
timestamp = iter(datetime.datetime.now, None)

for stamp, value in itertools.islice(zip(timestamp,sensor),10):
    print(stamp, value)
    time.sleep(1)

