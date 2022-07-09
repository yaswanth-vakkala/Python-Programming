def minimumPlatform(n, arr, dep):
    arr.sort()
    dep.sort()
    platform = 1
    i = 1
    j = 0
    while i < n:
        if arr[i] > dep[j]:
            i += 1
            j += 1
        else:
            platform += 1
            i += 1
    return platform

n = 6
arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]
print(minimumPlatform(n,arr,dep))
