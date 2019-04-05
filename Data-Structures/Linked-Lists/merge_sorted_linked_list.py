from circular_linked_list import CLinkedList

#Function to merge a sorted linked list
# @@Param: first_list, second_list
def merge_sorted_linked_list(aNode,bNode):
    if(aNode == None):
        return bNode
    if(bNode == None):
        return aNode
    if(aNode.data <=bNode.data):
        result = aNode
        result.next = merge_sorted_linked_list(aNode.next,bNode)
    else:
        result = bNode
        result.next = merge_sorted_linked_list(aNode,bNode.next)
    return result
        
    
        

def main():
    aList = CLinkedList()
    bList = CLinkedList()
    for i in xrange(1,10,2):
        aList.insert_node(i)
        bList.insert_node(i+1)

    aList.traverse()
    bList.traverse()

    #Circular linked list to normal linked list conversion
    aList._CLinkedList__get_last_node().next = None
    bList._CLinkedList__get_last_node().next = None

    newList = merge_sorted_linked_list(aList.head,bList.head)

    while newList is not None:
        print("{} - >".format(newList.data)),
        newList = newList.next
    print("(end)")

main()
