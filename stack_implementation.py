__author__ = 'kathiria'


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


def rev_string(st):
    s = Stack()

    for ch in st:
        s.push(ch)

    revstr =''
    while not s.is_empty():
        revstr = revstr + s.pop()
    return revstr


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol )

        else:
            if s.is_empty():
                balanced = False


def para_checker(para):
    index = 0
    balanced = True
    s = Stack()
    while index < len(para) and balanced:
        # If any element of string contains '(' at the beginning, then push that in the stack
        if para[index] == '(':
            s.push(para[index])
        else:
            # If stack is empty, nothing to balance
            if s.is_empty():
                balanced = False
            else:
                # Cleanup the stack if anything other than '(' in the stack
                s.pop()
        index += 1
    if balanced and s.is_empty():
        return True
    else:
        return False


def binary_to_decimal(dec_number):
    s = Stack()
    while dec_number > 0:
        rem = dec_number % 2
        s.push(rem)
        dec_number = dec_number/2

    bstring = ""
    while not s.is_empty():
        bstring = bstring + str(s.pop())
    return bstring


def base_converter(decnum, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while decnum > 0:
        rem = decnum % base
        s.push(rem)
        decnum = decnum // base

    revstr = ""
    while not s.is_empty():
        revstr = revstr + digits[s.pop()]
    return revstr





def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print (s.peek())
    print (binary_to_decimal(3))
    print (base_converter(26 , 26))

if __name__ == '__main__':
    main()


















