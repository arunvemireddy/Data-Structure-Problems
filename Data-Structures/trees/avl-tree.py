class AVLTreeNode:
    def __init__(self,data):
        self.left = None 
        self.right = None
        self.data = data
        self.height = 0

class AVLTree:
    def __init__(self):
        self.head = None
    def left_left_rotation(self,disbalanced_node):
        newParent = disbalanced_node.left
        disbalanced_node.left = newParent.right
        newParent.right = disbalanced_node
        #calculate height for newParent
        newParent.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right)) 
        #calculate height for disbalanced_node
        disbalanced_node.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right))

        return newParent
    def right_right_rotation(self,disbalanced_node):
        newParent = disbalanced_node.right
        disbalanced_node.right = newParent.left
        newParent.left = disbalanced_node
        #calculate height for newParent
        newParent.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right)) 
        #calculate height for disbalanced_node
        disbalanced_node.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right))

        return newParent
    
    def get_height(self,node):
        if node is None:
            return -1
        return node.height
    
    def construct_tree(self):
        self.head = AVLTreeNode(10)
        self.head.left = AVLTreeNode(20)
        self.head.left.left = AVLTreeNode(30)
    def inorder_traverse(self,node):
        if node is None:
            return 
        self.inorder_traverse(node.left)
        print(node.data)
        self.inorder_traverse(node.right)

def main():
    tree = AVLTree()
    tree.construct_tree()
    tree.inorder_traverse(tree.head)
    tree.head = tree.left_left_rotation(tree.head)
    print(tree.head.left.data, tree.head.data, tree.head.right.data)
main()