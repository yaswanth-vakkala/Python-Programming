class base1():
    def __init__(self):
        print("base1 class")
        super().__init__()

class base2():
    def __init__(self):
        print("base2 class")
        super().__init__()

class base3():
    def __init__(self):
        print("base3 class")

class derived(base1,base2,base3):
    pass

obj1 = derived()
