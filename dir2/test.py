class shape():
    def area(self,a=None,b=None):
        if a == None and b == None:
            return 0
        elif a!= None and b == None:
            return  a * a
        elif a == None and b != None:
            return b * b
        elif a!= None and b!= None:
            return a * b
        else:
            print("something went wrong")

obj = shape()
print(obj.area())
print(obj.area(2))
print(obj.area(b=3))
print(obj.area(2,3))
