class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class single_linked_lst():
    def __init__(self):
        self.head = None

nod1 = Node(10)
print("head:",id(nod1))
print(nod1.data,nod1.next)
obj1 = single_linked_lst()
obj1.head = id(nod1)
print("head:",obj1.head)

nod2 = Node(12)
nod1.next = id(nod2)
print("next1:",id(nod2))

nod3 = Node(20)
nod2.next = id(nod3)
print("next2:",id(nod3))

print("next1:",nod1.next,"next2:",nod2.next,"next3:",nod3.next)
