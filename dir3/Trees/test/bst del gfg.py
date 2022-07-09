'''class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 
def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right) 
def insert(root, key):
    if root == None:
        temp = Node(key)
        return temp 
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def deleteIterative(root, key):
    curr = root
    prev = None
    while(curr != None and curr.data != key):
        prev = curr
        if curr.data < key:
            curr = curr.right
        else:
            curr = curr.left
    if curr == None:
        print("Key % d not found in\
           the provided BST." % key)
        return root
    if curr.left == None or\
            curr.right == None:
        newCurr = None
        if curr.left == None:
            newCurr = curr.right
        else:
            newCurr = curr.left
        if prev == None:
            return newCurr
        if curr == prev.left:
            prev.left = newCurr
        else:
            prev.right = newCurr
        curr = None
    else:
        p = None
        temp = None
        temp = curr.right
        while(temp.left != None):
            p = temp
            temp = temp.left
        if p != None:
            p.left = temp.right
        else:
            curr.right = temp.right
        curr.data = temp.data
        temp = None
    return root 
def main():
    root = None
    root = insert(root, 10)
    root = insert(root, 7)
    root = insert(root, 5)
    root = insert(root, 8)
    root = insert(root, 15)
    root = insert(root, 11)
    root = insert(root, 18)
    print("Inorder traversal of original BST:")
    inorder(root)
    print("\n")
    root = deleteIterative(root, 11)
    print("Deletion of 11")
    print("Inorder traversal post deletion:")
    inorder(root)
    print("\n")
    root = deleteIterative(root, 15)
    print("Deletion of 15")
    print("Inorder traversal post deletion:")
    inorder(root)
    print("\n")
    root = deleteIterative(root, 10)
    print("Deletion of 10")
    print("Inorder traversal post deletion:")
    inorder(root)
    print()

if __name__ == "__main__":
    main()'''
class bst:
  def __init__(self,value):
      self.value= value
      self.left= None
      self.right= None
      
  def insert(self,data):
      if self.value is None:
          self.value= data
          return
      if self.value == data:
          return
      if data < self.value:
          if self.left:
              self.left.insert(data)
          else:
              self.left= bst(data)
      else:
          if self.right:
              self.right = bst(data)
              
  def search(self,value):
      if self.value== data:
          print("Node is present in tree")
          return
      if data < self.value:
          if self.left:
              self.left.search(data)
          else:
              print("Node is not present in tree")
      else:
          if self.right:
              self.right.search(data)
          else:
              print("Node is not present in tree")
               
  def delete(self,data):
      if self.value is None:
          print("tree is empty")
          return
      if data < self.value:
          if self.left:
              self.left=self.left.delete(data)
          else:
              print("given node is not present in the tree")
      elif data > self.value:
           if self.right:
               self.right=self.right.delete(data)
           else:
               print("given node is not present in the tree")
      else:
           if self.left is None:
               temp = self.right
               self=None
               return temp
           if self.right is None:
               temp=self.left
               self=None
               return temp
               node = self.right
               while node.left:
                   node = node.left
                   self.value=node.value
                   self.right=self.right.delete(node.value)
               return self
def inorder(value):
    if value:
         inorder(value.left)
         print(value.value)
         inorder(value.right)

self = bst(10)
list1 = [7,4,2,7,89,4,7]
for i in list1:
    self.insert(i)
print("inorder")
inorder(self)
print()
self.delete(7)
print("after deleting")
inorder(self)