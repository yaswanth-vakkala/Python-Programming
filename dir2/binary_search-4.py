class binary():
    def array(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr
    def binarys(self,arr,low,high,s):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] < s:
                return binary.binarys(self,arr,mid+1,high,s)
            elif arr[mid] > s:
                return binary.binarys(self,arr,low,mid-1,s)
            elif arr[mid] == s:
                return mid
        else:
            return -1
obj = binary()
s = 2
arr = [1,2,3,4,5]
out = obj.binarys(obj.array(),0,len(arr)-1,s)

if out != -1:
    print("Element found at index",out)
else:
    print("Element not found")