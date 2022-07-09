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
        # i_node = Node(data)
        # if self.head is None:
        #     self.head = i_node
        # elif self.head.next is None:
        #     self.head.next = i_node
        #     i_node.prev = self.head
        # else:
        #     i_node = Node(data)
        #     temp = self.head.next
        #     prev = self.head
        #     for i in range(index-1):
        #         temp = temp.next
        #         prev = prev.next
        #     i_node.prev = prev
        #     prev.next = i_node
        #     i_node.next = temp
        #     temp.prev = i_node
        if self.head is None:
            self.head = Node(data)
        elif self.head.next is None:
            i_node = Node(data)
            self.head.next = i_node
            i_node.prev = self.head
        # elif self.head.next.next is None:
        #     i_node = Node(data)
        #     self.head.next.next = i_node
        #     i_node.prev = self.head.next
        # elif self.head.next.next.next is None:
        #     i_node = Node(data)
        #     self.head.next.next.next = i_node
        #     i_node.prev = self.head
        elif index == 0:
            i_node = Node(data)
            i_node.next = self.head
            self.head.prev = i_node
            self.head = i_node
        elif index == 1:
            i_node = Node(data)
            temp = self.head.next
            self.head.next = i_node
            i_node.prev = self.head
            i_node.next = temp
            temp.prev = i_node
        else:
            counter = 0
            temp = self.head
            while temp.next is not None:
                temp = temp.next
                counter += 1
            if temp.next is None and index == counter+1:
                self.insert_end(data)
            else:
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
        # else:
        #     initial_indx = 1
        #     temp = self.head.next
        #     prev = self.head
        #     while temp is not None:
        #         if initial_indx == index - 1:
        #             break
        #         else:
        #             initial_indx += 1
        #             temp = temp.next
        #             prev = prev.next
        #     if temp is None:
        #         print(index, "is not valid index")
        #     else:
        #         i_node = Node(data)
        #         i_node.next = temp.next
        #         i_node.next.prev = i_node
        #         temp.next = i_node
        #         i_node.prev = temp


    def display_odd(self):
        if self.head is None:
            print("It is an empty linked list")
        else:
            counter = 1
            temp = self.head
            while temp is not None:
                if counter % 2 != 0:
                    print(temp.data,"-->|",end=" ")
                temp = temp.next
                counter += 1
        print("")


dll = double_linked_list()
# dll.insert_begin(1)
# dll.insert_begin(2)
# dll.insert_end(9)
# dll.insert_end(10)
# dll.display()
# dll.insert_postion(5,2)
# dll.display()
# dll.insert_postion(7,4)
# dll.display()
# dll.insert_postion(15,5)
# dll.display()
# dll.insert_postion(12,3)
# dll.display()
# dll.display_odd()
dll.insert_postion(1,0)
dll.insert_postion(2,1)
dll.display()
dll.insert_postion(12,0)
dll.display()
dll.insert_postion(100,3)
dll.display()
dll.insert_postion(5,2)
dll.display()
dll.insert_postion(7,3)
dll.display()
dll.insert_postion(9,4)
dll.display()
dll.insert_postion(3,2)
dll.display()
print("odd position output is:")
dll.display_odd()