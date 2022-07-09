class methodoverload():
    def add(self,a=0,b=0,c=0):
        sum = a + b + c
        print("sum is",sum)

obj = methodoverload()
obj.add(5)
obj.add(5,10)
obj.add(5,5,10)

class methodoverload2():
    def add(self,a=None,b=None,c=None):
        if a != None and b!=None and c!=None:
            sum = a + b + c
            print("sum is",sum)
        elif a != None and b != None and c == None:
            sum = a + b
            print("sum is",sum)
        elif a != None and b == None and c == None:
            sum = a
            print("sum is",sum)
        else:
            print("arguments error")


obj = methodoverload2()
obj.add(5)
obj.add(5,15)
obj.add(5,5,10)