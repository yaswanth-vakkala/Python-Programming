def wmachine(s):
    stk = []
    for i in s:
        if i == "POP":
            if stk == []:
                return -1
            else:
                stk.pop()
        elif i == "DUP":
            if stk == []:
                return -1
            else:
                stk.append(stk[-1])
        elif i == "+":
            if len(stk) < 2:
                return -1
            else:
                newe1 = int(stk[-1]) - int(stk[-2])
                stk.pop()
                stk.pop()
                stk.append(newe1)
        elif i == "-":
            if len(stk) < 2:
                return -1
            else:
                newe2 = int(stk[-1]) - int(stk[-2])
                stk.pop()
                stk.pop()
                stk.append(newe2)
        elif int(i) >= 0:
           stk.append(i)
        else:
            return -1
    return stk[-1]

# ops = input()
# print(wmachine(ops))

ops1 = ["1","5","DUP","3","-"]
print(wmachine(ops1))
ops2 = ["+"]
print(wmachine(ops2))
ops3 = [0,0,"+","+"]
print(wmachine(ops3))