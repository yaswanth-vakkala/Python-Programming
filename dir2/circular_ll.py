class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class circular_ll():
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("It is an empty list")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
                if temp == self.head:
                    break
        print("")
    def insert_begin(self,data):
        begin_n = Node(data)
        if self.head is None:
            begin_n.next = begin_n
            self.head = begin_n
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            begin_n.next = self.head
            self.head = begin_n
            temp.next = self.head

    def insert_end(self,data):
        end_n = Node(data)
        if self.head is None:
            end_n.next = end_n
            self.head = end_n
        else:
            temp = self.head
            while temp.next is not self.head:
                temp = temp.next
            temp.next = end_n
            end_n.next = self.head
    def insert_position(self,data,index):
        initial_indx = 1
        temp = self.head.next
        while temp is not None:
            if initial_indx == index-1:
                break
            else:
                initial_indx += 1
                temp = temp.next
        if temp is None:
            print(index,"is not valid index")
        else:
            i_node = Node(data)
            i_node.next = temp.next
            temp.next = i_node

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.next == self.head:
            self.head = None
            self.head.next = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next

    def delete_end(self):
        if self.head is None:
            print("LL is empty")
        elif self.head.next == self.head:
            self.head = None
        else:
            temp = self.head.next
            prev = self.head
            while temp.next != self.head:
                temp = temp.next
                prev = prev.next
            prev.next = self.head

    def delete_position(self, pos):
        temp = self.head.next
        before = self.head
        for i in range(pos - 1):
            temp = temp.next
            before = before.next
        before.next = temp.next
    def delete_node(self,data):
        temp = self.head.next
        previous = self.head
        while temp is not None:
            if temp.data == data:
                break
            else:
                temp = temp.next
                previous = previous.next
        if temp is None:
            print(data, "is not present in linked list")
        else:
            previous.next = temp.next
            temp.next = None


obj  = circular_ll()
obj.display()
obj.insert_begin(2)
obj.insert_begin(1)
obj.display()
obj.insert_end(5)
obj.insert_end(10)
obj.display()
obj.insert_position(7,3)
obj.display()
obj.delete_begin()
obj.display()
obj.delete_end()
obj.display()
obj.insert_begin(1)
obj.insert_end(10)
obj.delete_node(7)
obj.display()
obj.delete_position(2)
obj.display()
