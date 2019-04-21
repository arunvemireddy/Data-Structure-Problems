from stack import Stack

# Function to traverse a tree in ZIG ZAG fashion
# Method uses two stacks
def zig_zag_traverse(node):
    if node is None:
        return 
    
    current_stack = Stack()
    next_stack = Stack()
    left_to_right = True
    current_stack.push(node)

    while not current_stack.is_empty():
        temp = current_stack.pop().data
        #print ("inslide node {}".format(temp.data))
        if temp:
            print(temp.data)
            if left_to_right:
                if temp.left:
                    next_stack.push(temp.left)
                if temp.right:
                    next_stack.push(temp.right)
            else:
                if temp.right:
                    next_stack.push(temp.right)
                if temp.left:
                    next_stack.push(temp.left)
                
        if current_stack.is_empty():
            left_to_right = not left_to_right
            current_stack,next_stack = next_stack,current_stack
    return
