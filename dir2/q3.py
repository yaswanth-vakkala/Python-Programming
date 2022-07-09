class Student():
    def __init__(self,name,marks):
        self.n = name
        self.m = marks
    def assign(self):
        global total,tmax
        total = 0
        tmax = 600
    def compute(self):
        global total,average
        total = 0
        for i in self.m:
            total = total + i
        average = total / len(self.m)
    def display(self):
        print(self.n,"has scored a total marks of",total,"out of",tmax,"marks","with average of",average)

obj = Student("harish",[100,100,100,100,100,100])
obj.assign()
obj.compute()
obj.display()