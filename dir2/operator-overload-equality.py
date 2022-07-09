class equality():
    def __init__(self,val):
        self.val = val

    def __eq__(self, other):
        if self.val == other.val:
            return True
        else:
            return False

obj1 = equality(2)
obj2 = equality(12)
if(obj1==obj2):
    print(obj1.val,"is equal to",obj2.val)
else:
    print(obj1.val,"is not equal to",obj2.val)


obj3 = equality(10)
obj4 = equality(10)
if(obj3==obj4):
    print(obj3.val,"is equal to",obj4.val)
else:
    print(obj3.val,"is not equal to",obj4.val)
