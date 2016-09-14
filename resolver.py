__author__ = 'kathiria'

import socket
from timeit import timeit

class Resolver:

    def __init__(self):
        self.mycache = {}  # create a dictionary call cache #

    def __call__(self, host):
        print " Calling the __call__"
        if host not in self.mycache:
            self.mycache[host] = socket.gethostbyname(host)
        return self.mycache[host]

    def clear(self):
        self.mycache.clear()

    def has_host(self, host):
        return host in self.mycache


