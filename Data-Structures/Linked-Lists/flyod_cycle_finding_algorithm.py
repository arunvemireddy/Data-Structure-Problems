from circular_linked_list import CLinkedList

def floyd_cycle_finding(head):
    slowPointer = head
    fastPointer = head
    
    while True:
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
        print("slow:({}) fast:({})".format(slowPointer.data,fastPointer.data))
        if slowPointer == fastPointer:
            print("Cycle found")
            return
        if fastPointer == None:
            print("No Cycle found")
            return
    
        

def main():
    link_list = CLinkedList()
    for i in xrange(100):
        link_list.insert_node(i)
    
    link_list.traverse()
    #Creating a cycle in linked list
    last_node = link_list._CLinkedList__get_last_node()
    nth_node = link_list._CLinkedList__get_node(6)
    last_node.next = nth_node

    floyd_cycle_finding(link_list.head)
    print("end")
main()
