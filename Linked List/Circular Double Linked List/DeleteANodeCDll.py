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
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head.prev = new_node

    def Delete(self, pos):
        cur_pos = 1
        if(cur_pos >= pos):
            temp = self.head
            nxt = self.head.next
            while(temp.next != self.head):
                temp = temp.next
            nxt.prev = temp
            temp.next = nxt
            self.head = nxt
            return
        else:
            temp = self.head
            prev = self.head
            while(temp.next != self.head):
                if(cur_pos == pos):
                    nxt = temp.next
                    prev.next = nxt
                    nxt.prev = prev
                    return
                else:
                    prev = temp
                    temp = temp.next
                    cur_pos += 1
            else:
                prev.next = self.head
                self.head.prev = prev
                return

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
myList.Delete(4)
myList.display()
