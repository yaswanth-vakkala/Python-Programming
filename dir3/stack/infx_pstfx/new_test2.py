class Stack:
    def __init__(self,len):
        self.list = []
        self.len = len

    def push(self,element):
        if len(self.list) >= self.len:
            print("overflow error")
        else:
            self.list.append(element)

    def pop(self):
        if self.list == []:
            print("underflow error")
        else:
            return self.list.pop()

    def peek(self):
        if self.list == []:
            print("underflow error")
        else:
            return self.list[-1]

    def isempty(self):
        if self.list == []:
            return True
        else:
            return False
    def isfull(self):
        if len(self.list) == self.len:
            return True
        else:
            return False
    def size(self):
        if len(self.list) == self.len:
            print("stack is full with size of",len(self.list))
        elif self.list == []:
            print("size of stack is zero")
        elif self.list:
            print("size of stack is",len(self.list))

def infx_postfx(expression):
    stk = Stack(len(expression))
    operators = ["^", "*", "/", "+", "-"]
    paranths = ["(",")"]
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    presedence = {
        # "(": 1,
        # ")": 2,
        "^": 1,
        "/": 2,
        "*": 2,
        "+": 3,
        "-": 3,
    }
    postfx = ""
    for i in expression:
        if i.lower() in alphabets:
            postfx += i
        elif i in paranths:
            if i =="(":
                stk.push(i)
            elif i ==")":
                p = stk.pop()
                while p != "(":
                    postfx += p
                    if stk.isempty():
                        break
                    p = stk.pop()
                    if p == "(":
                        break
        elif i in operators:
            if stk.isempty() or stk.peek() == "(":
                stk.push(i)
            elif not stk.isempty() and presedence[i] < presedence[stk.peek()]:
                stk.push(i)
            elif not stk.isempty() and presedence[i] > presedence[stk.peek()]:
                while not stk.isempty():
                    if stk.peek() == "(":
                        stk.push(i)
                        break
                    elif i == ")":
                        p = stk.pop()
                        while p != "(":
                            postfx += p
                            p = stk.pop()
                            if p == "(":
                                break
                    elif presedence[i] > presedence[stk.peek()]:
                        postfx += stk.pop()
                    elif presedence[i] == presedence[stk.peek()]:
                        postfx += stk.pop()
                        stk.push(i)
                        break
                    elif presedence[i] < presedence[stk.peek()]:
                        stk.push(i)
                        break
                    else:
                        postfx += i
                        break
                if stk.isempty():
                    stk.push(i)
            elif presedence[i] == presedence[stk.peek()]:
                if i == "^":
                    stk.push(i)
                else:
                    postfx += stk.pop()
                    stk.push(i)
    while True:
        if stk.isempty() is not True:
            postfx+= stk.pop()
        else:
            break
    print(postfx.upper())

infx_postfx("a-b/c*d+e")
infx_postfx("A*B+C")
infx_postfx("A+B*C")
infx_postfx("A*B+C*D")
infx_postfx("A*B^C+D")
infx_postfx("A*(B+C*D)+E")
infx_postfx("A+(B*C-(D/E^F)*G)*H")
infx_postfx("(A+B)*C+D/(E+F*G)-H")
infx_postfx("A-B-C*(D+E/F-G)-H")
infx_postfx("a+b*(c^d-e)^(f+g*h)-i")
infx_postfx("A+B-C*D")
infx_postfx("(a+b-c)*d-(e+f)")
infx_postfx("a+b^c-d*e/f-g/h-i")
infx_postfx("a-b*c+(d-e)*f/g/h")
infx_postfx("a^b*c/(d*e-f)")