class Bike:
    def __init__(self,color,price):
        self.color = color
        self.price = price
    def display(self):
        print("color of bike is:",self.color)
        print("price of bike is:",self.price)


Testone = Bike('blue',49.99)
Testone.display()

Testtwo = Bike("purple",25.0)
Testtwo.display()
