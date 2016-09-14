__author__ = 'kathiria'

import urllib.requests
url = 'http://diveintopython3.org/examples/feed.xml'
data =  urllib.requests.urlopen(url).read()
type(data)