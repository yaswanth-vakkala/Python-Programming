def subseq(s):
    stk = []
    counter = 0
    lp = "("
    rp = ")"
    for i in s:
        if stk == [] or i == stk[-1]:
            stk.append(i)
        elif i==rp and stk[-1]==lp:
            stk.pop()
            counter+= 2
        else:
            stk.append(i)
    return counter

# s = input()
# print(subseq(s))

s1 = "())(()"
print(subseq(s1))
s2 = "))(("
print(subseq(s2))
s3 = "))()))()"
print(subseq(s3))
s4= "((((())"
print(subseq(s4))