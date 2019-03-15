from tree import Tree
from tree import Node
from stack import Stack
from binary_search_tree import BinarySearchTree
from random import randrange

head = Node(None)

def find_path_with_sum(node,sum,path):
    if node is None:
        return
    path.append(node.data)
    if sum ==0:
        print(path)
    else:
        if sum > node.data:
            sum -= node.data
            
            find_path_with_sum(node.left,sum,path[:])
            find_path_with_sum(node.right,sum,path[:])

def mirror_tree(node):
    if node is None:
        return
    mirror_tree(node.left)
    mirror_tree(node.right)

    temp = node.left
    node.left = node.right
    node.right = temp

def is_mirror_trees(self,other):
    if self is None and other is None:
        return True
    if self is None or other is None:
        return False
    if  self.data != other.data:
        return False
    else:
        return is_mirror_trees(self.left,other.right) and is_mirror_trees(self.right,other.left)
        
def build_tree(preorder_string,inorder_string,start,end):
    if start > end:
        return None
    
    newNode = Node(preorder_string[build_tree.preorder_index])
    build_tree.preorder_index +=1
    if start == end:
        return newNode
    inorderIndex = inorder_string.index(preorder_string[build_tree.preorder_index])
    newNode.left = build_tree(preorder_string,inorder_string,start,inorderIndex-1) 
    newNode.right = build_tree(preorder_string,inorder_string,inorderIndex+1,end)
    return newNode

def convert_tree_to_dll(node):
 
    if node is None:
        return
    convert_tree_to_dll(node.left)
    if convert_tree_to_dll.prev is None:
        global head
        head = node
        print(head)

    else:
        node.left = convert_tree_to_dll.prev
        convert_tree_to_dll.prev.right = node
    convert_tree_to_dll.prev = node
    convert_tree_to_dll(node.right)
    
def copy_ref(self,other):
    if self is None or other is None:
        return None
    self.data = other.data
    self.left = other.left
    self.right = other.right
    return self

def convert_linked_list_to_bst(head):
    if head is None:
        return None
    queue = Queue()
    queue.enqueue(head)
    while not queue.is_empty():
        parent = queue.dequeue()
        left_child = right_child = None
        if head.next is not None:
            head = head.next
            left_child = head
            queue.enqueue(left_child)
        if head.next is not None:
            head = head.next
            right_child = head
            queue.enqueue(right_child)
        parent.left = left_child
        parent.right = right_child

def find_ceil(array,low,high,key):
    if key <array[low]:
        return low
    if key > array[high]:
        return -1
    mid = int((low+high)/2)
    
    if (key == array[mid]):
        return mid
    elif(key< array[mid]):
        if(mid-1> low and key >array[mid-1]):
            return mid
        else:
            find_ceil(array,low,mid-1,key)
    else:
        if(mid+1 <=high and key <= array[mid+1]):
            return mid+1
        else:
            return find_ceil(array,mid+1,high,key)

def range_print(node,k1,k2):
    if not None:
        return
    if node.data >= k1:
        range_print(node.left,k1,k2)
    if node.data >=k1 and node.data <=k2:
        print(node.data)
    if node.data <=k2:
        range_print(node.right,k1,k2)