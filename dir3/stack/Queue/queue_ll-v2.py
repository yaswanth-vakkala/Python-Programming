class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
        if self.lcounter < self.limit:
            end_n = Node(data)
            if self.rear == None:
                self.front = end_n
                self.rear = end_n
            else:
                self.rear.next = end_n
                self.rear = end_n
            self.lcounter += 1
        else:
            print("overflow error")
    def dequeue(self):
        if self.front is None:
            print("underflow error")
        else:
            temp = self.front
            self.front = temp.next
            temp.next = None
            del temp
            self.lcounter -= 1
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
    def is_full(self):
        if self.lcounter >= self.limit:
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

# qu = Queue(4)
# qu.enqueue(1)
# qu.enqueue(2)
# qu.display()
# qu.enqueue(3)
# qu.display()
# qu.dequeue()
# qu.display()
# qu.Front()
# qu.Rear()
# qu.is_empty()
# qu.size()
# qu.dequeue()
# qu.size()
# qu.dequeue()
# qu.size()
# qu.dequeue()
# class Menu:
#     def __init__(self,option,text):
#         self.option = option
#         self.text = text
#     def display(self):
#         print("select",self.option,"for",self.text)
#         input
#
# o1 = Menu(1,"displaying the result")
# o1.display()

def Menu():
    limit = int(input("Enter the max size of queue you want: "))
    qu = Queue(limit)
    while True:
        option = int(input("select one of the options below:\n 1. display the Queue \n 2. enQueue \n 3. deQueue \n 4. display the front element"
                           "\n 5. display the rear element \n 6. empty check on Queue \n 7. check if Queue is full \n 8. find the size of Queue"
                           "\n 9. quit \n ::--> "))
        if option == 1:
            qu.display()
        elif option == 2:
            data = input("Enter the input data: ")
            qu.enqueue(data)
        elif option == 3:
            qu.dequeue()
        elif option == 4:
            qu.Front()
        elif option == 5:
            qu.Rear()
        elif option == 6:
            qu.is_empty()
        elif option == 7:
            qu.is_full()
        elif option == 8:
            qu.size()
        elif option ==9:
            break
        else:
            print("Invalid Input")
Menu()