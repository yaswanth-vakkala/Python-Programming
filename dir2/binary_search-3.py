class binary():
    def array(self):
        arr = []
        n = int(input("Enter the size of array: "))
        for i in range(n):
            arr.append(int(input("Enter the " + str(i) + " value of array :")))
        return arr
    def binarys(self,arr):
        low = 0
        high = len(arr) - 1
        s = int(input("Enter the search element: "))
        while low <= high:
            mid = (high + low) // 2
            print(mid)
            if arr[mid] == s:
                return mid
            elif arr[mid] < s:
                low = mid + 1
            elif arr[mid] > s:
                high = mid - 1
        else:
            return -1

obj = binary()
out = obj.binarys(obj.array())

if out != -1:
    print("Element found at index",out)
else:
    print("Element not found")

