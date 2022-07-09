def duplicate_rm(s):
    result = "".join(dict.fromkeys(s))
    return result

print(duplicate_rm("aaaaabbbbccccdddddaa"))
print(duplicate_rm("a"))