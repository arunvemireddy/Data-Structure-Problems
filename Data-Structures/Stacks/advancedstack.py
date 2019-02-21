from stack import Stack

class AdvancedStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.min_stack = Stack()
    def push(self,data):
        if self.is_empty():
            self.min_stack.push(data)
        else:
            top = Stack.get_top()
            if(data<top):
                self.min_stack.push(data)
        Stack.push(self,data)
    def get_min(self):
        return self.min_stack.get_top()
    
def main():
    stack = AdvancedStack()
    for i in xrange(10):
        stack.push(i)
    print(stack.get_min())
main()
