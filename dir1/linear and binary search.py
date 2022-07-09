def array():
    arr = []
    n = int(input("Enter the size of array: "))
    for i in range(n):
        arr.append(int(input("Enter the "+ str(i) +" value of array :")))
    return arr

def linear(arr):
    s = int(input("Enter the search element: "))
    flag = 1
    for i in range(len(arr)):
        if arr[i] == s :
            flag = 0
    if flag == 0:
        print("element found")
    else:
        print("element not found")

def binary(arr):
    s = int(input("Enter the search element: "))
    flag = 1
    low = 0
    high = len(arr) - 1
    while high > low :
        mid = round((low + high) / 2)
        if arr[mid] == s:
            flag = 0
            break
        elif arr[mid] > s:
            high = mid-1
        elif arr[mid] < s:
            low = mid+1
    if flag == 0:
        print("element found")
    else:
        print("element not found")
binary(array())