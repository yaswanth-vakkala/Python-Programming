class Company():
    def __init__(self,cname,cproj):
        self.cname = cname
        self._cproj = cproj

class Employee(Company):
    def __init__(self,ename,esal,cname,cproj):
        Company.__init__(self,cname,cproj)
        self.ename = ename
        self.__esal = esal

    def show_sal(self):
        print("The salary of",self.ename,"is",self.__esal,'rupees')

obj = Employee("richard",2000,"ivory","trader")
print("welcome to",obj.cname)
obj.show_sal()

