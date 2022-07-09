# def balancer(s):
#     stk = []
#     counter = 0
#     lp = "("
#     rp = ")"
#     p = "()"
#     for i in s:
#         if stk == [] or i == stk[-1]:
#             stk.append(i)
#             counter += 1
#         elif i==rp and stk[-1]==lp:
#             stk.pop()
#             counter-= 1
#         else:
#             stk.append(i)
#             counter += 1
#     return counter
#
# print(balancer(")))(("))
# print(balancer("(()("))
# print(balancer("()"))
# print(balancer("(())"))

def balancer(s):
    stk = []
    counter = 0
    lp = "("
    rp = ")"
    p = "()"
    q='"'
    for i in s:
        if i==q:
            pass
        elif stk == [] or i == stk[-1]:
            stk.append(i)
            counter += 1
        elif i==rp and stk[-1]==lp:
            stk.pop()
            counter-= 1
        else:
            stk.append(i)
            counter += 1
    return counter

inp = input()
print(balancer(inp))