class AppleBasket:
    def __init__(self,color,quantity):
        self.apple_color = color
        self.apple_quantity = quantity

    def increase(self):
        self.apple_quantity = self.apple_quantity + 1
        return self.apple_quantity

    def __str__(self):
        return "A basket of "+str(self.apple_quantity)+" "+self.apple_color+" apples."

t1 = AppleBasket('red',10)
print(t1)
t1.increase()
print(t1)

t2 = AppleBasket('green',4)
print(t2)
t2.increase()
print(t2)