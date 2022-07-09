def sea_view_calc(input):
    stk = []
    indx = []
    counter = 0
    for i in input:
        if stk == [] or stk[-1]>i:
            stk.append(i)
            indx.append(counter)
        elif stk[-1]==i:
            stk.pop()
            indx.pop()
            stk.append(i)
            indx.append(counter)
        elif stk[-1] < i:
            while stk[-1] < i:
                stk.pop()
                indx.pop()
                if stk == []:
                    break
            stk.append(i)
            indx.append(counter)
        counter += 1
    # print(stk)
    return indx

print(sea_view_calc([1,5,5,2,3]))
print(sea_view_calc([10,50,50,20,30]))
print(sea_view_calc([50,40,60,50,30,45,48]))
# print("__________________")
print(sea_view_calc([40,20,10,30,200,25]))

# def sea_view_calc(input):
#     stk = []
#     indx = []
#     counter = 0
#     for i in input:
#         if stk == [] or stk[-1]>i:
#             stk.append(i)
#             indx.append(counter)
#         elif stk[-1] < i:
#             while stk[-1] < i:
#                 stk.pop()
#                 indx.pop()
#                 if stk == []:
#                     break
#             stk.append(i)
#             indx.append(counter)
#         counter += 1
#     return indx
#
# i = int(input())
# inp_list = []
# for i in range(0,i):
#     inp_list.append(int(input()))
#
# print(sea_view_calc(inp_list))
