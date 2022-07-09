def array():
    arr = []
    n = int(input("Enter the size of array: "))
    for i in range(n):
        arr.append(int(input("Enter the "+ str(i) +" value of array :")))
    return arr

def binarys(arr):
    low = 0
    high = len(arr) - 1
    s = int(input("Enter the search element: "))

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < s:
            low = mid + 1
        elif arr[mid] > s:
            high = mid - 1
        elif arr[mid] ==s :
            return mid
    else:
        return -1

result = binarys(array())

if result != -1:
    print("Element found at index",str(result))
else:
    print("Element not found")
