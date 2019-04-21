class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

# Function to convert a Doubly Linked List to a Binary Seach Tree
# @@Param: head of Doubly Linked List
def convert_dll_to_bst(head):
    if not head or not head.next:
        return head
    p = head
    middle = get_middle(head)
    
    while p.next != middle : 
        p = p.next
    p.next  = None
    q = middle.next
    middle.next = None
    middle.left = convert_dll_to_bst(head)
    middle.right = convert_dll_to_bst(q)

    return middle

# Function to find the middle of a linked list
def get_middle(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer.next and fast_pointer.next.next:
        slow_pointer = slow_pointer.next 
        fast_pointer = fast_pointer.next.next
    print("middle",slow_pointer)
    return slow_pointer

def __inorder_traverse(node):
        if(node is not None):
            __inorder_traverse(node.left)
            print(node.data)
            __inorder_traverse(node.right)

def main():
    head = Node(1)
    temp = head
    for i in range(2,8):
        new_node = Node(i)
        temp.next = new_node
        new_node.prev = temp
        temp = temp.next
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
    tree = convert_dll_to_bst(head)
    print(tree)
    __inorder_traverse(tree)
main()