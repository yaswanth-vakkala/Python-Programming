i = int(input("select one of the following operations that you wish to perform \n 1. ceil 2. floor 3. factorial "
              "4. sqrt 5. gcd 6. exponential 7. pow 8. remainder 9. lcm 10. distance bwn 2 points"
              "11. logarithm 12.  \n - "))

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