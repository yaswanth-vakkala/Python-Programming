class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def preorder(root):
    if root is None:
        return []
    stk = []
    stk.append(root)
    while stk != []:
        current = stk.pop()
        print(current.data, end=" ")
        if current.right is not None:
            stk.append(current.right)
        if current.left is not None:
            stk.append(current.left)
    print("")

def inorder(root):
    stk = []
    while root is not None or stk != []:
        while root is not None:
            stk.append(root)
            root = root.left
        root = stk.pop()
        print(root.data,end=" ")
        root = root.right

root = Node(4)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(1)

print("Preorder")
preorder(root)
print("Inorder")
inorder(root)
