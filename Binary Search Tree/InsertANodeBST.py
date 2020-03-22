from random import randint


class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def InsertNode(root, data):
    if root is None:
        root = node(data)
    elif(data <= root.data):
        root.left = InsertNode(root.left, data)
    else:
        root.right = InsertNode(root.right, data)
    return root


def InOrderTraversal(root):
    if(root):
        InOrderTraversal(root.left)
        print(root.data, end=" ")
        InOrderTraversal(root.right)


root = node(5)
for i in range(0, 10):
    InsertNode(root, i)
InOrderTraversal(root)
