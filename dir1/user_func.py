def factorial(n):
    sum = n
    for i in range(n):
        if n != 1:
            n = n-1
            sum = sum * n
    return sum

print(factorial(5))

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