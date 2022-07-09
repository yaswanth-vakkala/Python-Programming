class Complex():
    def __init__(self,real,img):
        self.r = real
        self.i = img

    def __add__(self, other):
        rpart = self.r + other.r
        ipart = self.i + other.i
        comp = complex(rpart,ipart)
        return comp

o1 = Complex(5,2)
o2 = Complex(3,4)
print(o1+o2)

o3 = Complex(4,5)
o4 = Complex(2,9)
print(o3+o4)

