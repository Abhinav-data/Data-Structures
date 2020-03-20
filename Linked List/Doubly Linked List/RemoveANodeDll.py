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

    def RemoveNode(self, data):
        temp = self.head
        while(temp):
            if(temp.data == data and temp == self.head):
                cur = self.head
                if(cur.next is None):
                    cur = None
                    cur.next = None
                    cur.prev = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    cur.prev = None
                    cur = None
                    self.head = nxt
                    return

            elif(temp.data == data):
                if(temp.next):
                    nxt = temp.next
                    prv = temp.prev
                    prv.next = nxt
                    nxt.prev = prv
                    temp.next = None
                    temp.prev = None
                    temp = None
                    return
                else:
                    prv = temp.prev
                    prv.next = None
                    temp.next = None
                    temp.prev = None
                    temp = None
                    return
            temp = temp.next

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
myList.RemoveNode(40)
myList.display()
