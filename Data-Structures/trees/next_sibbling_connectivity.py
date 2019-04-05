from queue import Queue
from tree import Tree

# function to add new node into a next sibbling tree
# @@Param: root node
def insert_next_sibbling(node):
    queue = Queue()
    queue.enqueue(node.root)
    queue.enqueue(None)

    while not queue.is_empty():
        temp = queue.dequeue()
        if not temp:
            if not queue.is_empty():
                queue.enqueue(None)
        else:
            temp.next_sibbling = queue.peek()
            if temp.left:
                queue.enqueue(temp.left)
            if temp.right:
                queue.enqueue(temp.right)
    del queue
    return


def insert_next_sibbling_rec(node):
    if not node:
        return
    if node.left:
        node.left.next_sibbling = node.right
    if node.right:
        next_sib = node.next_sibbling
        if next_sib:
            next_sib = next_sib.left
        node.right.next_sibbling = next_sib
    insert_next_sibbling_rec(node.left)
    insert_next_sibbling_rec(node.right)

# Function to traverse next sibbling tree
# @@Param: root node
def traverse_next_sibbling_tree(tree):
    root = tree.root
    queue = Queue()
    queue.enqueue(root)
    while not queue.is_empty():
        temp = queue.dequeue()
        if temp:
            if temp.left:
                queue.enqueue(temp.left)
            print(temp.data),
            current_temp = temp.next_sibbling
            while(current_temp):
                print(current_temp.data),
                current_temp = current_temp.next_sibbling
        
    

def main():
    tree = Tree()
    for i in range(10):
        tree.insert(i)
    tree.root.next_sibbling = None
    insert_next_sibbling_rec(tree.root)
    traverse_next_sibbling_tree(tree)
main()
