def selection_sort(list):
    for i in range(len(list)-1):
        for j in range(i+1,len(list)):
            if list[j] < list[i]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    return list

list = [5,2,1,3,4,7,6,120,51,2]
print(selection_sort(list))
