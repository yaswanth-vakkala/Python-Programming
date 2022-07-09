def heapify(a,n,i):
    largest = i
    l = (2*i)+1
    r = (2*i)+2
    if l<n and a[l] < a[largest]:
        largest = l
    if r<n and a[r] < a[largest]:
        largest = r
    if largest!= i:
        a[i],a[largest] = a[largest],a[i]
        heapify(a,n,largest)

def heap(a,n):
    for i in range((n//2-1),-1,-1):
        heapify(a,n,i)

a = [15,20,7,9,30]
n = len(a)
heap(a,n)
print(a)
