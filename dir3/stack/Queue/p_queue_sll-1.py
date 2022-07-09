class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class pqueue:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("It is an empty linked list")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data, "-->|", end=" ")
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

    def dequeue(self):
        if self.head is None:
            print("The queue is empty")
        elif self.head.next is None:
            self.head = None
        else:
            min = self.head
            temp = self.head
            while temp is not None:
                if temp.data < min.data:
                    min = temp
                temp = temp.next
            temp1 = self.head.next
            prev1 = self.head
            while temp1 is not None:
                if prev1.data is min.data:
                    self.head = prev1.next
                    prev1.next = None
                    prev1 = self.head
                else:
                    if temp1.data is min.data:
                        prev1.next = temp1.next
                        temp1.next = None
                temp1 = temp1.next
                prev1 = prev1.next

    def getmin(self):
        if self.head is None:
            print("The queue is empty")
        else:
            min = self.head
            temp = self.head
            while temp is not None:
                if temp.data < min.data:
                    min = temp
                temp = temp.next
            print(min.data)

    def size(self):
        counter = 0
        temp = self.head
        while temp is not None:
            counter += 1
            temp = temp.next
        print(counter)

pq = pqueue()
pq.enqueue(20)
pq.enqueue(11)
pq.enqueue(1)
pq.enqueue(101)
pq.display()
pq.enqueue(3)
pq.enqueue(41)
pq.display()
pq.dequeue()
pq.display()
pq.size()
pq.getmin()
pq.dequeue()
pq.display()
pq.dequeue()
pq.display()
pq.getmin()
pq.dequeue()
pq.display()
pq.getmin()
pq.dequeue()
pq.display()
pq.getmin()
pq.dequeue()
pq.display()