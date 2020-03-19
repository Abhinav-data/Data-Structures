class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def InsertAtEnd(self, data):
        new_node = node(data)
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def display(self):
        a = []
        temp = self.head
        while temp.next != None:
            temp = temp.next
            a.append(str(temp.data))
        print("->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
