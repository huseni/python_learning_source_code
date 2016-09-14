__author__ = 'kathiria'

import unittest


def avrg(a,b,c):
    return a+b+c/3


class MyTests(unittest.TestCase):
    def test_average(self):
        self.assertEquals(avrg(1, 2, 3), 2, "Calculate the avg")
       # self.assertEquals(avg(1, 2, 3), 2, "Calculate the avg")
       # self.assertEquals(avg(1, 2, 3), 2, "Calculate the avg")

unittest.main()