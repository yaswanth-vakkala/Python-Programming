strings = "hello world its me guys"

def longest(st):
    a = []
    s = st.split()
    for i in s:
        a.append(len(i))
        x = a.index(max(a))
    return s[x]
print(longest(strings))