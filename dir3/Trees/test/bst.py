class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def insert(self, value):
        Node = self
        while True:
            if value < Node.value:
                if Node.left is None:
                    Node.left = BinarySearchTree(value)
                    break
                else:
                    Node = Node.left
            else:
                if Node.right is None:
                    Node.right = BinarySearchTree(value)
                    break
                else:
                    Node = Node.right
        return self
    def contains(self, value):
        Node = self
        while Node is not None:
            if value < Node.value:
                Node = Node.left
            elif value > Node.value:
                Node = Node.right
            else:
                return True
        return False
    def remove(self, value, OriginNode = None):
        Node = self
        while Node is not None:
            if value < Node.value:
                OriginNode = Node
                Node = Node.left  
            elif value > Node.value:
                OriginNode = Node
                Node = Node.right
            else:   
                if Node.left is not None and Node.right is not None:
                    Node.value = Node.right.Min()
                    Node.right.remove(Node.value, Node) 
                elif OriginNode is None:
                    if Node.left is not None:
                        Node.value = Node.left.value
                        Node.right = Node.left.right
                        Node.left = Node.left.left
                    elif Node.right is not None:
                        Node.value = Node.right.value
                        Node.left = Node.right.left
                        Node.right = Node.right.right
                    else:
                        pass
                elif OriginNode.left == Node:
                    OriginNode.left = Node.left if Node.left is not None else Node.right
                elif OriginNode.right == Node:
                    OriginNode.right = Node.left if Node.left is not None else Node.right
                break
        return self
    def Min(self):
        Node = self
        while Node.left is not None:
            Node =Node.left
        return Node.value
    
def inorder(value):
    if value:
         inorder(value.left)
         print(value.value)
         inorder(value.right)
         
r = BinarySearchTree(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)
r.insert(60)
r.insert(80)
print("Before removal")
inorder(r)
r.remove(70)
r.remove(40)
print("After removal")
inorder(r)

