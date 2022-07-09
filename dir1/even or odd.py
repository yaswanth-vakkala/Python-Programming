try:
    n = int(input("Enter the number : "))
    if n % 2 == 0:
        print(n, "is an even number")
    elif n % 2 != 0 :
        print(n, "is an odd number")
except:
    print("Invalid Input")
