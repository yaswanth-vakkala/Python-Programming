def subsetsWithDup(nums):
    result = []
    i, count = 0, 1 << len(nums)
    nums.sort()
    while i < count:
        current = []
        for j in range(len(nums)):
            if i & 1 << j:
                current.append(nums[j])
        if current not in result:
            result.append(current)
        i += 1
    return result

print(subsetsWithDup([1,2,2]))