class node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def InOrderTraversal(root):
    if(root):
        InOrderTraversal(root.left)
        print(root.data, end=" ")
        InOrderTraversal(root.right)


def InsertNode(root, data):
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if(not temp.left):
            temp.left = node(data)
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right = node(data)
            break
        else:
            q.append(temp.right)


root = node(0)
for i in range(1, 11):
    InsertNode(root, i)

InOrderTraversal(root)
