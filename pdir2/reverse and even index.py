def zevenindex():
    main_list = []
    even_index_list = []
    rg = int(input("Enter the range of numbers for the list: "))
    for i in range(1, rg+1):
        main_list.append(i)
    print("The list with all elemnets:", main_list)
    main_list.reverse()
    print("The list with reversed elements:",main_list)
    print("List with even indexes:",main_list[2::2])
zevenindex()

