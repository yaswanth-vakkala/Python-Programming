def smatrix(arr,target):
    for i in arr:
        for j in i:
            if(j==target):
                print("element found")
                quit()
    else:
        print("element not found")

arr = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
smatrix(arr,34)
