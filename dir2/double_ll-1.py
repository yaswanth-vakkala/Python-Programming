class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class double_linked_list():
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

    def display_reverse(self):
        if self.head is None:
            print("It is an empty list")
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            while temp is not None:
                print(temp.data, "-->|", end=" ")
                temp = temp.prev
        print("")
    def insert_begin(self,data):
        begin_n = Node(data)
        if self.head is None:
            self.head = begin_n
        else:
            begin_n.next = self.head
            self.head.prev = begin_n
            self.head = begin_n

    def insert_end(self,data):
        end_n = Node(data)
        if self.head.next == None:
            self.head = end_n
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = end_n
            end_n.prev = temp

    def insert_postion(self,data,index):
        i_node = Node(data)
        temp = self.head.next
        prev = self.head
        for i in range(index-1):
            temp = temp.next
            prev = prev.next
        i_node.prev = prev
        prev.next = i_node
        i_node.next = temp
        temp.prev = i_node

    def delete_begin(self):
        if self.head is None:
            print("linked list is emtpy")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.head.prev = None
            del temp
    def delete_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None
        temp.prev = None

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
            temp.next.prev = previous
            temp.prev = None
            temp.next = None

    def delete_position(self, index):
        # initial_indx = 1
        # temp = self.head.next
        # prev = self.head
        # while temp is not None:
        #     if initial_indx == index - 1:
        #         break
        #     else:
        #         initial_indx += 1
        #         temp = temp.next
        #         prev = prev.next
        # if prev == self.head:
        #     self.head = temp
        #     temp.prev = None
        #     prev.next = None
        # elif temp == None:
        #     prev.next = None
        #     temp.prev = None
        # else:
        #     prev.next = temp.next
        #     temp.next.prev = prev
        #     temp.prev = None
        #     temp.next = None
        #

        temp = self.head.next
        prev = self.head
        for i in range(index-1):
            temp = temp.next
            prev = prev.next
        if index == 1:
            temp = self.head.next
            prev = self.head
            prev.next = temp.next
            temp.next.prev = prev
            temp.next = None
            temp.prev = None
        elif prev == self.head:
            self.head = temp
            temp.prev = None
            prev.next = None
        elif temp.next == None:
            prev.next = None
            temp.prev = None
        else:
            prev.next = temp.next
            temp.next.prev = prev
            temp.prev = None
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
        print(sum / counter)
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
        for i in range(counter - 1):
            self.delete_end()

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


# obj = double_linked_list()
#
# obj.insert_begin(3)
# obj.insert_begin(2)
# obj.insert_begin(1)
# obj.display()
# obj.display_reverse()
# obj.insert_end(4)
# obj.insert_end(5)
# obj.display()
# obj.delete_begin()
# obj.display()
# obj.delete_end()
# obj.display()
# obj.insert_postion(22,1)
# obj.insert_postion(20,1)
# obj.display()
# obj.delete_node(22)
# obj.display()
# obj.reverse()
# obj.display()
# obj.delete_position(1)
# obj.display()
# obj.max()
# obj.mean()
# obj.reverse()
# obj.display()
# obj.sort()
# obj.display()

def Menu():
    ll = double_linked_list()
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
            ll.insert_postion(data,index)
        elif option == 5:
            ll.delete_begin()
        elif option == 6:
            ll.delete_end()
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