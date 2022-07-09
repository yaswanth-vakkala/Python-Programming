class Test:
    def __init__(self):
        self.pub = "public variable"
        self.__priv = "private variable"
        self._prot = "protected variable"
    def acc(self):
        print("this is", self._prot)

p = Test()
print("public variable is ",p.pub)
print("private variable is",p._Test__priv)
p.acc()
