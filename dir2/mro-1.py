# MRO- method resolution order in multiple inheritence- left to right
class base1():
    def __init__(self):
        print("base1 class")

class base2():
    def __init__(self):
        print("base2 class")

class derived(base1,base2):
    pass

obj1 = derived()

class derived(base2,base1):
    pass

obj2 = derived()
