class circle():
    pi = 3.14
    def __init__(self,radius):
        self.r = radius
    def area_circle(self):
        ar = circle.pi * self.r * self.r
        print("area is",ar)

class square():
    def __init__(self,side):
        self.s = side
    def area_square(self):
        ar = self.s * self.s
        print("area is",ar)

obj1 = circle(5)
obj2 = square(5)

obj1.area_circle()
obj2.area_square()