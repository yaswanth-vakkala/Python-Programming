class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack_ll:
    def __init__(self,limit):
        self.head = None
        self.count = 0
        self.limit = limit


    def display(self):
        if self.head is None:
            print("Stack is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
            print("")

    def push(self,data):
        if self.limit > self.count:
            begin_n = Node(data)
            self.count += 1
            if self.head is None:
                self.head = begin_n
            else:
                begin_n.next = self.head
                self.head = begin_n
        else:
            print("overflow error")
    def peek(self):
        if self.head is None:
            print("underflow error")
        else:
            print(self.head.data)
    def pop(self):
        if self.head is None:
            print("underflow error")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.count -= 1
    def isempty(self):
        if self.head is None:
            print("True")
        else:
            print("False")

    def isfull(self):
        if self.count >= self.limit:
            print("True")
        else:
            print("False")

    def size(self):
        if self.count >= self.limit:
            print("Stack is full with size of",self.count)
        elif self.head is None:
            print("Stack is empty")
        else:
            print("The size of stack is",self.count)
obj = Stack_ll(5)
obj.display()
obj.peek()
obj.pop()
obj.isempty()
obj.size()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.push(5)
obj.display()
obj.size()
obj.isfull()
obj.peek()
obj.pop()
obj.pop()
obj.display()
obj.isempty()
obj.isfull()
obj.size()
obj.display()
obj.push(6)
obj.push(7)
obj.display()
obj.pop()
obj.display()