class greater():
    def __init__(self,val):
        self.val = val

    def __gt__(self, other):
        if self.val > other.val:
            return True
        else:
            return False

obj1 = greater(2)
obj2 = greater(12)
if(obj1>obj2):
    print(obj1.val,"is greater than",obj2.val)
else:
    print(obj1.val,"is not greater than",obj2.val)


obj3 = greater(10)
obj4 = greater(4)
if(obj3>obj4):
    print(obj3.val,"is greater than",obj4.val)
else:
    print(obj3.val,"is not greater than",obj4.val)
