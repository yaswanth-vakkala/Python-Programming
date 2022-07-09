class Stack:
    def __init__(self,len):
        self.list = []
        self.len = len

    def display(self):
        print(self.list)

    def display_reverse(self):
        r_list = []
        for i in range(len(self.list)-1,-1,-1):
            r_list.append(self.list[i])
        print(r_list)

    def push(self,element):
        if len(self.list) >= self.len:
            print("overflow error")
        else:
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
    def isfull(self):
        if len(self.list) == self.len:
            print("True")
        else:
            print("False")
    def size(self):
        if len(self.list) == self.len:
            print("stack is full with size of",len(self.list))
        elif self.list == []:
            print("size of stack is zero")
        elif self.list:
            print("size of stack is",len(self.list))


obj = Stack(4)
obj.isempty()
obj.size()
obj.peek()
obj.pop()
obj.push(1)
obj.push(2)
obj.push(3)
obj.push(4)
obj.display()
obj.pop()
obj.size()
obj.display()
obj.peek()
obj.isempty()
obj.push(4)
obj.display()
obj.push(5)
obj.isfull()
obj.size()
obj.display_reverse()
