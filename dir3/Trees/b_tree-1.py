class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

class b_tree:
    def __init__(self):
        self.root = None
        self.current = None

    def insert_left(self,data):
        l_node = Node(data)
        if self.root is None:
            self.root = l_node
            self.current = l_node
        else:
            self.current.left = l_node
            self.current = l_node

    def insert_right(self,data):
        r_node = Node(data)
        if self.root is None:
            self.root = r_node
            self.current = r_node
        else:
            self.current.right = r_node
            self.current = r_node

bt = b_tree()
bt.insert_right(1)
bt.insert_left(2)
bt.insert_right(4)
bt.insert_left(3)
bt.insert_right(4)
bt.insert_left(5)
print(bt)
