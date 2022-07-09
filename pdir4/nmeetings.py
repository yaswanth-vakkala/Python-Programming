def nmeetings(s,e,n):
    meeting = [[s[i], e[i]] for i in range(len(s))]
    meeting = sorted(meeting, key=lambda x: x[1])
    res = []
    res.append(meeting[0])
    for i in range(1, len(meeting)):
        if res[-1][1] < meeting[i][0]:
            res.append(meeting[i])
    return len(res)

start = [1,3,0,5,8,5]
end = [2,4,6,7,9,9]
n = len(start)
print(nmeetings(start,end,n))