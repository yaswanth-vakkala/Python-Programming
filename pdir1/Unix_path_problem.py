# import ast
#
# def crct_path(s):
#     stk  = []
#     for i in s:
#         if i == "..":
#             if len(stk) == 0:
#                 pass
#             else:
#                 stk.pop()
#         elif i == ".":
#             pass
#         else:
#             stk.append(i)
#
#     return stk
#
# # path1 = ["usr","..","usr",".","local","bin","docker"]
# # print(crct_path(path1))
# # path2 = input()
# # # new_path = path2.split()
# # # new_path = new_path[0]
# # # print(new_path)
# # # print(type(new_path))
# #
# # new_path = path2.strip("][").split(", ")
# # print(new_path)
# # lst = []
# # for i in new_path:
# #     lst.append(i)
# # print(lst)
# # res = new_path.strip('][').split(', ')
# #
# # # printing final result and its type
# # print("final list", res)
# # print(type(res))
# # for k in res:
# #     print(k)
# # for i in new_path[0]:
# #     print(i)
# # print(crct_path(path2))
# # path2 = ["bin","..",".."]
# # print(crct_path(path2))
#
#
# ##########################################################
#
# # initializing string representation of a list
# path = input()
# # Converting string to list
# res = ast.literal_eval(path)
#
# # printing final result and its type
# print ("final list", res)
# print (type(res))
# for i in res:
#     print(i)



import ast

def crct_path(s):
    stk  = []
    for i in s:
        if i == "..":
            if len(stk) == 0:
                pass
            else:
                stk.pop()
        elif i == ".":
            pass
        else:
            stk.append(i)

    return stk

path = input()
new_path = ast.literal_eval(path)
print(crct_path(new_path))