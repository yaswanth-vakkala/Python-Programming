class Queue:
    def __init__(self):
        self.list = []
        self.rear = -1
        self.front = -1

    def display(self):
        for i in self.list:
            print(i,end=" ")
        print("\n")

    def enqueue(self,data):
        self.rear += 1
        self.list.append(data,self.rear)

    def dequeue(self):
        if self.list == []:
            return -1
        else:
            self.front+=1
            self.list.pop(self.front)
            self.rear-=1


i = int(input())
inp_list = []
for i in range(0,i):
    inp_list.append(input())

qu = Queue(i)
for k in inp_list:
    if k[0:2]=="en":
        qu.enqueue(k[k.find("(")+1:k.find(")")])
    elif k == "dequeue()":
        qu.dequeue()
    elif k=="display()":
        qu.display()
