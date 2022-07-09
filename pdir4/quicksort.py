# def partition(arr,low,high):
#     i,j = low,high-1
#     pivot = arr[high]
#     while i<j:
#         while i<high and arr[i] < pivot:
#             i+=1
#         while j>low and arr[j] >= pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j] = arr[j],arr[i]
#     if arr[i] > pivot:
#         arr[i],arr[high] = arr[high] , arr[i]
#     return i
#
# def quicksort(arr,low,high):
#     if low<high:
#         p = partition(arr,low,high)
#         quicksort(arr,low,p-1)
#         quicksort(arr,p+1,high)
#
#
# arr = [2,5,3,8,6,5,4,7]
# quicksort(arr,0,len(arr)-1)
# print(arr)

def quickSort(arr):
    elements = len(arr)
    if elements < 2:
        return arr
    cp = 0
    pivot = arr[0]
    for i in range(1, elements):
         if arr[i] <= pivot:
              cp += 1
              arr[cp],arr[i] = arr[i],arr[cp]
    arr[0],arr[cp] = arr[cp],arr[0]
    left = quickSort(arr[0:cp])
    right = quickSort(arr[cp+1:elements])
    arr = left + [arr[cp]] + right
    return arr

arr = [2,5,3,8,6,5,4,7]
print(quickSort(arr))