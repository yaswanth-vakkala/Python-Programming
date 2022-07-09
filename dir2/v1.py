# classes and objects
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def setage(self, Age):
        self.age = Age
        return Age

d1=Dog("lop", 8)
d2=Dog("kim", 9)
print(d1.getage())
d1.getname()
print(d2.setage(10))



class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max):
        self.name = name
        self.max = max
        self.students = []
    def add(self, student):
        if len(self.students) <= self.max:
            self.students.append(student)
            return True
        return False

    def avgg(self):
        pass

s1= Student("jim", 19, 93)
s2=Student("kim", 23, 100)
s3=Student("jake", 24, 50)

course = Course("chem", 2)
course.add(s1)
course.add(s2)
print(course.students[0].name)
'''
# inheritence
'''
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")
    def speak(self):
        print("Idk")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("meow")
    def show(self):
        print(f"I am {self.name} and i am {self.age} and i am {self.color}")

class Dog(Pet):
    def speak(self):
        print("bark")
class Fish(Pet):
        pass

p = Pet("kim", 2)
p.show()
c = Cat("jill", 23, "orange")
c.speak()
c.show()
d=Dog("tom", 5)
d.speak()
d.show()
f = Fish("bubble", 5)
f.speak()
f.show()
'''
# note - self is an attribute for object reference
#static and class methods and attributes
# class attributes
'''
class Person:
    no_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.no_of_people += 1
p1 = Person("tim")
print(Person.no_of_people)
p2 = Person("kim")
print(Person.no_of_people)
'''
#class methods
'''
class Person:
    no_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
    @classmethod
    def no_of_person(cls):
        return cls.no_of_people
    @classmethod
    def add_person(cls):
        cls.no_of_people += 1

p1 = Person("tim")
p2 = Person("kim")
print(Person.no_of_person())
'''
#static methods
'''
class Math:
    @staticmethod
    def add5(x):
        return x+5

print(Math.add5(5))
'''