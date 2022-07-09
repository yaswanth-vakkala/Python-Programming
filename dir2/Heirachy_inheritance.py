class Parent():
    def func1(self):
        print("this is function 1")

class child1(Parent):
    def func2(self):
        print("this is function 2")

class child2(Parent):
    def func3(self):
        print("this is function 3")

class child3(Parent):
    def func4(self):
        print("this is function 4")

o = child1()
i = child2()
j = child3()

o.func1()
o.func2()

i.func1()
i.func3()

j.func1()
j.func4()