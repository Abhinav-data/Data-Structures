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
            cur = self.head
            while(cur.next != self.head):
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def InsertAtPos(self, data, pos):
        new_node = node(data)
        cur_pos = 1

        if(cur_pos >= pos):
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            new_node.prev = temp
            self.head = new_node
            return

        temp = self.head
        prv = self.head
        while(temp.next != self.head):
            if(cur_pos == pos):
                prv.next = new_node
                new_node.prev = prv
                new_node.next = temp
                temp.prev = new_node
                return
            else:
                cur_pos += 1
                prv = temp
                temp = temp.next
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            new_node.prev = temp
            return

    def display(self):
        temp = self.head
        a = []
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
myList.InsertAtPos(50, 5)
myList.display()
