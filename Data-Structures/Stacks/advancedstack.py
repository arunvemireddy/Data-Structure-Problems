from stack import Stack

class AdvancedStack(Stack):
    def __init__(self):
        self.min_stack = Stack()
        self.stack = Stack()
        
    def push(self,data):
        if self.min_stack.is_empty():
            self.min_stack.push(data)
        else:
            top = self.stack.get_top()
            if(data<=top):
                self.min_stack.push(data)
        self.stack.push(data)
    def pop(self):
        poped_value = self.stack.pop().data
        if(poped_value == self.min_stack.get_top()):
            self.min_stack.pop()
        
        
    def get_min_value(self):
        return self.min_stack.get_top()

    
def main():
    stack = AdvancedStack()
    for i in xrange(1,9):
        stack.push(i)
    print stack.get_min_value()
    stack.push(-1)
    print stack.get_min_value()
    stack.push(-5)
    print stack.get_min_value()
main()
