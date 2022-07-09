class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class stack():
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("It is an empty linked list")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
        print("")

    def push(self,data):
        begin_n = Node(data)
        if self.head is None:
            self.head = begin_n
        else:
            begin_n.next = self.head
            self.head.prev = begin_n
            self.head = begin_n

    def pop(self):
        if self.head is None:
            print("underflow error")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.head.prev = None

    def peek(self):
        if self.head is None:
            print("underflow error")
        else:
            print(self.head.data)

    def is_empty(self):
        if self.head is None:
            print("True")
        else:
            print("False")

    def size(self):
        counter = 0
        temp = self.head
        while temp is not None:
            counter+=1
            temp=temp.next
        print(counter)

ds = stack()
ds.size()
ds.is_empty()
ds.push(3)
ds.push(2)
ds.display()
ds.push(1)
ds.display()
ds.pop()
ds.display()
ds.is_empty()
ds.size()
ds.peek()
