vowels = ['a', 'e', 'i', 'o', 'u']

c = input("Enter the character : ")
if c.lower() in vowels:
    print(c, "is a vowel")
else:
    print(c, "is not a vowel")