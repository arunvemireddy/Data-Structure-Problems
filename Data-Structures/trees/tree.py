from stack import Stack
from queue import Queue


class Node:
    def __init__(self, data, left_node=None, right_node=None):
        self.data = data
        self.left = left_node
        self.right = right_node
    def __eq__(self,other):
        return self.data == other.data


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
            print(temp.data)
            if temp.left is not None:
                queue.enqueue(temp.left)
            if temp.right is not None:
                queue.enqueue(temp.right)
        del queue

    def __preorder_traverse(self, node):
        if(node is not None):
            print(node.data),
            self.__preorder_traverse(node.left)
            self.__preorder_traverse(node.right)

    def __inorder_traverse(self, node):
        if(node is not None):
            self.__inorder_traverse(node.left)
            print(node.data)
            self.__inorder_traverse(node.right)

    def __postorder_traverse(self, node):
        if(node is not None):
            self.__inorder_traverse(node.left)
            self.__inorder_traverse(node.right)
            print(node.data)

    def find_max(self, node):
        if node is None:
            return -999999

        current_data = node.data
        left_data = self.find_max(node.left)
        right_data = self.find_max(node.right)

        max = None
        if(left_data > right_data):
            max = left_data
        else: 
            max = right_data
        if(current_data > max):
            max = current_data
        
        return max
    def find_max_iterative(self):
        queue = Queue()
        max = -999999
        queue.enqueue(self.root)

        while not queue.is_empty():
            temp = queue.dequeue()
            if(temp.data > max):
                max = temp.data

            if temp.left is not None:
                queue.enqueue(temp.left)

            if temp.right is not None:
                queue.enqueue(temp.right)
        return max
    
    def search(self, node, value):
        if node is None:
            return False
        if node.data == value:
            return True
        left_value = self.search(node.left,value)
        if left_value:
            return left_value
        return self.search(node.right, value)
    
    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            temp = queue.dequeue()
            if temp.left is None:
                temp.left = new_node
                break
            else:
                queue.enqueue(temp.left)
            if temp.right is None:
                temp.right = new_node
                break
            else:
                queue.enqueue(temp.right)
        
        del queue
        return

    def size(self):
        return self.__size(self.root)

    def __size(self,node):
        if node is None:
            return 0
        
        left_size = 0
        right_size = 0
        
        if node.left is not None:
            left_size = self.__size(node.left)
        if node.right is not None:
            right_size = self.__size(node.right)
        
        return left_size+ 1 + right_size
        
    def __eq__(self,other):
        if self.head is None and other is None:
            return True
        
        if self.head or None and other is None:
            return True
        
        return self == other and self.left == other.left and self.right == other.right
            



def main():
    tree = Tree()
    tree2 = Tree()
    for i in range(10):
        tree.insert(i)
        tree2.insert(i)
    
    #tree.levelorder_traverse()
    print(tree==tree2)
    #print(tree.find_max(tree.root))
    #print(tree.find_max_iterative())
    #print(tree.search(tree.root, 2))
    
main()
