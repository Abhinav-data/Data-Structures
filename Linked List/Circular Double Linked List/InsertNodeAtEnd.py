class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def InsertAtEnd(self, data):
        new_node = node(data)
        if(self.head.data is None):
            self.head = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            temp = self.head
            cur = self.head
            while(cur.next != self.head):
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        a = []
        temp = self.head
        a.append(str(temp.data))
        while(temp.next != self.head):
            temp = temp.next
            a.append(str(temp.data))
        print("<->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
