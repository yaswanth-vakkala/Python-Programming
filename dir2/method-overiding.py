class Parent():
    def func1(self):
        print("this is function 1")

class child(Parent):
    def func1(self):
        print("this is function 2")
        Parent.func1(self)

obj = child()
obj.func1()