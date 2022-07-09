class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack_ll:
    def __init__(self,limit):
        self.head = None
        self.count = 0
        self.limit = limit

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
    def pop(self):
        if self.head is None:
            print("underflow error")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.count -= 1
            return temp.data

def reverse(string):
    ll = Stack_ll(len(string))
    list = ""
    for i in string:
        ll.push(i)
    for j in range(len(string)):
        list += ll.pop()
    print(list)

reverse("hello world")
reverse("delhi")
reverse("thailand")