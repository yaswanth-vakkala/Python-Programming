slist = [1,2,3,4,5]
def zsumaveg(list):
    sum = 0
    for i in list:
        sum = sum + i
    average = sum / len(list)
    print("sum is",sum)
    print("average is",average)

zsumaveg(slist)