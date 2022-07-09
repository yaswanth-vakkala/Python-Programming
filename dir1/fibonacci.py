def fib(n):
    n1 = 0
    n2 = 1
    i = 2
    print(n1)
    print(n2)
    while i!=n:
        v = n1 + n2
        print(v)
        n1 = n2
        n2 = v
        i = i +1
def fib2(n):
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for l in range(n-2):
        v = n1 + n2
        print(v)
        n1 = n2
        n2 = v
