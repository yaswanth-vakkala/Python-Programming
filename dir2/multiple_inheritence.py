class Parent1():
    def func1(self):
        print("this is functino 1")

class Parent2():
    def func2(self):
        print("this is function 2")

class child(Parent1,Parent2):
    def func3(self):
        print("this is function 3")

obj = child()

obj.func1()
obj.func2()
obj.func3()
