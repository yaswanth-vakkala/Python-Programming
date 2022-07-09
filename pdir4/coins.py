def minnc(v):
    output = 0
    index = -1
    while True:
        if currency[index] <= v and v!=0:
            output += 1
            v= v - currency[index]
        else:
            index = index -1
        if v ==0:
            break

    return output

currency = [1,2,5,10,20,50,100,500,1000]
print(minnc(121))