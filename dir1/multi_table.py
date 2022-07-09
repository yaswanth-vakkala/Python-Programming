i = int(input("Enter the number: "))
r = int(input("Enter the range of multiplication: "))

for n in range(r+1):
    table = n * i
    if table == 0:
        pass
    else:
        print(table)