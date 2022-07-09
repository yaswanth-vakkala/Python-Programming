def q1(n):
    binum=[]
    q=[]
    count=0
    while n!=0:
        binum.insert(0,n%2)
        n=n//2
    for k in binum:
        if k==1:
            q.append(k)
        elif k==0:
            if len(q)>count:
                count = len(q)
            q = []
    if count==0:
        count = len(q)
    return count
print(q1(156))
print(q1(125))
print(q1(511))
