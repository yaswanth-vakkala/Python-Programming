class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

class mheapt:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,root):
        if root.left is None:
            root.left = Node(data)
        elif root.right is None:
            root.right = Node(data)

        # elif root.left and root.right is not None:
        #     current_l = root.left
        #     current_r = root.right
        #     if current_l.right == None or current_l.left == None:
        #         self._insert(data,current_l)
        #     elif current_r.right == None or current_r.left == None:
        #         self._insert(data, current_r)
        #     elif current_l.right != None and current_l.left != None:
        #         self._insert(data,current_l)
        #     elif current_r.right != None and current_r.left != None:
        #         self._insert(data,current_r)

            # self._insert(data,current_l)
            # self._insert(data,current_r)
ht = mheapt()
ht.insert(25)
ht.insert(23)
ht.insert(32)
ht.insert(27)
ht.insert(11)
ht.insert(46)
ht.insert(90)
ht.insert(89)
ht.insert(67)
ht.insert(33)
ht.insert(31)
ht.insert(75)