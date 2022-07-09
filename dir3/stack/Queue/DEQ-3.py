class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def display(self):
        if self.front is None:
            print("It is an empty dq")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,"-->|",end="")
                temp = temp.next
            print("")

    def insert_begin(self,data):
        begin_n = Node(data)
        if self.front is None:
            self.front = begin_n
            self.rear = begin_n
        else:
            begin_n.next = self.front
            self.front.prev = begin_n
            self.front = begin_n

    def insert_end(self,data):
        end_n = Node(data)
        if self.front is None:
            self.front = end_n
            self.rear = end_n
        elif self.front.next == None:
            self.front.next = end_n
            end_n.prev = self.front
            self.rear = end_n
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = end_n
            end_n.prev = temp
            self.rear = end_n

    def delete_begin(self):
        if self.front is None:
            print("dq is emtpy")
        elif self.front.next == None:
            self.front = None
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            self.front.prev = None

    def delete_end(self):
        if self.front is None:
            print("dq is empty")
        elif self.front.next == None:
            self.front = None
        else:
            prev = self.front
            temp = self.front.next
            while temp.next is not None:
                temp = temp.next
                prev = prev.next
            prev.next = None
            temp.prev = None

    def is_empty(self):
        if self.front is None:
            print("True")
        else:
            print("False")

    def Front(self):
        if self.front is None:
            print("DEQ is empty")
        else:
            print(self.front.data)

    def Rear(self):
        if self.front is None:
            print("DEQ is empty")
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            print(temp.data)

    def size(self):
        counter = 0
        temp = self.front
        while temp is not None:
            counter += 1
            temp = temp.next
        print(counter)


dq =  DQueue()
dq.display()
dq.insert_begin(3)
dq.display()
dq.insert_begin(2)
dq.insert_end(4)
dq.display()
dq.delete_end()
dq.delete_begin()
dq.display()
dq.delete_end()
dq.display()
dq.is_empty()
dq.size()
dq.insert_end(1)
dq.Front()
dq.Rear()
dq.insert_end(2)
dq.Rear()
dq.size()