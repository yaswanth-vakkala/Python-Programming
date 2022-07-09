def balance(s):
    stk = []
    isTrue = False
    lp = "("
    rp = ")"
    sl = "["
    sr = "]"
    cl = "{"
    cr = "}"
    for i in s:
        if stk == [] or i == stk[-1]:
            stk.append(i)
        elif i==rp and stk[-1]==lp or i==sr and stk[-1]==sl or i==cr and stk[-1]==cl:
            stk.pop()
        else:
            stk.append(i)
    if stk == []:
        isTrue = True
    return isTrue

# s = input()
# print(balance(s))

s1 = "[(])"
print(balance(s1))
s2 = "([])[]({})"
print(balance(s2))
