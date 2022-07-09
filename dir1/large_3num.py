n1 = float(input("Enter the 1st number: "))
n2 = float(input("Enter the 2st number: "))
n3 = float(input("Enter the 3rd number: "))

if n1 > n2 and n1 > n3:
    print(n1, "is greater than", n2, "and", n3)
elif n2>n1 and n2>n3:
    print(n2, "is greater than", n1, "and", n3)
elif n3 > n1 and n3 > n2 :
    print(n3,"is greater than", n1, "and", n2)