class CLNode:
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
        temp = self.head
        while counter < position:
            temp = temp.next
            counter += 1
        
        new_node = CLNode(data, temp.next)
        temp.next = new_node
        self.__increment_counter()

    def __get_last_node(self, verbose=False):
        ret_value = self.head
        while ret_value.next != self.head:
            ret_value = ret_value.next
        return ret_value

    def traverse(self):
        ret_value = self.head
        print("{}->".format(ret_value.data)),
        while ret_value.next != self.head:
            ret_value = ret_value.next
            print("{} ->".format(ret_value.data)),
        print('(head)')


    def __increment_counter(self):
        self.count +=1

def main():
    link_list = CLinkedList()
    link_list.insert_node(3)
    link_list.insert_node(4)
    link_list.insert_node(5)
    link_list.insert_node(10)
    link_list.traverse()
main()
