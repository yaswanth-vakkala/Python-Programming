class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data)
        Inorder(root.right)

def Preorder(root):
    if root is None:
        return
    print(root.data)
    Preorder(root.left)
    Preorder(root.right)

def Postorder(root):
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.data)

root = Node(4)
root.left = Node(5)
root.right = Node(10)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(1)
print("Inorder")
Inorder(root)
print("Preorder")
Preorder(root)
print("Postorder")
Postorder(root)