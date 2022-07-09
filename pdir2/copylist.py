list1 = [4,2,5,213,54,1,5,342]
def zcplist(list):
    global cplist
    cplist = list.copy()
    print("Your new copy of list is:",cplist,"and you can access is using variable name // cplist //")
zcplist(list1)

