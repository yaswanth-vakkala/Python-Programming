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

    def delete_node(self,data):
            temp = self.head.next
            previous = self.head
            if previous.data == data:
                self.head = previous.next
                previous.next = None
            else:
                while temp is not None:
                    if temp.data == data:
                        break
                    else:
                        temp = temp.next
                        previous = previous.next
                if temp is None:
                    print(data, "is not present in linked list")
                else:
                    previous.next = temp.next
                    temp.next = None

    def dequeue(self):
        if self.head is None:
            print("The queue is empty")
        elif self.head.next is None:
            self.head = None
        else:
            min = self.head
            temp = self.head
            while temp.next is not None:
                if temp.data > min.data:
                    min = temp
                temp = temp.next
            self.delete_node(min.data)

    def getmin(self):
        if self.head is None:
            print("The queue is empty")
        else:
            min = self.head
            temp = self.head
            while temp.next is not None:
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
pq.enqueue(2)
pq.enqueue(1)
pq.display()
pq.enqueue(3)
pq.enqueue(4)
pq.display()
pq.dequeue()
pq.display()
pq.size()
pq.getmin()
pq.dequeue()
pq.display()
pq.dequeue()
pq.display()
pq.dequeue()
pq.display()