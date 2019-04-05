from stack import Stack

# Function to reverse a stack
def reverse_stack(stack):
    x = None
    if not stack.is_empty():
        x = stack.pop().data
        print(x)
        reverse_stack(stack)
        stack.push(x)
        return stack

def main():
    stack = Stack()
    for i in xrange(10):
        stack.push(i)

    print(stack)

    print reverse_stack(stack)

    
    
main()        
