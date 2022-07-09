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

    def insert_position(self,data,index):
        initial_indx = 1
        temp = self.head.next
        while temp is not None:
            if initial_indx == index-1:
                break
            else:
                initial_indx += 1
                temp = temp.next
        if temp is None:
            print(index,"is not valid index")
        else:
            i_node = Node(data)
            i_node.next = temp.next
            temp.next = i_node

    def delete_first(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp  = self.head
            self.head = temp.next
            temp.next = None
        del temp
    def delete_last(self):
        previous = self.head
        temp = self.head.next
        if previous.next is None:
            print("LL is empty")
        elif temp.next is None:
            previous.next = None
        else:
            while temp.next is not None:
                temp = temp.next
                previous = previous.next
        previous.next = None
    def delete_position(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None
    def delete_node(self,data):
        temp = self.head.next
        previous = self.head
        while previous is not None:
            if previous.data == data:
                break
            else:
                temp = temp.next
                previous = previous.next
        if previous.data is not data :
            return False
        else:
            previous.next = temp.next
            temp.next = None

    def isprime(self,data):
        if data > 1:
            for i in range(2, data):
                if (data % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    def delete_prime(self):
        counter = 1
        if self.head is None:
            print("ll is empty")
        elif self.head.next is None:
            if self.isprime(self.head.data):
                self.head = None
        else:
            prev = self.head
            # temp = self.head.next
            if self.isprime(prev.data):
                self.delete_first()
            while prev is not None:
                if self.isprime(prev.data):
                    self.delete_node(prev.data)
                    # self.delete_position(counter)
                prev = prev.next
                # temp = temp.next
                counter += 1

ll = single_linked_lst()
ll.insert_begin(2)
ll.insert_begin(1)
ll.insert_end(4)
ll.insert_end(5)
ll.insert_end(9)
ll.display()
ll.delete_prime()
ll.display()