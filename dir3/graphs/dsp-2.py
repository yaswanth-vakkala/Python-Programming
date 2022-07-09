# def svalid(value):
#     paran1 = "("
#     paran2 = ")"
#     flower1 = "{"
#     flower2 = "}"
#     sqr1 = "["
#     sqr2 = "]"
#     if value[0] == "(" and value[-1] == ")":
#         print("valid")
#     else:
#         print("invalid")
#
# v = "([]{})"
# svalid(v)

def svalid(value):
    parans = ["(",")"]
    sqrs = ["[","]"]
    flws = ["{","}"]
    stk1 = []
    stk2 = []
    flag = False
    if value[0] == parans[0]  and value[-1] == parans[1] :
        for i in range(1,len(value)-1):
            if i % 2 == 0:
                stk1.append(value[i])
            else:
                stk2.append(value[i])
        for i in range(len(stk1)):
            if stk2[i] == sqrs[0] and stk1[i] == sqrs[1] or stk2[i] == flws[0] and stk1[i] == flws[1]:
                flag = True
            else:
                flag = False
    if flag is True:
        print("valid")
    else:
        print("not valid")

v = "([]{})"
svalid(v)
v2 = "([)]"
svalid(v2)
