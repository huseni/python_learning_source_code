__author__ = 'kathiria'

import time
import hashlib
import pickle
from itertools import chain
cache = {}


### Obsolete the data in the cache
def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


### Compute it
def compute_key(function, args, kw):
    key = pickle.dumps((function.func_name, args, kw))
    return hashlib.sha1(key).hexdigests()


### Cache it
def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            ### Check if we have it already
            if key in cache and not is_obsolete(cache[key], duration):
                print ("We got a winner")
                return cache[key]['value']

            ### Computing if we do not have it
            result = function(*args, **kw)

            ### Store the result
            cache[key] = {'value': result, 'time': time.time()}
            return result
        return __memoize
    return _memoize


@memoize()
def very_complex_stuff(a, b):
    """
    If computer gets to hot during this calculation, then stop it
    """
    return a + b
