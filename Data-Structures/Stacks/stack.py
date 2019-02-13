class Node:
    def __init__(self,data,nNode=None):
        self.data = data
        self.next = nNode

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
    def push(self,data):
        if self.head is None:
            self.head = Node(data,None)
            self.length +=1
            return
        new_node = Node(data,self.head)
        self.head = new_node
        self.length +=1
    
    def pop(self):
        if self.length == 0:
            raise ValueError("Under Flow Condition")
        retValue = self.head
        self.head = self.head.next
        return retValue

    def __str__(self):
        message = ""
        traverse = self.head
        while traverse is not None:
            
        
