arr = [1,2,3,4,-1,-4,-5,-2]

def arrange(arr):
    a,b = [],[]
    for i in arr:
        if i > 0:
            a.append(i)
        else:
            b.append(i)
    x = b + a
    return x
print(arrange(arr))