from stack import Stack

class AdvancedStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.minStack = Stack()
    def push(self,data):
        if Stack.is_empty():
            self.minStack.push(data)
        else:
            top = Stack.get_top()
            if(data<top):
                self.minStack.push(data)
        Stack.push(self,data)
    def get_min(self):
    
def main():
    stack = AdvancedStack()
    stack.push('shubham')
    print(stack)
main()
