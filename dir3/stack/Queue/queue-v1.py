class Queue:
    def __init__(self,limit):
        self.list = []
        self.front = -1
        self.rear = -1
        self.counter = 0
        self.limit = limit

    def display(self):
        print(self.list)

    def enqueue(self,data):
        if len(self.list) >= self.limit:
            print("overflow error")
        else:
            self.list.append(data)
            self.rear += 1
            if self.counter == 0:
                self.front += 1
                self.counter += 1

    def dequeue(self):
        if self.list == []:
            print("underflow error")
        else:
            self.list.pop(0)
            self.front += 1
    def is_empty(self):
        if len(self.list) == 0:
            print("True")
        else:
            print("False")
    def is_full(self):
        if len(self.list) >= self.limit:
            print("True")
        else:
            print("False")

    def size(self):
        if len(self.list) >= self.limit:
            print("The queue is full with size of",len(self.list))
        elif len(self.list) == 0:
            print("The queue is empty")
        elif self.list:
            print("size of queue is",len(self.list))

qu = Queue(4)
qu.display()
qu.dequeue()
qu.size()
qu.is_empty()
qu.enqueue(1)
qu.enqueue(2)
qu.enqueue(3)
qu.display()
qu.size()
qu.is_full()
qu.dequeue()
qu.dequeue()
qu.display()
print(qu.rear)
print(qu.front)
qu.enqueue(4)
qu.enqueue(5)
qu.enqueue(6)
qu.display()
qu.enqueue(8)
qu.is_full()
print(qu.rear)
print(qu.front)
qu.is_empty()
qu.size()
