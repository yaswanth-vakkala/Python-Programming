class Student():
    def __init__(self,name,nsubs,tmax,total):
        self.n = name
        self.nsubs = nsubs
        self.marks_array = []
        self.tmax = tmax
        self.total = total

    def assign(self):
        for i in range(self.nsubs):
            self.marks_array.append(int(input("enter the subject marks: ")))
    def compute(self):
        global avg
        for i in range(0,len(self.marks_array)):
            self.total = self.total + self.marks_array[i]
        for i in range(self.nsubs):
            self.tmax = self.tmax + 100
        avg = self.total / len(self.marks_array)

    def display(self):
        print(self.n,"has obtained",self.marks_array,"marks in each subject with total",self.total,"out of",self.tmax,"marks with average of",avg)

student1 = Student('loki',3,0,0)
student1.assign()
student1.compute()
student1.display()