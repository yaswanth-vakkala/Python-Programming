def jscheduling(jb,n):
    t = 1
    p = 0
    mp = 0
    count = 0
    while t<= n:
        for i in jb:
            if i[1] == t:
                if i[2]>p:
                    count+=1
                    p = i[2]
        t = t+1
        mp += p
        p = 0
    return (count-1,mp)

n = 4
jobs = [(1,4,20),(2,1,10),(3,1,40),(4,1,30)]
print(jscheduling(jobs,n))