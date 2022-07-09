class pQueue:
    def __init__(self):
        self.list = []
        self.counter = 0

    def display(self):
        print(self.list)

    def enqueue(self,data):
        self.list.append(data)
        self.list.sort()

    def dequeue(self):
        if not self.list:
            print("queue is empty")
        else:
            self.list.pop(0)

    def getmin(self):
        if not self.list:
            print("queue is empty")
        else:
            print(self.list[0])

    def size(self):
        self.counter = 0
        for i in self.list:
            self.counter += 1
        print(self.counter)

pq = pQueue()
pq.enqueue(10)
pq.enqueue(20)
pq.enqueue(30)
pq.display()
pq.dequeue()
pq.display()
pq.getmin()
pq.size()
pq.dequeue()
pq.dequeue()
pq.dequeue()

pq.enqueue((10,"red"))
pq.enqueue((20,"cyan"))
pq.enqueue((10,"purple"))
pq.display()
pq.dequeue()
pq.display()
pq.getmin()
pq.size()
pq.dequeue()
pq.dequeue()
pq.dequeue()