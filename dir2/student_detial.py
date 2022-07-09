class Students:
    def __init__(self,name):
        self.n = name
        self.marks = []
    def entermarks(self):
        for i in range(3):
            inp = input("Enter you marks in subject "+str(i+1)+" :")
            self.marks.append(inp)
        return self.marks
    def display(self):
        print(self.n,"your marks in 3 subjects are",self.marks)
s1 = Students('hari')
s1.entermarks()
s1.display()

s2 = Students("vinod")
s2.entermarks()
s2.display()
