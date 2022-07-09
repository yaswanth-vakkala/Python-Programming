# def rdup(value):
#     f = ''.join(set(value))
#     print(f)
#
# v = "heello"
# rdup(v)
#
# def duplicate_rm(s):
#     result = "".join(dict.fromkeys(s))
#     return result
#
# print(duplicate_rm("aaaaabbbbccccdddddaa"))


def duplicate_rm(value):
    result = []
    for c in value:
        if c not in result:
            result.append(c)
    result = ''.join(result)
    print(result)

v = "hheello"
duplicate_rm(v)
