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
    def insert_position(self,data,index):
        # temp = self.head.next
        # previous  = self.head
        # initial_indx = 1
        # while temp is not None:
        #     if initial_indx == index:
        #         break
        #     else:
        #         initial_indx += 1
        #         temp = temp.next
        #         previous = previous.next
        # if temp is None:
        #     print(index,"is not valid index")
        # else:
        #     i_node = Node(data)
        #     i_node.next = previous.next
        #     previous.next = i_node
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
    def delete_node(self,data):
        temp = self.head.next
        previous = self.head
        while temp is not None:
            if temp.data == data:
                break
            else:
                temp = temp.next
                previous = previous.next
        if temp is None:
            print(data, "is not present in linked list")
        else:
            previous.next = temp.next
            temp.next = None

    def delete_position(self, pos):
        temp = self.head.next
        prev = self.head
        for i in range(pos - 1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def max(self):
        temp = self.head
        max = temp.data
        while temp is not None:
            if temp.data > max:
                max = temp.data
            temp = temp.next
        print(max)
    def mean(self):
        sum = 0
        counter = 0
        temp = self.head
        while temp is not None:
            sum += temp.data
            counter += 1
            temp = temp.next
        print(sum/counter)
    def reverse(self):
        temp = self.head
        counter = 0
        while temp is not None:
            if counter == 0:
                counter += 1
                temp = temp.next
                pass
            else:
                self.insert_begin(temp.data)
                temp = temp.next
                counter += 1
        for i in range(counter-1):
            self.delete_last()

    def sort(self):
        prev = self.head
        if self.head == None:
            print("linked list is empty")
        else:
            while prev != None:
                temp = prev.next
                while temp != None:
                    if prev.data > temp.data:
                        t = prev.data
                        prev.data = temp.data
                        temp.data = t
                    temp = temp.next
                prev = prev.next


# ll = single_linked_lst()
# ll.insert_begin(3)
# ll.insert_begin(2)
# ll.insert_begin(1)
# ll.display()
# ll.insert_begin(0)
# ll.display()
# ll.insert_end(100)
# ll.display()
# ll.delete_first()
# ll.display()
# ll.delete_last()
# ll.display()
# ll.insert_after(20,2)
# ll.display()
# ll.insert_before(15,2)
# ll.display()
# ll.insert_position(27,4)
# ll.display()
# ll.delete_node(20)
# ll.display()
# ll.max()
# ll.mean()
# ll.delete_position(3)
# ll.display()
# ll.max()
# ll.mean()
# ll.reverse()
# ll.display()
# ll.sort()
# ll.display()

def Menu():
    ll = single_linked_lst()
    while True:
        option = int(input("select one of the options below:\n 1. display the ll \n 2. insertion at start \n 3. insertion at end \n 4. insert at"
                           " certain position"
                           "\n 5. delete first element \n 6. delete last element \n 7. delete element at a position \n 8. find max of elements"
                           "\n 9. find mean of elements \n 10. sort the ll \n 11. reverse the ll \n 12. quit \n ::--> "))
        if option == 1:
            ll.display()
        elif option == 2:
            data = int(input("Enter the input data: "))
            ll.insert_begin(data)
        elif option == 3:
            data = int(input("Enter the input data: "))
            ll.insert_end(data)
        elif option == 4:
            data = int(input("Enter the input data: "))
            index = int(input("Enter the index: "))
            ll.insert_position(data,index)
        elif option == 5:
            ll.delete_first()
        elif option == 6:
            ll.delete_last()
        elif option == 7:
            index = int(input("Enter the index: "))
            ll.delete_position(index)
        elif option == 8:
            ll.max()
        elif option ==9:
            ll.mean()
        elif option == 10:
            ll.sort()
        elif option == 11:
            ll.reverse()
        elif option == 12:
            break
        else:
            print("Invalid Input")
Menu()