class linears():
    def __init__(self,arr):
        self.arr = arr
    def find(self,search):
        for i in range(len(self.arr)):
            if self.arr[i] == search:
                print("element found at", i, "index value")
                break
        else:
            print("element not found")

obj = linears([1,2,3,4])
obj.find(1)
obj.find(4)
obj.find(5)
obj.find(12)
