i = int(input("For which diagram do you want to find area \n 1. circle 2. rectangle \n : "))

if i == 1:
    r = float(input("Enter the radius of the circle: "))
    a = 3.14 * r * r
    print(a)
elif i == 2:
    l = float(input("Enter the length of rectangle: "))
    b = float(input("Enter the breadth of rectangle: "))
    a = l * b
    print(a)
else:
    print("Invalid Option Selected")
