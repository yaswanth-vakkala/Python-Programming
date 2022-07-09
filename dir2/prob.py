class person():
    def __init__(self,name,age):
        self.n = name
        self.a = age
    def display(self):
        print(self.n,self.a)

class publications():
    def __init__(self,no_rp,no_bks):
        self.rps = no_rp
        self.bks = no_bks
    def display(self):
        print(self.rps,self.bks)

class faculty(person):
    def __init__(self,name,age,desgn,dept,rps,bks):
        self.desgn = desgn
        self.dept = dept
        person.__init__(self,name,age)
        self.pubs = publications(rps,bks)
    def display(self):
        person.display(self)
        self.pubs.display()
        print(self.desgn,self.dept)


obj = faculty("alex",20,"professor","cse",12,2)
obj.display()
