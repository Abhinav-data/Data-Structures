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
            new_node.next = new_node
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def Delete(self, pos):
        cur_pos = 1
        prev_node = node()
        temp = self.head
        while(temp.next != self.head):
            if(cur_pos != pos):
                prev_node = temp
                temp = temp.next
                cur_pos += 1
            else:
                prev_node.next = temp.next
                break

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
myList.Delete(2)
myList.display()
