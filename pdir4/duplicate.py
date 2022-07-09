def find_duplicate(arr):
    range = len(arr)-1
    ref_arr = [0] *  range
    for i in arr:
        ref_arr[i-1] += 1
        if ref_arr[i-1] == 2:
            dup = i
            break
    return dup

arr = [1,2,5,2,6,3,4]
print(find_duplicate(arr))
