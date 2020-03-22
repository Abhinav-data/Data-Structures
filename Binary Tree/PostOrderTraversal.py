class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def PostOrderTraversal(root):
    if root:
        PostOrderTraversal(root.left)
        PostOrderTraversal(root.right)
        print(root.data, end=" ")


def InsertNode(root, data):
    new_node = node(data)
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)

        if(not temp.left):
            temp.left = new_node
            break
        else:
            q.append(temp.left)

        if(not temp.right):
            temp.right = new_node
            break
        else:
            q.append(temp.right)


root = node(0)
for i in range(1, 11):
    InsertNode(root, i)

PostOrderTraversal(root)
