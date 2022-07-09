import math

def ceil():
    # rounds to the closest high integer
    n = float(input("Enter a number on which you want to perform ceil func: "))
    print(math.ceil(n))
def cpsign():
    n1 = float(input("Enter the target number: "))
    n2= float(input("Enter the source number: "))
    print(math.copysign(n1, n2))
def pow():
    n1 = int(input("Enter the number: "))
    n2 = int(input("Enter the power to which you want to rise: "))
    print(math.pow(n1, n2))
def log():
    # performs log with base e
    n = float(input("Enter the number: "))
    print(math.log(n))
def floor():
    # rounds to the closest low integer
    n = float(input("Enter the number: "))
    print(math.floor(n))
def sqrt():
    n = float(input("Enter the number: "))
    print(math.sqrt(n))
def lcm():
    n1 = int(input("Enter the number1: "))
    n2 = int(input("Enter the number2: "))
    print(math.lcm(n1, n2))
def gcd():
    n1 = int(input("Enter the number1: "))
    n2 = int(input("Enter the number2: "))
    print(math.gcd(n1, n2))
def fact():
    n = int(input("Enter the number: "))
    print(math.factorial(n))
def degree():
    n = float(input("Enter the radians: "))
    print(math.degrees(n))
def rads():
    n = float(input("Enter the degrees: "))
    print(math.radians(n))
def remainder():
    n1 = int(input("Enter the number1: "))
    n2 = int(input("Enter the number2: "))
    print(math.remainder(n1, n2))
def sin():
    n = float(input("Enter the number: "))
    print(math.sin(n))
def cos():
    n = float(input("Enter the number: "))
    print(math.cos(n))

i = int(input("select one of the following operations that you wish to perform \n 1. ceil 2. copysign 3. pow 4. log 5. floor 6. sqrt"
              "7. rads to degrees 8. lcm 9. gcd 10. factorial \n11. sin 12. degrees to rads 13. cos 14. remainder of 2 digits \n :-: "))
if i == 1:
    ceil()
elif i == 2:
    cpsign()
elif i == 3:
    pow()
elif i == 4:
    log()
elif i == 5:
    floor()
elif i == 6:
    sqrt()
elif i == 7:
    degree()
elif i == 8:
    lcm()
elif i == 9:
    gcd()
elif i == 10:
    fact()
elif i == 11:
    sin()
elif i == 12:
    rads()
elif i == 13:
    cos()
elif i == 14:
    remainder()
else:
    print("Invalid Input")

import math
print(math.ceil(1.01))
print(math.copysign(-3, 5))
print(math.pow(5, 3))
print(math.log(2)) # to base e
print(math.floor(5.9))
print(math.sqrt(36))
print(math.degrees(22))
print(math.lcm(12,18))
print(math.gcd(10, 72))
print(math.factorial(5))
print(math.sin(30))
print(math.radians(30))
print(math.cos(30))
print(math.remainder(12, 4))