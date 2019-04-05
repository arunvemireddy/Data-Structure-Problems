from stack import Stack

#Used to Convert infix expression to postfix expression
class Convertor:
    def __init__(self):
        self.stack = Stack()
    
    # Method to check if char is operator
    # @@Param: char
    def is_operator(self,char):
        operators = {"+","-","/","*"}
        return char in operators

    # Method to check if char is Bracket
    # @@Param: char
    def is_bracket(self,char):
        brackets = {"(",")"}
        return char in brackets

    # Method to check if char is operand
    # @@Param: char
    def is_operand(self,char):
        operators = {"+","-","/","*",")","("}
        return char not in operators 
    
    #Method to return prority of the expression
    # @@Param: first operand, second operand
    def is_higher_pro(self,first,second):
        priority = {
            "(":17,
            ")":17,
            "[":17,
            "]":17,
            "*":15,
            "/":15,
            "%":15,
            "+":12,
            "-":12
            }
        if first in priority and second in priority:
            return priority[first] >= priority[second]
        return False
    
    #Method to convertan Infix expression to postfix expression
    # @@Param: string containing expression
    def infixToPostfix(self,expression):
        for char in expression:
            if self.is_operand(char):
                print(char),
            elif char == ")":
                top = self.stack.pop().data
                while top != "(":
                    if not self.is_bracket(top):
                        print(top),
                    top = self.stack.pop().data
            else:
                if char == "(":
                    self.stack.push(char)
                if not self.stack.is_empty():
                    if not self.is_higher_pro(char,self.stack.get_top()):
                        top = self.stack.pop().data
                        if not self.is_bracket(top):
                            print(top),
                self.stack.push(char)
                
        while not self.stack.is_empty():
             top = self.stack.pop().data
             if not self.is_bracket(top):
                 print(top),
                 
    # Method to evalute a postfix expression
    # @@Param: string containing a valid postfix expression
    def evaluatePostfix(self,expression):
        self.stack = Stack()
        for char in expression:
            if self.is_operand(char):
                self.stack.push(char)
            else:
                if not self.is_operand(char):
                    if not self.stack.is_empty():
                        second = self.stack.pop().data
                        first = self.stack.pop().data
                        _expression  = "{}{}{}".format(first,char,second)
                        self.stack.push(eval(_expression))
        print(self.stack.pop().data)
        

def main():
    convertor = Convertor()
    convertor.infixToPostfix("((A*B)+(C/D))")
    convertor.evaluatePostfix("123*+5-")
                
            
main()
