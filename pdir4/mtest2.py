def minmax(arr,i,j,min,max):
	if i == j:
		min = arr[0]
		max = arr[0]
		return min,max
	elif j == i-1:
		if arr[i] < arr[j]:
			max = arr[j]
			min = arr[i]
			return  min,max
		else:
			min = arr[j]
			max = arr[i]
			return min,max
	else:
		mid = (i+j)//2
		min,max = minmax(arr, i, mid, min, max)
		min,max = minmax(arr, mid + 1, j, min, max)
		return min,max

inf = float('inf')
arr = [2,5,3,8,6,5,4,7]
min,max = inf,-inf
min, max = minmax(arr, 0, len(arr) - 1, min, max)
print("minimum: ",min,"| maximum: ",max)