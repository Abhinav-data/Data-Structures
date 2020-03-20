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
        if(self.head.data == None):
            self.head = new_node
            new_node.next = self.head
            new_node.prev = self.head
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def Search(self, data):
        cur_pos = 1
        temp = self.head
        while(temp.next != self.head):
            if(temp.data == data):
                print("Found at", cur_pos)
                break
            else:
                cur_pos += 1
                temp = temp.next
        else:
            print("No node found")

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
myList.Search(10)
