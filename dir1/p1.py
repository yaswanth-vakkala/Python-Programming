n1 = int(input("Enter the first integer number: "))
n2 = int(input("Enter the second integer number: "))
i = int(input("select one of the following operations that you wish to perform \n 1. addition 2. subtraction 3. multiplication "
              "4. float division 5. integer division 6. exponential 7. modulus 8. average \n - "))

if i == 1:
    n = n1 + n2
    print(n)
elif i == 2:
    n = n1 - n2
    print(n)
elif i == 3:
    n = n1 * n2
    print(n)
elif i == 4:
    n = n1 / n2
    print(n)
elif i == 5:
    n = n1//n2
    print(n)
elif i == 6:
    n = n1 ** n2
    print(n)
elif i == 7:
    n = n1 % n2
    print(n)
elif i == 8:
    n = (n1 + n2)/2
    print(n)
else:
    print("Invalid option")