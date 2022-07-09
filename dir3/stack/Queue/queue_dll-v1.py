class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self,limit):
        self.limit = limit
        self.front = None
        self.rear = None
        self.lcounter = 0

    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
            print("")

    def enqueue(self,data):
        end_n = Node(data)
        if self.rear == None:
            self.front = end_n
            self.rear = end_n
        else:
            self.rear.next = end_n
            self.rear.next.prev = self.rear
            self.rear = end_n
    def dequeue(self):
        if self.front is None:
            print("underflow error")
        elif self.front.next == None:
            temp = self.front
            self.front = temp.next
            del temp
        else:
            temp = self.front
            self.front = temp.next
            self.front.prev = None
            del temp
    def Front(self):
        if self.front is None:
            print("underflow error")
        else:
            print(self.front.data)
    def Rear(self):
        if self.rear == None:
            print("queue is empty")
        else:
            print(self.rear.data)

    def is_empty(self):
        if self.front == None:
            print("True")
        else:
            print("False")

    def size(self):
        count = 0
        temp = self.front
        while temp is not None:
            count += 1
            temp = temp.next
        print("size of queue is",count)

qu = Queue(4)
qu.enqueue(1)
qu.enqueue(2)
qu.display()
qu.enqueue(3)
qu.display()
qu.dequeue()
qu.display()
qu.dequeue()
qu.display()
qu.enqueue(4)
qu.enqueue(5)
qu.Front()
qu.display()
qu.Rear()
qu.is_empty()
qu.size()
qu.dequeue()
qu.size()
qu.dequeue()
qu.size()
qu.display()
qu.dequeue()
qu.size()
qu.dequeue()
qu.display()