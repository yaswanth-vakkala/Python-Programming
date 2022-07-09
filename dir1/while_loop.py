n = int(input("Enter the natural number : "))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i+1    # update counter

print("The sum is", sum)

i = 0
a = input("Enter a desired word: ")

while i < len(a):
    if a[i] == ' ':
        i += 1
        pass
    print('Current Letter :', a[i])
    i += 1

vowels = ['a', 'e', 'i', 'o', 'u']
i = 0
c = input("Enter the word: ")
count = 0
while i < len(c):
    if c[i] in vowels:
        count = count + 1
    i = i + 1
print(count)