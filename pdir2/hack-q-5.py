a = [1,2,3,4]
b = [1,2,4,5]

def match(a,b):
    if a == b:
        return -1
    else:
        for i in range(len(a)):
            if a[i] != b[i]:
                return i


print(match(a,b))