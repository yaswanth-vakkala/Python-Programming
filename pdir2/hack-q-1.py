sample = [1,1,1,2,3,4,4,5,4,3]

def norepeat(arr):
    a = []
    for i in arr:
        if arr.count(i) == 1:
            a.append(i)
    return a
print(norepeat(sample))