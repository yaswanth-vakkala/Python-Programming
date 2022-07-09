class pQueue:
    def __init__(self):
        self.list = []
        self.counter = 0

    def display(self):
        print(self.list)

    def enqueue(self,data):
        self.list.append(data)

    def dequeue(self):
        if not self.list:
            print("The queue is empty")
        else:
            max = 0
            for i in range(len(self.list)):
                if self.list[i] > self.list[max]:
                    max = i
            del self.list[max]
    def getmax(self):
        if not self.list:
            print("queue is empty")
        else:
            max = 0
            for i in range(len(self.list)):
                if self.list[i] > self.list[max]:
                    max = i
            print(self.list[max])
    def size(self):
        self.counter = 0
        for i in self.list:
            self.counter += 1
        print(self.counter)

pq = pQueue()
pq.enqueue(1)
pq.enqueue(2)
pq.enqueue(3)
pq.enqueue(1)
pq.display()
pq.getmax()
pq.size()
pq.dequeue()
pq.size()
pq.display()
pq.dequeue()
pq.display()
pq.dequeue()
pq.display()
pq.dequeue()
pq.size()
pq.dequeue()
pq.getmax()

pq.enqueue((10,"zbc"))
pq.enqueue((10,"red"))
pq.enqueue((20,"cyan"))
pq.enqueue((10,"purple"))
pq.display()
pq.dequeue()
pq.display()
pq.getmax()
pq.size()
pq.dequeue()
pq.display()
pq.dequeue()
pq.dequeue()