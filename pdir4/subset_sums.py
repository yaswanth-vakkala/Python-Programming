def subsetSums(arr, n):
	if len(arr) == 1:
		return [0, arr[0]]
	sums = subsetSums(arr[1:], n)
	n = len(sums)
	for i in range(n):
	    sums.append(sums[i]+arr[0])
	return sums

print(subsetSums([5,2,1],3))

