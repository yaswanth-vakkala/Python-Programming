class employees:
    no = 0
    def __init__(self,name,designation,salary):
         employees.no = employees.no + 1
         self.n = name
         self.d = designation
         self.s = salary
    def display(self):
        print("the total no of employees =",employees.no)
        print("the",employees.no,"employee name is",self.n,"their designation is",self.d,"and thier salary is",self.s,"k rupees")

e1 = employees("sham","intern",15)
e1.display()
e2 = employees("ram","manager",50)
e2.display()
print(employees.no)
