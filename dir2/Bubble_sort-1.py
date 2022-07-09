def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp

    return list

list = [50,12,41,87,34]
print(bubble_sort(list))
