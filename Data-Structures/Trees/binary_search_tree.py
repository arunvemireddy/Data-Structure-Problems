from tree import Node
from random import randrange
import sys

class BinarySearchTree:
    prev = -sys.maxint -1

    def __init__(self):
        self.root = None
    
    # Method to insert data into tree
    # @@Param: data
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
            return
        self.__insert(self.root,data)
    
    def __insert(self,node,data):
        if node is None:
            return Node(data)
        if data > node.data:
            node.right = self.__insert(node.right,data)
        elif data < node.data:
            node.left = self.__insert(node.left,data)
        return node
    
    # Method to display INORDER TRAVERSE
    def inorder_traverse(self):
        self.__inorder_traverse(self.root)
    def __inorder_traverse(self,node):
        if not node:
            return
        self.__inorder_traverse(node.left)
        print(node.data)
        self.__inorder_traverse(node.right)
    
    # Method to find the minimum value in the tree
    # @@Param: root node
    def find_min(self,node):
        if not node:
            raise ValueError("empty tree")
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # Method to find the max value from the tree
    # @@Param root node
    def find_max(self,node):
        if not node:
            raise ValueError("empty tree")
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    # Method to find if data exists into the tree
    # @@Param: root node, data to find
    def find(self,node,data):
        if not node:
            return None
        if node and node.data == data:
            return node
        if data < node.data:
            return self.find(node.left,data)
        elif data > node.data:
            return self.find(node.right,data)
    
    # Method to check if the tree is binary search tree
    # @@Param: root node
    def is_bst(self,node):
        if node is None:
            return True
        if not self.is_bst(node.left):
            return False
        if node.data < self.prev:
            return False
        self.prev = node.data
        return self.is_bst(node.right)

            