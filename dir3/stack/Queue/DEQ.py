class Dequeue:
    def __init__(self,limit):
        self.list = []
        self.limit = limit
        self.counter = 0

    def display(self):
        if not self.list:
            print("queue is empty")
        else:
            print(self.list)

    def insert_begin(self,data):
        if self.counter >= self.limit:
            print("queue is full")
        else:
            self.list.insert(0,data)
            self.counter += 1

    def insert_last(self,data):
        if self.counter >= self.limit:
            print("queue is full")
        else:
            self.list.append(data)
            self.counter += 1

    def delete_front(self):
        if not self.list:
            print("queue is empty")
        else:
            self.list.pop(0)
            self.counter -= 1

    def delete_last(self):
        if not self.list:
            print("queue is empty")
        else:
            self.list.pop()
            self.counter -= 1

    def front(self):
        if not self.list:
            print("queue is empty")
        else:
            print(self.list[0])

    def rear(self):
        if not self.list:
            print("queue is empty")
        else:
            print(self.list[-1])

    def is_empty(self):
        if not self.list:
            print("True")
        else:
            print("False")

    def size(self):
        print(len(self.list))

    def is_full(self):
        if self.counter >= self.limit:
            print("True")
        else:
            print("False")

dq = Dequeue(4)
dq.display()
dq.is_empty()
dq.insert_begin(2)
dq.insert_begin(1)
dq.display()
dq.insert_last(3)
dq.insert_last(5)
dq.display()
dq.is_full()
dq.insert_last(12)
dq.delete_front()
dq.delete_last()
dq.display()
dq.is_full()
dq.is_empty()
dq.size()
dq.front()
dq.rear()
dq.delete_last()
dq.delete_last()
dq.delete_front()