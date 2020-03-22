class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    if(root is None):
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


def SearchNode(root, data):
    if(root is None):
        return
    q = []
    q.append(root)
    while(len(q)):
        if(q[0].data == data):
            print("Node found in tree")
            break
        node = q.pop(0)
        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)
    else:
        print("No node found")


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

LevelOrderTraversal(root)
print()
SearchNode(root, 11)
