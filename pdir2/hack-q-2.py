twodar = [[1,2],[34,3],[6,7]]

def largest(arr):
    a = []
    for i in arr:
        a.append(max(i))
    return a
print(largest(twodar))