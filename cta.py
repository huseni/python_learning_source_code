__author__ = 'kathiria'

from collections import Counter
import readrides


rides = readrides.read_rides_as_dicts()
rides_by_route = Counter()
for ride in rides:
    rides_by_route[ride['route']] + = ride['numrides']

most_common = rides_by_route.most_common()
for rank, (route, numrides) in enumerate(most_common,1):
    print('#5d  %5s  %10d' % (rank, route, numrides))
