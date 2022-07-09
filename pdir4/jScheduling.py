def jScheduling(arr,n):
    s_arr = sorted(arr, reverse=True)
    print(s_arr)
    jobs = [0]*n
    for i in s_arr:
        if jobs[i[1]-1] == 0:
            jobs[i[1]-1] = i[0]
        else:
            # for j in reversed(jobs[:i[1]-1]):
            #     if j == 0:
            #         jobs[j] = i[0]
            for j in range(i[1]-2,-1,-1):
                if jobs[j] == 0:
                    jobs[j] = i[0]
                    break
    return jobs

arr = [(60,2),(100,1),(20,3),(40,2),(20,1)]
# arr = [(200,5),(180,3),(190,3),(300,2),(120,4),(100,2)]
# arr = [(35,3),(30,4),(25,4),(20,2),(15,3),(12,1),(5,2)]
# arr = [(3,1),(5,3),(20,4),(18,3),(1,2),(6,1),(30,2)]
# arr = [(15,9),(2,2),(18,5),(1,7),(25,4),(20,2),(8,5),(10,7),(12,4),(5,3)]

jbs = jScheduling(arr,len(arr))
profit = 0
for i in jbs:
    profit += i
print(jbs)
print(profit)