def zdiv3list():
    div3_list = []
    rangez = int(input("Enter the range of numbers for the list : "))
    for i in range(1, rangez+1):
        div3_list.append(i)
    print("Before removing 3 divisibles:",div3_list)
    for i in div3_list:
        if i % 3 == 0:
            div3_list.remove(i)
    print("After removing 3 divisibles:",div3_list)
zdiv3list()

