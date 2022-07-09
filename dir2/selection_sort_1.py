def selection_sort(list):
    for i in range(len(list)-1):
        low = i
        for j in range(i,len(list)):
            if list[j] < list[low]:
                low = j
        temp = list[i]
        list[i] = list[low]
        list[low] = temp
    return list

list = [5,2,1,3,4,7,6]
print(selection_sort(list))
