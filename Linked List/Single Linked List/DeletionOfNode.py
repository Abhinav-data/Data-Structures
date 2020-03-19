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
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def display(self):
        a = []
        temp = self.head
        while(temp.next):
            temp = temp.next
            a.append(str(temp.data))
        print("->".join(a))

    def DeleteNode(self, pos):
        prev = node()
        c = 1
        temp = self.head
        while(temp):
            prev = temp
            temp = temp.next
            if(c == pos):
                prev.next = temp.next
                break
            c += 1


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.DeleteNode(2)
myList.display()
