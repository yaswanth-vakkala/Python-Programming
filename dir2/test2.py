class base1():
    def __init__(self,a):
        self.a = a
        print("base1 class")
        print("a=",self.a)
        super().__init__(30)
class base2():
    def __init__(self,b):
        self.b = b
        print("base2 class")
        print("b=",self.b)

class derived(base1,base2):
    def __init__(self,c):
        self.c = c
        print("derived class")
        print("c=",self.c)
        super().__init__(20)

obj = derived(10)