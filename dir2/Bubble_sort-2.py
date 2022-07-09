class bsort():
    def array(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr
    def bubble_sort(self,list):
        for i in range(len(list)-1):
            for j in range(len(list)-1-i):
                if list[j] > list[j+1]:
                    temp = list[j+1]
                    list[j+1] = list[j]
                    list[j] = temp

        return list

list = [50,12,41,87,34]
obj = bsort()
print(obj.bubble_sort(obj.array()))
