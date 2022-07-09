def quadroot():
    print("Enter the coefficients values in quadratic equation form ax**2+by+c")
    a = int(input("Enter the value of a: "))
    b = int(input("Enter the value of b: "))
    c = int(input("Enter the value of c: "))
    d = b**2 - 4*a*c
    if d>0:
        print("roots are real")
    elif d == 0:
        print("roots are equal")
    else:
        print("roots are imaginary")

quadroot()
