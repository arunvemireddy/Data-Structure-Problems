from stack import Stack

class InfixToPostFix:
    def __init__(self):
        self.stack = Stack()
    def isOperator(char):
        operators = {"+","-","/","*"}
        return char in operators
    def convert(self,expression):
        for char in expression:
            if not isOperator(char):
                self.stack.push(char)
            elif( char == ")"):
                top = self.stack.pop().data
                while top != "(":
                    if top!="(":
                        print(top,end=" ")
                    top = self.stack.pop().data
            else:
                top = self.stack.pop().data
                while not self.stack.isEmpth() or top != ")":
                     if top!="(":
                        print(top,end=" ")
                        top = self.stack.pop().data
                self.stack.push(char)
            print(char,end=" ")
                
            
            
