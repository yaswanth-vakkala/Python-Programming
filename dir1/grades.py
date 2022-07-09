m = int(input("Enter your marks here: "))

if m >= 90 and m <= 100:
    print("you got A grade")
elif m >= 80 and m< 90:
    print("you got B grade")
elif m >= 70 and m< 80:
    print("you got C grade")
elif m >= 60 and m < 70:
    print("you got D grade")
elif m >= 50 and m < 60:
    print("you got E grade")
elif m >= 0 and m < 50 :
    print("you failed the test")
else:
    print("Invalid Value entered")