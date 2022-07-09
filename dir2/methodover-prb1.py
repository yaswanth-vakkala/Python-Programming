class Rectangle():
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        ar = self.l * self.b
        print("the area of retangle is",ar)

class Square(Rectangle):
    def __init__(self,s):
        self.s = s

    def area(self):
        ar = self.s * self.s
        print("the area of square",ar)

obj1 = Rectangle(6,2)
obj1.area()

obj2 = Square(3)
obj2.area()
