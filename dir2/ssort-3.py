class ssort():
    def array(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr
    def selection_sort(self,list):
        for i in range(len(list) - 1):
            for j in range(i + 1, len(list)):
                if list[j] < list[i]:
                    temp = list[i]
                    list[i] = list[j]
                    list[j] = temp
        return list

list = [5,2,1,3,4,7,6,120,51]
obj = ssort()
print(obj.selection_sort(obj.array()))

