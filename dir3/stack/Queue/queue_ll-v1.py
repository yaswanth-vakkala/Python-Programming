class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self,limit):
        self.head = None
        self.limit = limit
        self.front = -1
        self.rear = -1
        self.counter = 0
        self.lcounter = 0

    def display(self):
        if self.head is None:
            print("Queue is empty")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
            print("")

    def enqueue(self,data):
        end_n = Node(data)
        if self.head == None:
            self.head = end_n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = end_n
        self.rear += 1
        if self.counter == 0:
            self.front += 1
            self.counter += 1
        self.lcounter += 1
    def dequeue(self):
        if self.head is None:
            print("underflow error")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            del temp
            self.front += 1
            self.lcounter -= 1
    def is_empty(self):
        if self.front > self.rear or self.head is None:
            print("True")
        else:
            print("False")
    def is_full(self):
        if self.lcounter >= self.limit:
            print("True")
        else:
            print("False")
    def size(self):
        if self.lcounter >= self.limit:
            print("The queue is full with size of",self.lcounter)
        elif self.front > self.rear or self.head is None:
            print("Queue is empty")
        else:
            print("The size of queue is",self.lcounter)

qu = Queue(4)
qu.display()
qu.size()
qu.dequeue()
qu.is_empty()
qu.enqueue(1)
qu.enqueue(2)
qu.display()
qu.enqueue(3)
qu.display()
qu.size()
qu.dequeue()
qu.display()
print(qu.front)
print(qu.rear)
qu.is_empty()
qu.is_full()
qu.display()
qu.enqueue(4)
qu.enqueue(5)
qu.display()
qu.is_full()
qu.size()