def zevod():
    main_list = []
    even_list = []
    odd_list = []
    rg = int(input("Enter the range of numbers for the list: "))
    for i in range(1, rg+1):
        main_list.append(i)
    for j in main_list:
        if j % 2 == 0:
            even_list.append(j)
        elif j % 2 != 0:
            odd_list.append(j)
    print("Even list is :",even_list)
    print("Odd list is :",odd_list)
zevod()
