class AVLTreeNode:
    def __init__(self,data):
        self.left = None 
        self.right = None
        self.data = data
        self.height = 0

class AVLTree:
    def __init__(self):
        self.head = None
    def single_rotation_left(self,disbalanced_node):
        newParent = disbalanced_node.left
        disbalanced_node.left = newParent.right
        newParent.right = disbalanced_node
        #calculate height for newParent
        newParent.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right)) 
        #calculate height for disbalanced_node
        disbalanced_node.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right))

        return newParent
    def single_rotation_right(self,disbalanced_node):
        newParent = disbalanced_node.right
        disbalanced_node.right = newParent.left
        newParent.left = disbalanced_node
        #calculate height for newParent
        newParent.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right)) 
        #calculate height for disbalanced_node
        disbalanced_node.height = max(self.get_height(disbalanced_node.left),self.get_height(disbalanced_node.right))

        return newParent

    def double_rotation_lr(self,disbalanced_node):
        disbalanced_node.left = single_rotation_right(disbalanced_node.left)
        return single_rotation_left(disbalanced_node)
    
    def double_rotation_rl(self,disbalanced_node):
        disbalanced_node.right = single_rotation_left(disbalanced_node.right)
        return single_rotation_right(disbalanced_node)
    

    def insert(self,node,data):
        if node is None:
            return AVLTreeNode(data)
        if data < node.data:
            node.left =  self.insert(node.left,data)
        else:
            node.right =  self.insert(node.right,data)
        balanced = self.get_height(node.left) - self.get_height(node.right)

        if balanced > 1:
            #left size is unbalanced
            if self.get_height(node.left.left) > self.get_height(node.left.right):
                ##left left
                node.left = self.single_rotation_left(node.left)
            else:
                node.left = self.double_rotation_lr(node.left) 
        if balanced < -1:
            #right size is unbalanced
            if self.get_height(node.right.right) > self.get_height(node.right.left):
                node.right = self.single_rotation_right(node.right)
            else:
                node.right = self.double_rotation_rl(node.right)
        node.height = 1+ max(self.get_height(node.left),self.get_height(node.right))
        return node



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
    for i in range(10):
        tree.head = tree.insert(tree.head,10-i)

    tree.inorder_traverse(tree.head)
main()