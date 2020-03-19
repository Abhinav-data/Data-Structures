class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = node(data)
        temp = self.head
        if(self.head is None):
            self.head = new_node
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node

    def InsertAtBeginning(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        a = []
        temp = self.head
        while(temp != None):
            a.append(str(temp.data))
            temp = temp.next
        print("->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(300)
myList.InsertAtEnd(40)
myList.InsertAtBeginning(410)
myList.display()
