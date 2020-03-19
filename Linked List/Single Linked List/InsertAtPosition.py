class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
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

    def InsertAtPosition(self, data, pos):
        new_node = node(data)
        cur_pos = 1
        prev = node()
        temp = self.head
        while temp.next:
            prev = temp
            temp = temp.next
            if(cur_pos == pos):
                prev.next = new_node
                new_node.next = temp
                return
            cur_pos += 1

    def display(self):
        a = []
        temp = self.head
        while(temp):
            a.append(str(temp.data))
            temp = temp.next
        print("->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.InsertAtPosition(50, 1)
myList.display()
