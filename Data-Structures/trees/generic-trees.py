from queue import Queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.first_node = None
        self.next_sibbling = None

def create_generic_tree(head_node):
    head_node.data = 1
    first_child = TreeNode(2)
    head_node.first_node = first_child
    second_child = TreeNode(3)
    first_child.next_sibbling = second_child
    third_child = TreeNode(4)
    second_child.next_sibbling = third_child
    fourth_child = TreeNode(5)
    first_child.first_node = fourth_child
    fifth_child = TreeNode(6)
    fourth_child.next_sibbling = fifth_child

def traverse_generic_tree(root,sum):
    queue = Queue()
    queue.enqueue(root)
    total = 0
    while not queue.is_empty():
        temp = queue.dequeue()
        total += temp.data
        print(temp.data),
        if temp.first_node is not None:
            queue.enqueue(temp.first_node)
        while temp.next_sibbling is not None:
            temp = temp.next_sibbling
            total += temp.data
            print(temp.data),
            if temp.first_node is not None:
                queue.enqueue(temp.first_node)
    if sum:
        print("Total: {}".format(total))
def find_childs(node):
    total = 0
    if node is None:
        return -1
    node = node.first_node
    while node is not None:
        total +=1
        node = node.next_sibbling
    return total
def is_tree_isomorphic(first,second):
    if not first  and not second :
        return True
    if (not first and second) or (first and not second):
        return False
    return is_tree_isomorphic(first.left,second.left) and is_tree_isomorphic(first.right,second.right)


def main():
    root  = TreeNode(0)
    create_generic_tree(root)
    traverse_generic_tree(root,True)
    print(find_childs(root))
main()