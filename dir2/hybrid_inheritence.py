class Parent1():
    def func1(self):
        print("this is function 1")

class Parent2():
    def func2(self):
        print("this is function 2")

class child1(Parent1):
    def func3(self):
        print("this is function 3")

class child2(Parent2, child1):
    def func4(self):
        print("this is function 4")

o = child2()
o.func1()
o.func2()
o.func3()
o.func4()
