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
        if self.root is None:
            print("empty tree")
        else:
            self._search(data,self.root)

    def _search(self,data,current):
        if data == current.data:
            print("element found")
        elif data > current.data and current.right:
            self._search(data,current.right)
        elif data < current.data and current.left:
            self._search(data,current.left)
        else:
            print("element not found")

    def min_node(self):
        root = self.root
        while root.left is not None:
            root = root.left
        print("min element in tree is",root.data)

    def max_node(self):
        root = self.root
        while root.right is not None:
            root = root.right
        print("max element in tree is",root.data)

    def getmin(self,root):
        current = root.right
        if current.left == None:
            return current
        else:
            while current.left is not None:
                current = current.left

    def getmax(self,root):
        current = root.left
        if current.right is None:
            return current
        else:
            while current.right is not None:
                current = current.right

    def deletion(self,target):
        if self.root is None:
            print("empty tree")
        else:
            temp = self.root
            while temp is not None:
                if temp.data == target:
                    break
                elif temp.data < target:
                    current = temp
                    temp = temp.right
                else:
                    current = temp
                    temp = temp.left
            if temp.left == None and temp.right == None:
                if current.data < temp.data:
                    current.right = None
                else:
                    current.left = None
                del temp
            elif temp.left == None and temp.right != None:
                if current.data < temp.data:
                    current.right = temp.right
                else:
                    current.left = temp.right
                del temp
            elif temp.left != None and temp.right == None:
                if current.data > temp.data:
                    current.left = temp.left
                else:
                    current.right = temp.left
                del temp

            elif temp.left!= None and temp.right != None:
                current = temp.right
                if current.left == None and current.right == None:
                    temp.data = current.data
                    temp.right = None
                    del current
                elif current.left == None and current.right!= None:
                    temp.data = current.data
                    temp.right = current.right
                    del current
                else:
                    while current.left.left!= None:
                        current = current.left
                    temp.data = current.left.data
                    current.left = None
    def Preorder(self,rnode):
        if rnode is None:
            return
        print(rnode.data)
        self.Preorder(rnode.left)
        self.Preorder(rnode.right)

    def Inorder(self,rnode):
        if rnode:
            self.Inorder(rnode.left)
            print(rnode.data,end="")
            self.Inorder(rnode.right)

    def Postorder(self,rnode):
        if rnode is None:
            return
        self.Postorder(rnode.left)
        self.Postorder(rnode.right)
        print(rnode.data)


obj = bst()
obj.insertion(8)
obj.insertion(3)
obj.insertion(10)
obj.insertion(1)
obj.insertion(6)
obj.insertion(14)
obj.insertion(13)
obj.insertion(4)
obj.insertion(7)


print("Preorder")
obj.Preorder(obj.root)
print("Inorder")
obj.Inorder(obj.root)
print("postorder")
obj.Postorder(obj.root)
# obj.search(98)
# obj.search(6)
# obj.search(91)
# obj.min_node()
# obj.max_node()
obj.deletion(7)
obj.deletion(3)
obj.deletion(14)
print("")
print("Inorder")
obj.Inorder(obj.root)
