class Ad:
    def __click(self):
        print("you clicked on a ad")

ads = Ad()
ads._Ad__click()

class Area:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def __area(self):
        return self.l * self.b
    def print(self):
        print(self.__area())
obj = Area(5,2)
obj.print()

