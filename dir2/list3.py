class linears():
    def arr(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr

    def find(self,arr):
        indexes = []
        search = int(input("Enter the search element: "))
        for i in range(len(arr)):
            if arr[i] == search:
                indexes.append(i)
        return indexes

obj = linears()
indx = obj.find(obj.arr())
if indx == []:
    print("element not found")
else:
    for i in indx:
        print("element found at index",i)