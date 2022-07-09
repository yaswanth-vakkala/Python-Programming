class circle():
    pi = 3.14
    def __init__(self,radius):
        self.r = radius
    def area(self):
        ar = circle.pi * self.r * self.r
        print("area is",ar)

class square(circle):
    def __init__(self,side):
        self.s = side
    def area(self):
        ar = self.s * self.s
        print("area is",ar)

def find_area(obj):
    obj.area()
obj1 = circle(5)
obj2 = square(5)

find_area(obj1)
find_area(obj2)