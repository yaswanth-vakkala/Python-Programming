import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dist_2points(self):
        dist = math.sqrt(self.x**2+self.y**2)
        print("The distance from origin to point is:",dist)

p1 = Point(4,2)
p1.dist_2points()
p2 = Point(2,2)
p2.dist_2points()

