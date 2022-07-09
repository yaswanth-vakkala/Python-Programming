def sortArray(nums):
    if len(nums) == 1:
        return nums
    half = len(nums) // 2
    left = nums[:half]
    right = nums[half:]
    left = sortArray(left)
    right = sortArray(right)
    return sort(left, right)

def sort(a, b):
    out = []
    while a and b:
        if a[0] <= b[0]:
            out.append(a.pop(0))
        else:
            out.append(b.pop(0))
    if a:
        out += a
    else:
        out += b
    return out

nlist = [3,1,4,1,5,9,2,6,5,4,123]
print(sortArray(nlist))