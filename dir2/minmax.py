def getMinMax(low, high, arr):
    # If there is only one element
    if low == high:
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_max, arr_min)
    # If there is only two element
    elif high == low + 1:
        if arr[low] > arr[high]:
            arr_max = arr[low]
            arr_min = arr[high]
        else:
            arr_max = arr[high]
            arr_min = arr[low]
        return (arr_max, arr_min)
    else:
        # If there are more than 2 elements
        mid = (low + high) // 2
        arr_max1, arr_min1 = getMinMax(low, mid, arr)
        arr_max2, arr_min2 = getMinMax(mid + 1, high, arr)
    if arr_max2 > arr_max1:
        print("maximum:",arr_max2)
    else:
        print("maximum:",arr_max1)
    if arr_min1 < arr_min2:
        print("minimum",arr_min1)
    else:
        print("minimum",arr_min2)
    return (max(arr_max1, arr_max2), min(arr_min1, arr_min2))

arr = [2,5,3,8,6,5,1,4,7]
print(getMinMax(0,len(arr)-1,arr))