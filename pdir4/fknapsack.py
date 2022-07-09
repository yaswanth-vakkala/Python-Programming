def fknapsack(v,w,n,mw):
    output =0
    rem = []
    cw = 0
    for i in range(n):
        div = v[i]/w[i]
        rem.append(div)
    while cw < mw and rem!= []:
        mindex = rem.index(max(rem))
        if cw+w[mindex] > mw:
            fw = v[mindex]/w[mindex]*(mw-cw)
            output+=fw
            break
        else:
            output += v[mindex]
            cw += w[mindex]
        rem.remove(rem[mindex])
        v.remove(v[mindex])
        w.remove(w[mindex])


    return output

values = [60,100,120]
weight = [10,20,30]
n = len(values)
mw = 50
print(fknapsack(values,weight,n,mw))