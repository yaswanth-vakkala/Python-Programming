class Parent():
    def func1(self):
        print("this is function 1")

class child(Parent):
    def func2(self):
        print("this is function 2")
        super().func1()

obj = child()
obj.func2()

class Parent():
    def func1(self):
        print("this is function 1")

class child(Parent):
    def func2(self):
        print("this is function 2")
        Parent.func1(self)

obj = child()
obj.func2()