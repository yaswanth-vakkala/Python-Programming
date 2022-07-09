def binarys(arr,s):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < s:
            low = mid + 1
        elif arr[mid] > s:
            high = mid - 1
        elif arr[mid] == s :
            return mid
    else:
        return -1

arr = [1,2,3,4,5,6,7]
s = 20
result = binarys(arr,s)

if result != -1:
    print("Element found at index",str(result))
else:
    print("Element not found")
