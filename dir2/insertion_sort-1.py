def insertion_sort(list):
    for i in range(1,len(list)):
        for j in range(i):
            if list[j] > list[i]:
                list[j],list[i] = list[i],list[j]
    return list

list = [10,4,25,1,5,10,4]
print(insertion_sort(list))
