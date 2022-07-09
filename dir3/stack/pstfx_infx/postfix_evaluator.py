def psfx_eval(expression):
    stk = []
    exp = expression.split()
    print(exp)
    for i in exp:
        if i.isdigit():
            stk.append(int(i))
        elif i == "+":
            first = stk.pop()
            second = stk.pop()
            stk.append(second + first)
        elif i == "-":
            first = stk.pop()
            second = stk.pop()
            stk.append(second - first)
        elif i == "*":
            first = stk.pop()
            second = stk.pop()
            stk.append(second * first)
        elif i == "/":
            first = stk.pop()
            second = stk.pop()
            stk.append(second / first)
        elif i == "^":
            first = stk.pop()
            second = stk.pop()
            stk.append(second ^ first)
    return stk.pop()
print(psfx_eval("10 2 8 * + 3 -"))
print(psfx_eval("3 5 + 1 *"))
print(psfx_eval("3 5 * 1 / 4 *"))
