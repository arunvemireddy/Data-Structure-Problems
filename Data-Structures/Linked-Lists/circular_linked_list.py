class CLNode:
    # Constructor
    # @@Param: data, next_node [optional]
    def __init__(self, data, nNode=None):
        if nNode is not None:
            self.next = nNode
        else:
            self.next = self
        self.data = data
    def __str__(self):
        return "{} -> {}".format(self.data,self.next.data)

class CLinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    # method to insert node into list
    # @@Param: data, position
    def insert_node(self, data, *position):
        if len(position) ==0:
            position = self.count
        else:
            position = position[0]
            if position > self.count:
                print("Invalid position")
                return
            
        if self.head is None:
            print("List is empty inserting at start")
            self.head = CLNode(data)
            self.__increment_counter()
            return

        if position == 0:
            new_node = CLNode(data, self.head)
            last_node = self.__get_last_node()
            last_node.next = new_node
            self.head = new_node
            self.__increment_counter()
            return
        
        counter = 1
        temp = self.__get_node(position-1)
        new_node = CLNode(data, temp.next)
        temp.next = new_node
        self.__increment_counter()

    # Method to delete node
    # @@Param: position
    def delete_node(self,position):
        if self.head is None:
            print("List is empty")
            return
        if position ==0:
            if(self.count ==1):
                self.head = None
            else:
                second_node = self.__get_node(1)
                last_node = self.__get_last_node()
                last_node.next = second_node
                self.head = second_node
                del second_node
        else:
            previous_node = self.__get_node(position-1)
            current_node = previous_node.next
            previous_node.next = current_node.next
            del current_node
        self.__increment_counter(-1)
        
    #Method to traverse the list
    def traverse(self):
        if self.head is None:
            print("Empty List")
            return
        ret_value = self.head
        print("{}->".format(ret_value.data)),
        while ret_value.next != self.head:
            ret_value = ret_value.next
            print("{} ->".format(ret_value.data)),
        print('(head)')

    def __get_node(self,index):
        counter = 0
        temp = self.head
        while counter < index:
            temp = temp.next
            counter +=1
        return temp
    
    def __get_last_node(self):
        ret_value = self.head
        while ret_value.next != self.head:
            ret_value = ret_value.next
        return ret_value
    
    def __increment_counter(self,op=1):
        self.count +=op

def main():
    link_list = CLinkedList()
    link_list.insert_node(3)
    link_list.insert_node(4)
    link_list.insert_node(5)
    link_list.insert_node(6)
    link_list.traverse()
    link_list.delete_node(0)
    link_list.delete_node(0)
    link_list.delete_node(0)
    link_list.delete_node(0)
    link_list.traverse()
main()
