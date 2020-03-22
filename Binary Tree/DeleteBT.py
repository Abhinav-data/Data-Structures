class node:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None


def LevelOrderTraversal(root):
    if(root is None):
        print("No tree found")
        return
    q = []
    q.append(root)
    while(len(q)):
        node = q.pop(0)
        print(node.data, end=" ")
        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)


def InsertNode(root, data):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if(temp.left):
            q.append(temp.left)
        else:
            temp.left = node(data)
            break
        if(temp.right):
            q.append(temp.right)
        else:
            temp.right = node(data)
            break


root = node(0)
for i in range(1, 11):
    InsertNode(root, i)
LevelOrderTraversal(root)
print()
root = None
LevelOrderTraversal(root)
