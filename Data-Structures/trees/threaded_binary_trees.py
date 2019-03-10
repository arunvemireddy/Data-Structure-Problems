from queue import Queue

class Node:
    def __init__(self,data):
        self.data = data
        self.left_tag = False
        self.right_tag = False
        self.left_child = None
        self.right_child = None
class ThreadedBinaryTree:
    def __init__(self):
        self.root = None
        self.dummy_node = Node(self,None)
        self.dummy_node.right_child = self.dummy_node
        self.dummy_node.right_tag = True
    def get_inorder_successor(self,node):
        if not node.right_tag:
            return node.right_child
        position = None
        while node.right_tag:
            position = node.left_child
        return position
    