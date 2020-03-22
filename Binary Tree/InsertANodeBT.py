class newNode():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    if root is None:
        return
    q = []
    q.append(root)
    while(len(q)):
        print(q[0].data, end=" ")
        node = q.pop(0)

        if(node.left is not None):
            q.append(node.left)

        if(node.right is not None):
            q.append(node.right)


def InsertNode(root, data):
    q = []
    q.append(root)
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if (not temp.left):
            temp.left = newNode(data)
            break
        else:
            q.append(temp.left)

        if (not temp.right):
            temp.right = newNode(data)
            break
        else:
            q.append(temp.right)


root = newNode(0)
for i in range(1, 10):
    InsertNode(root, i)

LevelOrderTraversal(root)
