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

    def InsertAtPos(self, data, pos):
        temp = self.head
        cur_pos = 1
        new_node = node(data)
        if(pos == 1):
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next):
                if(cur_pos == pos):
                    if(temp.next):
                        nxt = temp.next
                        prv = temp.prev
                        prv.next = new_node
                        new_node.next = temp
                        temp.next = nxt
                        break
                temp = temp.next
                cur_pos += 1
            else:
                temp.next = new_node
                new_node.prev = temp
                new_node.next = None

    def display(self):
        temp = self.head
        a = []
        a.append(str(temp.data))
        while(temp.next):
            temp = temp.next
            a.append(str(temp.data))
        print("<->".join(a))


myList = LinkedList()
myList.InsertAtEnd(10)
myList.InsertAtEnd(20)
myList.InsertAtEnd(30)
myList.InsertAtEnd(40)
myList.display()
myList.InsertAtPos(50, 10)
myList.display()
