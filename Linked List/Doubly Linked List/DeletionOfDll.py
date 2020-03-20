class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def InsertAtEnd(self, data):
        new_node = node(data)
        if(self.head is None):
            self.head = new_node
            new_node.next = None
            new_node.prev = None
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node
            new_node.next = None
            new_node.prev = temp

    def DeleteDll(self):
        self.head.next = None
        self.head.prev = None
        self.head = None

    def display(self):
        a = []
        temp = self.head
        if(temp):
            a.append(str(temp.data))
            while(temp.next):
                temp = temp.next
                a.append(str(temp.data))
            print("<->".join(a))
        else:
            print("No List Found")


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.DeleteDll()
myList.display()
