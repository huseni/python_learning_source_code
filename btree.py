__author__ = 'kathiria'


class BinaryTree(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_leftnode(self):
        return self.left

    def get_rightnode(self):
        return self.right

    def add_node(self, datanode, root):
        if(root == None):
            root = BinaryTree(datanode)
        if self.right == None:

            self.right = BinaryTree(datanode)

        elif self.left == None:
            self.left = BinaryTree(datanode)
        else:
            add_node(self.right,datanode)


    def __str__(self):
        return self.data

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data)
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.data)
            self.preorder(node.left)
            self.preorder(node.right)