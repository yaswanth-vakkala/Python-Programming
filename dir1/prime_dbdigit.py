def isprime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False

def rotation_check():
    n = input("Enter a number: ")
    list = []
    for i in range(len(n)):
      m = int(str(n)[i:] + str(n)[:i])
      list.append(m)
    checker = 0
    for i in list:
        if isprime(i):
            checker += 1
    if checker == len(list):
        return True
    else:
        return False
print(rotation_check())