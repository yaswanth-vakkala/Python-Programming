class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class single_linked_lst():
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("It is an empty linked list")
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,"-->|",end=" ")
                temp = temp.next
        print("")
    def insert_begin(self,data):
        begin_n = Node(data)
        if self.head is None:
            self.head = begin_n
        else:
            begin_n.next = self.head
            self.head = begin_n
    def insert_end(self,data):
        end_n = Node(data)
        if self.head == None:
            self.head = end_n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = end_n
    def insert_after(self,data,s_data):
        temp = self.head
        while temp is not None:
            if temp.data == s_data:
                break
            else:
                temp = temp.next
        if temp is None:
            print(s_data,"is not in linked list")
        else:
            a_node = Node(data)
            a_node.next = temp.next
            temp.next = a_node
    def insert_before(self,data,s_data):
        temp = self.head.next
        previous = self.head
        while temp is not None:
            if temp.data == s_data:
                break
            else:
                temp = temp.next
                previous = previous.next
        if temp is None:
            print(s_data,"is not in linked list")
        else:
            b_node = Node(data)
            previous.next = b_node
            b_node.next = temp
