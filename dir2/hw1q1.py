class Student:
    collegename = "gitam university"
    def __init__(self,name,rollno,course):
        self.name = name
        self.rollno = rollno
        self.course = course
    def display(self):
        print("name of the student is",self.name)
        print("roll no is",self.rollno)
        print("course is",self.course)
        print("collge is",self.collegename)

s1 = Student("kim",143,"cse")
s1.display()

s2 = Student("jake",122,"ece")
s2.display()