class StackWithDynamicArray:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        self.stack = [None]*self.capacity
        self.top = 0
    def push(self,data):
        if self.length == self.capacity:
            new_stack = self.stack + [None]*self.capacity
            self.stack = new_stack
            self.capacity = len(self.stack)
        
        self.stack[self.top] = data
        self.top+=1
        self.length+=1
    def pop(self):
        if self.length==0:
            raise ValueError("UnderFlow")
        retValue = self.stack[self.top-1]
        self.stack[self.top-1] = None
        self.top-=1
        return retValue
        
    def __str__(self):
        retValue = ""
        for data in self.stack:
            retValue+="{}|".format(data)
        return retValue

def main():
    dStack = StackWithDynamicArray()
    dStack.push(3)
    dStack.push(4)
    dStack.push(5)
    dStack.push(6)
    dStack.push(7)
    dStack.pop()
    print(dStack)
main()
