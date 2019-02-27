from stack import Stack
from queue import Queue

class Node:
    def __init__(self,data,left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node
class Tree:
    def __init__(self):
        self.root = None
        self.height = 0
    def preorder_traverse(self):
        self.__preorder_traverse(self.root)
    def inorder_traverse(self):
        self.__inorder_traverse(self.root)
    def postorder_traverse(self):
        self.__postorder_traverse(self.root)
        
    def preorder_traverse_itretive(self):
        stack = Stack()
        root = self.root
        while True:
            while root:
                print(root.data)
                stack.push(root)
                root = root.left
            if stack.is_empty():
                break
            root = stack.pop().data
            root = root.right
    def inorder_traverse_iterative(self):
        stack = Stack()
        root = self.root
        while True:
            while root:
                stack.push(root)
                root = root.left
            if stack.is_empty():
                break
            root = stack.pop().data
            print(root.data)
            root = root.right
            
    def levelorder_traverse(self):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        while(not queue.is_empty()):
            temp = queue.dequeue()
            print temp.data
            if temp.left is not None:
                queue.enqueue(temp.left)
            if temp.right is not None:
                queue.enqueue(temp.right)
            print(queue)
        del queue
    
    def __preorder_traverse(self,node):
        if(node is not None):
            print(node.data),
            self.__preorder_traverse(node.left)
            self.__preorder_traverse(node.right)

    def __inorder_traverse(self,node):
        if(node is not None):
            self.__inorder_traverse(node.left)
            print(node.data)
            self.__inorder_traverse(node.right)
    def __postorder_traverse(self,node):
        if(node is not None):
            self.__inorder_traverse(node.left)
            self.__inorder_traverse(node.right)
            print(node.data)

    def setup(self):
        self.root = Node(1)
        first_node = Node(2)
        second_node = Node(3)
        self.root.left = first_node
        self.root.right = second_node
        third_node = Node(4)
        fourth_node = Node(5)
        fifth_node = Node(6)
        sixth_node = Node(7)
        first_node.left = third_node
        first_node.right = fourth_node
        second_node.left = fifth_node
        second_node.right = sixth_node
        
def main():
    tree =Tree()
    tree.setup()
    #tree.preorder_traverse_itretive()
    #tree.inorder_traverse()
    #print('break')
    #tree.inorder_traverse_iterative()
    #tree.postorder_traverse()
    tree.levelorder_traverse()
main()
