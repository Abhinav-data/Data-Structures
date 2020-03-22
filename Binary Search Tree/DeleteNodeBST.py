class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def minValue(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current


def DeleteNode(root, data):
    if root is None:
        return root
    if(data < root.data):
        root.left = DeleteNode(root.left, data)

    elif(data > root.data):
        root.right = DeleteNode(root.right, data)

    else:
        if(root.left and root.right):
            pass
        elif(root.left is None):
            temp = root.right
            root = None
            return temp
        elif(root.right is None):
            temp = root.left
            root = None
            return temp

        temp = minValue(root.right)
        root.data = temp.data
        root.right = DeleteNode(root.right, temp.data)
    return root


def InsertNode(root, data):
    if root is None:
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

for i in range(1, 11):
    InsertNode(root, i)
InOrderTraversal(root)
print()
for i in range(3, 7):
    DeleteNode(root, i)
    print()
    InOrderTraversal(root)
