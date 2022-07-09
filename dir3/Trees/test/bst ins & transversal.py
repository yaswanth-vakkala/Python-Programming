class Node:
    
    def __init__(self, data):
        self.data = data
        self.RA = None
        self.LA = None

def post_order(root):
    if root != None:
        post_order(root.LA) #left
        post_order(root.RA) #right
        print(root.data) # raise the flag

def pre_order(root):
    
    if root!=None:
        print(root.data)  #raise the flage
        pre_order(root.LA) #left
        pre_order(root.RA) #right

def in_order(root):
    
    if root!=None:
        
        in_order(root.LA) #left
        print(root.data)  #raise the flage
        in_order(root.RA) #right
        
def insert(root, data):
    
    
    if data < root.data:
        # place left
        if root.LA == None:
            newnode = Node(data)
            root.LA = newnode
        else:
        # go left
            insert(root.LA, data)
        
    if data > root.data:
        # place right
        if root.RA == None:
            newnode = Node(data)
            root.RA = newnode
        else:
        # go right
            insert(root.RA, data)

def main():
    root = Node(50)
    insert(root, 25)
    insert(root, 75)
    insert(root, 15)
    insert(root, 12)
    insert(root, 65)
    insert(root, 55)
    #post_order(root)
    pre_order(root)


if __name__ == "__main__":
    main()