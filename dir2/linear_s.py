def array():
    arr = []
    n = int(input("Enter the size of array: "))
    for i in range(n):
        arr.append(int(input("Enter the "+ str(i) +" value of array :")))
    return arr

def linear(arr):
    s = int(input("Enter the search element: "))
    for i in range(len(arr)):
        if arr[i] == s :
            print("element found at",i,"index value")
            quit()
    else:
        print("element not found")

# linear(array())
# linear([1,2,3,4,5])

def linear(arr):
    s = int(input("Enter the search element: "))
    for i in range(len(arr)):
        if arr[i] == s :
            return i
            quit()
    else:
        return -1
arr = [1,2,3,4,5]
result = linear(arr)

if result == -1:
    print("element not found")
else:
    print("element found at index",result)
