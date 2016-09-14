__author__ = 'kathiria'

import requests
import time
import asyncore



url_list = ['https://randomtask.usa.hp.com:8443/dma', 'http://www.amazon.com', 'http://ibm.com', 'http://www.apple.com']
uid = "autotest"
pwd = "autotest"

start = time.time()
for url in url_list:
    print url
    url_link = requests.get(url, auth=(uid, pwd))
    print(url_link.headers)


print('elapsed time : %s' % (time.time() - start))

