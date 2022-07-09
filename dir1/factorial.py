def factorial(n):
    sum = n
    for i in range(n):
        if n != 1:
            n = n-1
            sum = sum * n
    return sum

print(factorial(5))