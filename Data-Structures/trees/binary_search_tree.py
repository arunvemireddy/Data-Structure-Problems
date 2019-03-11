from tree import Node
from random import randrange
class BinarySearchTree:
    def __init__(self):
        self.root = None
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
    def inorder_traverse(self):
        self.__inorder_traverse(self.root)
    def __inorder_traverse(self,node):
        if not node:
            return
        self.__inorder_traverse(node.left)
        print(node.data)
        self.__inorder_traverse(node.right)
    def find_min(self,node):
        if not node:
            raise ValueError("empty tree")
        current = node
        while current.left is not None:
            current = current.left
        return current
    def find_max(self,node):
        if not node:
            raise ValueError("empty tree")
        current = node
        while current.right is not None:
            current = current.right
        return current
    
    def find(self,node,data):
        if not node:
            return None
        if node and node.data == data:
            return node
        if data < node.data:
            return self.find(node.left,data)
        elif data > node.data:
            return self.find(node.right,data)
    def is_bst(self,node):
        if node is None:
            return True
        if node.left and self.find_max(node.left).data < node.data:
            return True
        if node.right and self.find_min(node.right).data > node.data:
            return True
        if not self.is_bst(node.left) or not self.is_bst(node.right):
            return False
        return True
def main():
    tree = BinarySearchTree()
    for i in range(10):
        number = randrange(0,100)
        tree.insert(number)
    tree.inorder_traverse()
    print(tree.is_bst(tree.root))

main()
            