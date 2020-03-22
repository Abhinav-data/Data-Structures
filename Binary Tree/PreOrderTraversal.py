class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def PreOrderTraversal(root):
    if(root):
        print(root.data, end=" ")
        PreOrderTraversal(root.left)
        PreOrderTraversal(root.right)


def InsertNode(root, data):
    new_node = node(data)
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if(temp.left is None):
            temp.left = new_node
            break
        else:
            q.append(temp.left)

        if(temp.right is None):
            temp.right = new_node
            break

        else:
            q.append(temp.right)


root = node(0)
for i in range(1, 11):
    InsertNode(root, i)

PreOrderTraversal(root)
