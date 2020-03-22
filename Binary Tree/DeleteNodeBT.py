class node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


def LevelOrderTraversal(root):
    if root is None:
        return
    q = []
    x = 0
    q.append(root)
    while(len(q)):
        node = q.pop(0)
        print(node.data, end=" ")
        if(node.left):
            q.append(node.left)
        if(node.right):
            q.append(node.right)


def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)


def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.key == key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root


def InsertNode(root, data):
    q = []
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)

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

print("The tree before the deletion:")
LevelOrderTraversal(root)

root = deletion(root, 3)
print()
print("The tree after the deletion;")
LevelOrderTraversal(root)
