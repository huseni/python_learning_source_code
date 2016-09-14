__author__ = 'kathiria'


class Custom(object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)
]


def getKey(custom):
    return custom.number


def main():
    customlist = [
    Custom('object', 99),
    Custom('michael', 1),
    Custom('theodore the great', 59),
    Custom('life', 42)
    ]
    sorted(customlist, key=getKey)


