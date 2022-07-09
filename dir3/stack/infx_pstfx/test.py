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
            return False
        else:
            return self.list.pop()

    def peek(self):
        if self.list == []:
            return False
        else:
            return self.list[-1]

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
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
def infx_postfx(expression):
    stk = Stack(len(expression))
    operators = [")","(","^","*","/","+","-"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    presedence = {
        "(": 1,
        ")": 2,
        "^":3,
        "/": 4,
        "*": 5,
        "-": 6,
        "+": 7,
    }
    postfx = ""
    for i in expression:
        if i in alphabets:
            postfx += i
        elif i in operators and stk.isempty():
            stk.push(i)
        elif presedence[i] < presedence[stk.peek()]:
            stk.push(i)
        elif presedence[i] > presedence[stk.peek()]:
            while presedence[i] > presedence[stk.peek()]:
                postfx += stk.pop()
        elif presedence[i] == presedence[stk.peek()]:
            if i == "^":
                stk.push(i)
    while True:
        if stk.isempty() is not True:
            postfx+= stk.pop()
        else:
            break
    print(postfx)

infx_postfx("a+b/c+e*c")