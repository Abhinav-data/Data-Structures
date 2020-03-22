class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def InsertNode(root, data):
    if(root is None):
        root = node(data)
    elif(data <= root.data):
        root.left = InsertNode(root.left, data)
    elif(data > root.data):
        root.right = InsertNode(root.right, data)

    return root


def InOrderTraversal(root):
    if root:
        InOrderTraversal(root.left)
        print(root.data, end=" ")
        InOrderTraversal(root.right)


root = node(5)
for i in range(0, 11):
    InsertNode(root, i)
InOrderTraversal(root)
root = None
print()
InOrderTraversal(root)
