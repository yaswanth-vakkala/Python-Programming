class Node:
   
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None
class DLL:
  
    def __init__(self):
        self.head=None  #initially empty DLL
    
    def display(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            temp=self.head  #temp, self.head will point to first node
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next
        print("")
    #printing in reverse
    def display_reverse(self):
        if self.head is None:
            print("DLL is Empty")
        else:
            #go to last node and print data
            #go to previous node and print data and repeat till u reach node1
            temp=self.head
            #go to last node
            while temp.next is not None:
                temp=temp.next
            while temp is not None:
                print(temp.data,end=" ")
                #go to previous node
                temp=temp.previous
                
    #insert at beginning of DLL
    def insert_begin(self,data):
        new_node=Node(data)
        #2 cases: if adding new node to empty LL
        #and another condition is Nonempty LL
        temp=self.head
        if self.head is None:
            self.head=new_node
        else:
            #update next of new_node
            new_node.next=self.head
            #update previous of node 1, which is after new_node
            temp.previous=new_node   #self.head.previous=new_node
            #change head position to new_node
            self.head=new_node
        
    #insert at end of DLL, travel to last node, till temp points to last node
    def insert_end(self,data):
         new_node=Node(data)
         if self.head is None:
             self.head=new_node
         else:
          temp=self.head
          #go to last Node
          while temp.next is not None:
              temp=temp.next
          #update last node next to new_node
          temp.next=new_node
          #update new_node previous with last node
          new_node.previous=temp
         
    def insert_position(self,data,pos):
        new_node=Node(data)
        temp=self.head.next
        before=self.head
        for i in range(pos-1):
            temp=temp.next
            before=before.next
        new_node.previous=before
        before.next=new_node
        new_node.next=temp
        temp.previous=new_node
       
    #delete begin of DLL
    def delete_begin(self):
        temp=self.head
         #point head to second Node      
        self.head=temp.next
         #change first node,temp next to None,disconnect link from n1 to n2
        temp.next=None
        #change second node previous to None
        self.head.previous=None
       
    def delete_end(self):
        #disconnect link between las node and last but 1 node
        #travel from first node to last node
        temp=self.head.next
        before=self.head
        #TRAVESING FROM NODE 1 TO LAST NODE, TEMP--LAST NODE, BEFORE--LAST BUT 1 NODE
        while temp.next is not None:
            temp=temp.next
            before=before.next
        before.next=None
        temp.previous=None
        
    def delete_position(self,pos):
        
        temp=self.head.next
        before=self.head
        for i in range(pos-1):
            temp=temp.next
            before=before.next
        if before==self.head:
            self.delete_begin()
            
        elif temp.next==None:
            self.delete_end()
        else:
            before.next=temp.next
            temp.next.previous=before
            temp.previous=None
            temp.next=None
           

LL=DLL()
'''n1=Node(10)
LL.head=n1
n2=Node(20)
n1.next=n2
n2.previous=n1
n3=Node(30)
n2.next=n3
n3.previous=n2'''
LL.display()
LL.insert_begin(5)  
LL.insert_begin(6)
LL.insert_begin(7)
LL.insert_end(100)
LL.insert_position(23,2)
LL.delete_begin()
LL.delete_end()
LL.insert_end(100)
LL.insert_end(200)
LL.display()
LL.delete_position(1)
LL.display()
