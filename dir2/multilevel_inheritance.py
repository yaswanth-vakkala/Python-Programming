class Parent():
    def func1(self):
        print("this is function 1")

class child1(Parent):
    def func2(self):
        print("this is function 2")

class child2(child1):
    def func3(self):
        print("this is functiion 3")

o = child2()
o.func1()
o.func2()
o.func3()