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

    def min_node(self):
        root = self.root
        while root.left is not None:
            root = root.left
        return root.data

    def max_node(self):
        root = self.root
        while root.right is not None:
            root = root.right
        return root.data

def display(list):
    obj = bst()
    for i in list:
        obj.insertion(i)
    min = obj.min_node()
    max = obj.max_node()
    return [min,max]

list = [5,12,2,3,1,21,9,25,19]
display(list)
