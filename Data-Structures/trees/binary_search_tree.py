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
def main():
    tree = BinarySearchTree()
    for i in range(10):
        number = randrange(0,100)
        tree.insert(number)
    tree.inorder_traverse()

main()
            