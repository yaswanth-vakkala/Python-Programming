class Queue:
    def __init__(self,limit):
        self.list = []

    def display(self):
        for i in self.list:
            print(i,end="")
        print("")

    def enqueue(self,data):
        self.list.append(data)

    def dequeue(self):
        if self.list == []:
            return -1
        else:
            self.list.pop(0)


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
