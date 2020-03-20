class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def InsertAtEnd(self, data):
        new_node = node(data)
        if(self.head.data is None):
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def SearchFor(self, data):
        cur_pos = 1
        temp = self.head
        while(temp.next != self.head):
            if(temp.data == data):
                print("found at", cur_pos)
                break
            else:
                temp = temp.next
                cur_pos += 1
        else:
            print("No node found")

    def display(self):
        a = []
        temp = self.head
        a.append(str(temp.data))
        while(temp.next != self.head):
            temp = temp.next
            a.append(str(temp.data))
        print("->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.SearchFor(60)
