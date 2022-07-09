#create and display the linked list
class Node:
  def __init__(self,data):
    self.data=data
    self.next=None #initially , no connection between                    #nodes, 1 node created  

class SingleLinkedList:
  def __init__(self):
    self.head=None #initially my LL is empty
  
  #first operation: Traversal
  def display(self):
    if self.head is None:
      print("LL is an Empty List")
    else:
      temp=self.head
      while temp is not None:
        print(temp.data,"-->",end=" ")
        temp=temp.next

      #print(self.head.data)
  #insert a node at the beginning
  def insert_begin(self,data):
    nb=Node(data)
    nb.next=self.head
    self.head=nb
  
  def insert_end(self,data):
    ne=Node(data)
    #no nodes in LL
    if self.head is None:
      self.head=ne
    else:
      #LL is not empty, and i need to traverse the #LL to go to last node
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=ne

   #insert after a node(data part,x is specified)
  def insert_after(self,data,x):  #data=5, x=20
    #traverse through the LL to find if x is present in LL
    temp=self.head
    while temp is not None:
      if x==temp.data:
        break
     
      else:
        temp=temp.next
    if temp is None:
      print("x(20) is not in the LL")
    else:
      new_node=Node(data)
      new_node.next=temp.next
      temp.next=new_node
    
  #method to insert a node before a node data 
  #insert at a particular position
  def insert_position(self,pos,data):
        temp=self.head
        #since we know the number of iterartions, we go with for loop
        for i in range(pos-1):
            #update temp to go to next node
            temp=temp.next
        #create a new node
        new_node=Node(data)
        #update the next of new_node to point to next node
        new_node.next=temp.next
        #update next of temp(current node) to point to new_node
        temp.next=new_node
    
  def search(self,x):
      temp=self.head   #node1--temp
      while temp is not None:
          if x==temp.data: #node1 data
             return True
             break
          temp=temp.next  #visit the next node
      else:
         return False
        
  def delete_begin(self):
       temp=self.head
       if temp is None:
           print("LL is empty")
       else:
           self.head=temp.next
           temp.next=None
  def delete_last(self):
       temp=self.head.next  #n2
       previous=self.head #n1
       if previous.next is None:
           print("LL is empty")
       elif temp.next is None:
           previous.next=None
       else:
           while temp.next is not None:
               temp=temp.next  #n3
               previous=previous.next  #n2
           previous.next=None
    
  def delete_position(self,pos):
      temp=self.head.next
      previous=self.head
      for i in range(pos-1):
          temp=temp.next
          previuos=previous.next
      previous.next=temp.next
      temp.next=None
      
            
        
                   
 #create the first node , object of Node class
n1=Node(10)
#print(id(n1))
#print(n1.data, n1.next)'''
LL=SingleLinkedList()
LL.head=n1
#print(id(LL.head))
n2=Node(20)
#link between node1 and node2
n1.next=n2
n3=Node(30)
n2.next=n3
print("before insert begin")
LL.display()
LL.insert_begin(50)
LL.insert_begin(25)
print("after insert a node in the beginning")
LL.display()
LL.insert_end(200)
LL.insert_end(600)
print("insert node at the end of LL")

LL.insert_after(5000,200)
LL.insert_position(2,'B16section')
LL.display()
result=LL.search(500)  #5--data value at some node
if result:
    print("FOUND")
else:
    print("NOT FOUND")
LL.delete_begin()
LL.delete_last()
print("after delete")
LL.display()
LL.delete_position(2)
print("after delete at position 2")
LL.display()









  