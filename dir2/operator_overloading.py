class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,other):
        return self.a + other.a


obj1 = A(10)
obj2 = A(5)
print(obj1 + obj2)
obj3 = A("gitam")
obj4 = A("university")
print(obj3+obj4)