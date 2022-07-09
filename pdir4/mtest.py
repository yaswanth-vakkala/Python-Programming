def minmax(arr,low,high,min,max):
	if low == high:
		if min > arr[high]:
			min = arr[high]
		if max < arr[low]:
			max = arr[low]
		return min,max
	elif high == low-1:
		if arr[low] < arr[high]:
			if min > arr[low]:
				min = arr[low]
			if max < arr[high]:
				max = arr[low]
		else:
			if min > arr[high]:
				min = arr[high]

			if max < arr[low]:
				max = arr[low]

		return min, max
	else:
		mid = (low+high)//2
		min,max = minmax(arr, low, mid, min, max)
		min,max = minmax(arr, mid + 1, high, min, max)
		return min,max

inf = float('inf')
arr = [2,5,3,8,6,5,1,4,7,9,120]
min,max = max(arr)+1,min(arr)-1
min, max = minmax(arr, 0, len(arr) - 1, min, max)
print("minimum: ",min,"| maximum: ",max)