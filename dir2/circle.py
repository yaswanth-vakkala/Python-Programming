class Circle:
    PI = 3.14159
    def __init__(self,radius):
        self.r = radius
    def area(self):
        area = self.PI * self.r * self.r
        return area
    def circumference(self):
        circum = 2 * self.PI * self.r
        return circum

c = Circle(5)
print("the area of circle is",c.area())
print("circumference of circle is",c.circumference())
