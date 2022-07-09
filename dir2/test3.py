class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):

        self.x = 12
        self.y = 91

    def __str__(self):
        return str(self.x) + ","+str(self.y)

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point

print(p)
print(q)

print(p is q)
