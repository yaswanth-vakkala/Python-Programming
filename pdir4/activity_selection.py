def activity_s(s, f):
    output = []
    l = len(s)
    k = 0
    output.append(k)
    for i in range(l):
        if s[i] >= f[k]:
            output.append(i)
            k = i
    return output


start = [1, 3, 0, 5, 8, 5]
end =  [2, 4, 6, 7, 9, 9]
print(activity_s(start,end))
