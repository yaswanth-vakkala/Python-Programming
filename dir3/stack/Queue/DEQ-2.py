class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Dqueue:
    def __init__(self,limit):
        self.front = None
        self.rear = None

    def display(self):
        if self.front is None:
            print("It is an empty DEQ")
        else:
            temp = self.front
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
        print("")

    def insert_begin(self, data):
        begin_n = Node(data)
        if self.front is None:
            self.front = begin_n
        else:
            begin_n.next = self.front
            self.front = begin_n

    def insert_end(self,data):
        end_n = Node(data)
        if self.front == None:
            self.front = end_n
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            temp.next = end_n

    def delete_front(self):
        if self.front is None:
            print("Linked list is empty")
        else:
            temp  = self.front
            self.front = temp.next
            temp.next = None

    def delete_last(self):
        if self.front is None:
            print("dq is empty")
        elif self.front.next is None:
            self.front = None
        else:
            previous = self.front
            temp = self.front.next
            while temp.next is not None:
                temp = temp.next
                previous = previous.next
            previous.next = None

    def is_empty(self):
        if self.front is None:
            print("True")
        else:
            print("False")

    def Front(self):
        if self.front is None:
            print("DEQ is empty")
        else:
            print(self.front.data)

    def Rear(self):
        if self.front is None:
            print("DEQ is empty")
        else:
            temp = self.front
            while temp.next is not None:
                temp = temp.next
            print(temp.data)

    def size(self):
        counter = 0
        temp = self.front
        while temp is not None:
            counter += 1
            temp = temp.next
        print(counter)


dq = Dqueue(4)
dq.insert_end(1)
dq.insert_end(2)
dq.display()
dq.insert_begin(0)
dq.delete_front()
dq.delete_last()
dq.display()
dq.delete_last()
dq.display()
dq.is_empty()
dq.size()
dq.insert_end(1)
dq.Front()
dq.Rear()
dq.insert_end(2)
dq.Rear()
dq.size()