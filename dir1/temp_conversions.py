i = int(input("Select an option: \n 1. Fahrenheit to celsius 2. Celsius to Fahrenheit 3. celsius to kelvin 4. Fahrenheit to kelvin\n - "))
t = float(input("Enter the temperature: "))
if i == 1:
    t = 5 * t/9 - 160 / 9
    print(format(t,".2f"),"C")
elif i == 2:
    t = (t*9/5) + 32
    print(format(t, ".2f"), "F")
elif i ==3:
    t = t + 273.15
    print(format(t, ".2f"), "K")
elif i ==4:
    t = (t - 32) * 5/9 + 273.15
    print(format(t, ".2f"), "K")
else:
    print("Invalid option selected")