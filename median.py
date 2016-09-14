__author__ = 'kathiria'

def median(iterable):

    items = sorted(iterable)
    if len(items) == 0:
        raise ValueError('Median() arg is an empty sequence')
    median_index = (len(items)-1)//2
    if len(items) % 2 != 0:
        return items[median_index]