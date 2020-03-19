class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = node()

    def InsertAtEnd(self, data):
        new_node = node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def DeleteLL(self):
        temp = self.head
        temp.next = None

    def display(self):
        a = []
        temp = self.head
        if(temp.next is None):
            print("NO Linked List")
        else:
            while(temp.next):
                temp = temp.next
                a.append(str(temp.data))
            print("->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.DeleteLL()
myList.display()
