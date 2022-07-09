class linears():
    def arr(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr

    def find(self,arr):
        search = int(input("Enter the search element: "))
        for i in range(len(arr)):
            if arr[i] == search:
                print("element found at", i, "index value")
                break
        else:
            print("element not found")

obj = linears()
obj.find(obj.arr())
