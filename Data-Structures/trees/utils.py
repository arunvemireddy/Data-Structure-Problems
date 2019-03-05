from tree import Tree
from tree import Node
from stack import Stack
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



