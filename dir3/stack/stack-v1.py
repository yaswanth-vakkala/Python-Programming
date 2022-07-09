class Stack:
    def __init__(self):
        self.list = []

    def display(self):
        print(self.list)

    def push(self,element):
        self.list.append(element)

    def pop(self):
        if self.list == []:
            print("underflow error")
        else:
            self.list.pop()

    def peek(self):
        if self.list == []:
            print("underflow error")
        else:
            print(self.list[-1])

    def isempty(self):
        if self.list == []:
            print("True")
        else:
            print("False")

obj = Stack()
obj.isempty()
obj.peek()
obj.pop()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.display()
obj.pop()
obj.display()
obj.peek()
obj.isempty()
