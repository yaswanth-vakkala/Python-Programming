class Person():
    def __init__(self,name,id,age):
        self.n = name
        self.id = id
        self.age = age
    def display(self):
        print("The id no "+str(self.id)+" name is "+self.n+ " of age "+str(self.age))


class Employee(Person):
    def __init__(self,name,id,age,salary):
        super().__init__(name,id,age)
        self.salary = salary

    def display(self):
        super().display()
        print("The salary of the employee is",self.salary)

obj = Employee("jake",432,25,"50k")
obj.display()


