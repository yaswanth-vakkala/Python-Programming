class car:
    age = 17
    def __init__(self,m,c):
        self.m = m
        self._c = c

obj = car("breeza","14l")

print(obj.m)
print(obj._c)
print(car.age)
obj.age = 20
print(obj.age)