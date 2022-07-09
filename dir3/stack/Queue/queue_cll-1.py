class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class cqueue():
    def __init__(self):
        self.front = None
        self.rear = None

    def display(self):
        if self.front is None:
            print("It is an empty list")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data, "-->|", end=" ")
                temp = temp.next
                if temp == self.front:
                    break
            print("")

    def enqueue(self,data):
        end_n = Node(data)
        if self.front is None:
            end_n.next = end_n
            self.front = end_n
            self.rear = end_n
        else:
            self.rear.next = end_n
            end_n.next = self.front
            self.rear = end_n

    def dequeue(self):
        if self.front is None:
            print("LL is empty")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        else:
            self.rear.next = self.front.next
            self.front.next = None
            self.front = self.rear.next

    def size(self):
        if self.front is None:
            print("queue is empty")
        else:
            counter = 1
            temp = self.front
            while temp.next != self.front:
                counter += 1
                temp = temp.next
            print(counter)

    def is_empty(self):
        if self.front is None:
            print("True")
        else:
            print("False")

    def Front(self):
        if self.front is None:
            print("queue is empty")
        else:
            print(self.front.data)

    def Rear(self):
        if self.front is None:
            print("queue is empty")
        else:
            print(self.rear.data)

qu = cqueue()
qu.enqueue(1)
qu.enqueue(2)
qu.display()
qu.enqueue(4)
qu.enqueue(3)
qu.display()
qu.size()
qu.Front()
qu.Rear()
qu.is_empty()
qu.dequeue()
qu.display()
qu.dequeue()
qu.display()
qu.dequeue()
qu.display()
qu.dequeue()
qu.display()
qu.size()
qu.is_empty()