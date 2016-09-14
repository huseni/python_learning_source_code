__author__ = 'kathiria'


class ExprNode(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self):
        if self.value == "+":
            return self.left.evaluate() + self.right.evaluate()

        if self.value == "-":
            return self.left.evaluate() - self.right.evaluate()

        if self.value == "*":
            return self.left.evaluate() * self.right.evaluate()

        if self.value == "/":
            return self.left.evaluate() / self.right.evaluate()

        else:
            return self.value

my_expr = ExprNode('*', ExprNode('+', ExprNode(2), ExprNode(6)), ExprNode(4))
#  (2+3) * (4) = 20

print(my_expr.evaluate())


class BinaryNode(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.right = right
        self.left = left

    def search(self, value):
        if self.value == value:
            return True
        else:
            if value < self.left:
                if self.left is not None:
                    return self.left.search(value)
                else:
                    return False
            else:
                if self.right is not None:
                    return self.left.right.search(value)
                else:
                    return False

    def insert(self, item):
        if self.value == item:
            return
        else:
            if item < self.value:
                if self.left is not None:
                    self.left.insert(item)
                else:
                    self.left = BinaryNode(item)
            else:
                if self.right is not None:
                    self.right.insert(item)
                else:
                    self.right = BinaryNode(item)


bn = BinaryNode()