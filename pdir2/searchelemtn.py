vowels = ['a','e','i','o','u']
def search_list(list):
    s = input("Enter the search element: ")
    value = list.index(s)
    print("The index of element--",s,"is",value)
search_list(vowels)
