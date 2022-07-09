class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
a.left = b
a.right = d
b.left = c
d.left = e
d.right = f
