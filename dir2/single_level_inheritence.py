class Parent():
    def func1(self):
        print("this is function 1")

class child(Parent):
    def func2(self):
        print("this is function 2")

o = child()

o.func1()
o.func2()