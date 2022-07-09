class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class bst:
    def __init__(self):
        self.root = None

    def insertion(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insertion(data,self.root)

    def _insertion(self,data,current):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self._insertion(data,current.left)
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insertion(data,current.right)

    def search(self,data):
        if self.root:
            is_found = self._search(data,self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None

    def _search(self,data,current):
        if data == current.data:
            print("Element found")
        elif data > current.data:
            self._search(data,current.right)
        elif data < current.data:
            self._search(data,current.left)

    def Preorder(self,rnode):
        if rnode is None:
            return
        print(rnode.data)
        self.Preorder(rnode.left)
        self.Preorder(rnode.right)

    def Inorder(self,rnode):
        if rnode:
            self.Inorder(rnode.left)
            print(rnode.data)
            self.Inorder(rnode.right)


obj = bst()
obj.insertion(10)
obj.insertion(6)
obj.insertion(3)
obj.insertion(1)
obj.insertion(98)
obj.insertion(3)
obj.insertion(7)
print("Preorder")
obj.Preorder(obj.root)
print("Inorder")
obj.Inorder(obj.root)
obj.search(98)
