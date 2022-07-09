def zdivlist():
    div_list = []
    choice = input("Enter whether you want numbers divisible by a.)2 or b.)4 (select an option) : ")
    rangez = int(input("Enter the range of numbers for the list : "))
    for i in range(rangez+1):
        if (choice == 'a' and i % 2 == 0) and i!= 0:
            div_list.append(i)
        elif (choice == 'b' and i % 4 == 0) and i!= 0:
            div_list.append(i)
    print(div_list)
zdivlist()
