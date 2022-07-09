class Minheap:
    def __init__(self):
        self.n = 0
        self.l = []
    def insert(self,value):
        self.l.append(value)
        i = self.n
        while(i>0):
            parent = (i-1)//2
            if self.l[parent] > self.l[i]:
                self.l[parent],self.l[i] = self.l[i],self.l[parent]
            i = parent
        self.n = self.n + 1

    def display(self):
        print(self.l)

mh = Minheap()
mh.insert(20)
mh.insert(3)
mh.insert(7)
mh.insert(9)
mh.insert(133)
mh.insert(100)
mh.display()
