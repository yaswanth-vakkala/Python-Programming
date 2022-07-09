#create and display the linked list
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None #initially , no connection between nodes, 1 node created  

class CLL:
  def __init__(self):
    self.head=None #initially my LL is empty
  
  #first operation: Traversal
  def display(self):
      temp=self.head
      if self.head is None:
          print("LL is empty")
      else:
          while temp is not None:
            print(temp.data,"-->",end=" ")
            temp=temp.next
            if temp==self.head:
                break

      #print(self.head.data)
  #insert a node at the beginning
  def insert_begin(self,data):
    new_node=Node(data)
    if self.head is None:
        new_node.next=new_node
        self.head=new_node
       
    else:
        temp=self.head
        #traverse through the nodes to reach the last node
        while temp.next is not self.head:
            temp=temp.next
        #after reaching the last node, update the addresses
        temp.next=new_node
        new_node.next=self.head
        #point head to new_node
        self.head=new_node
       
    
  def insert_end(self,data):
    new_node=Node(data)
    if self.head is None:
        new_node.next=new_node
        self.head=new_node
       
    else:
        temp=self.head
        while temp.next is not  self.head:
            temp=temp.next
        temp.next=new_node
        new_node.next=self.head
    
  def insert_position(self,pos,data):   #here assuming that pos of node1 starts at 0
        new_node=Node(data)
        #before pointing to node1
        before=self.head
        #temp is pointing to node2
        temp=self.head.next
        #traverse through LL to reach node that is pointed by pos
        for i in range(pos-1):
            before=before.next
            temp=temp.next
        new_node.next=temp
        before.next=new_node
  def delete_begin(self):
      if self.head is None:
          print("LL is not empty")
      elif self.head.next==self.head:
          self.head=None
          self.head.next=None
      else:
          temp=self.head
          while temp.next!=self.head:
              temp=temp.next
          temp.next=self.head.next
          self.head=self.head.next  #2nd node
        
  def delete_end(self):
      if self.head is None:
          print("LL is empty")
      elif self.head.next==self.head:
          self.head=None

      else:
          temp=self.head.next
          before=self.head
          while temp.next!=self.head:
              temp=temp.next  #last node
              before=before.next #last but 1 node
          
          before.next=self.head
  def delete_position(self,pos):
         
         
              temp=self.head.next
              before=self.head
              for i in range(pos-1):
                      temp=temp.next
                      before=before.next
              before.next=temp.next
              
        
        
       
LL=CLL()
LL.insert_begin(10)
LL.insert_begin(20)
LL.insert_begin(30)
LL.insert_end(100)
LL.insert_end(5)
LL.display()
LL.insert_position(2,120)
LL.insert_position(3,150)
print("")
# LL.delete_begin()
# LL.delete_end()
# LL.insert_end(200)
# LL.insert_end(205)
# LL.delete_position(3)
LL.display()